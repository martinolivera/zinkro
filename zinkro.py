from typing import Tuple

# Clase simple para manejar fechas (año, mes, día) incluyendo años negativos
class SimpleDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def from_string(s: str):
        # Permite formato "-10000-03-20" o "2026-03-20"
        s = s.strip()
        # Detectar año negativo (puede tener más de 4 dígitos)
        if s.startswith('-'):
            # Buscar el segundo '-' (separador de mes)
            second_dash = s.find('-', 1)
            year = int(s[:second_dash])
            rest = s[second_dash+1:]
            parts = rest.split('-')
            if len(parts) == 2:
                month = int(parts[0])
                day = int(parts[1])
                return SimpleDate(year, month, day)
        else:
            parts = s.split('-')
            if len(parts) == 3:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
                return SimpleDate(year, month, day)
        raise ValueError("Formato de fecha inválido")

    def is_leap(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    def to_ordinal(self):
        # Calcula el número de días desde el año 0-01-01 (no gregoriano)
        y = self.year
        m = self.month
        d = self.day
        days = y * 365 + (m - 1) * 30 + (d - 1)
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if m > 1:
            days += sum(month_days[:m-1]) - (30 * (m-1))
        # Sumar días bisiestos desde -10000 hasta el año anterior a y
        leap_days = 0
        for yr in range(-10000, y):
            if self.is_leap(yr):
                leap_days += 1
        # Si el año actual es bisiesto y el mes > 2, sumar el día extra
        if self.is_leap(y) and m > 2:
            leap_days += 1
        days += leap_days
        return days

    @staticmethod
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    @staticmethod
    def from_ordinal(n: int):
        # Convierte un número de días a una fecha simple considerando bisiestos
        year = -10000
        days = n
        while True:
            leap = SimpleDate.is_leap(year)
            year_days = 365 + (1 if leap else 0)
            if days < year_days:
                break
            days -= year_days
            year += 1
        # Ahora days es el día dentro del año actual
        month_days = [31,29 if SimpleDate.is_leap(year) else 28,31,30,31,30,31,31,30,31,30,31]
        month = 1
        for md in month_days:
            if days < md:
                day = days + 1
                return SimpleDate(year, month, day)
            days -= md
            month += 1

    def __sub__(self, other):
        return self.to_ordinal() - other.to_ordinal()

    def __add__(self, days):
        return SimpleDate.from_ordinal(self.to_ordinal() + days)

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"
class ZinkroCalendar:
    def __init__(self, start_date):
        """
        start_date: instancia de SimpleDate
        """
        self.start_date = start_date
        self.days_in_month = 28
        self.months_in_year = 13
        self.days_in_year = self.days_in_month * self.months_in_year

    def gregorian_to_zinkro(self, date) -> Tuple[int, int, int]:
        """
        Convierte una fecha gregoriana a fecha Zinkro.
        Retorna (año, mes, día)
        
        El año Zinkro va de 20/3 a 19/3:
        - 20/3/Y = Día Zero del año Y (year = Y+10000, month=None, day=0)
        - 21/3/Y = Mes 1, Día 1 del año Y (year = Y+10000)
        - 19/3/Y+1 en bisiesto = Día 366 (year = Y+10000, month=None, day=366)
        
        IMPORTANTE: Las fechas antes del 20/3 pertenecen al año anterior.
        Ejemplo para 2028 (bisiesto):
        - 1-20 de febrero 2028: año 12027 (pertenecen a 2027)
        - 28-29 de febrero 2028: año 12027 (pertenecen a 2027)
        - 1-19 de marzo 2028: año 12027 (pertenecen a 2027)
        - 20 de marzo 2028: Día Zero del año 12028 ← CAMBIO
        - 21-31 de marzo 2028: año 12028 (pertenecen a 2028)
        """
        from datetime import date as datetime_date
        
        # CASO 1: Día Zero (20 de marzo) - CAMBIA EL AÑO
        if date.month == 3 and date.day == 20:
            yearZ = date.year + 10000  # ← AÑO ACTUAL
            return (yearZ, None, 0)  # Día = 0, Mes = None (indefinido)
        
        # Determinar a qué año Zinkro pertenece
        if date.month < 3 or (date.month == 3 and date.day < 20):
            # Antes del 20 de marzo: año anterior
            yearZ = (date.year - 1) + 10000
            year_ref = date.year - 1
        else:
            # Después del 20 de marzo: año actual
            yearZ = date.year + 10000
            year_ref = date.year
        
        # CASO 2: Después del 20 de marzo (21/3 - 31/3 - ... - 19/3 siguiente)
        if date.month == 3 and date.day > 20:
            # 21 de marzo en adelante del mismo año gregoriano
            month = 1
            day = date.day - 20
            return (yearZ, month, day)
        
        if date.month > 3:
            # Abril a diciembre del mismo año gregoriano
            march_21 = datetime_date(date.year, 3, 21)
            days_since = (datetime_date(date.year, date.month, date.day) - march_21).days
            
            month = days_since // 28 + 1
            day = days_since % 28 + 1
            return (yearZ, month, day)
        
        # CASO 3: Antes del 20 de marzo (enero, febrero, 1-19 de marzo)
        # Estos días pertenecen al año anterior
        # Contar días desde el 20 de marzo del año anterior hasta hoy
        
        march_20_ref = datetime_date(year_ref, 3, 20)
        current_date = datetime_date(date.year, date.month, date.day)
        days_from_prev_zero = (current_date - march_20_ref).days
        
        # days_from_prev_zero es el número de días DESPUÉS del Día Zero anterior
        # Ejemplo: 21 de marzo = 1 día, 22 de marzo = 2 días, etc.
        
        # IMPORTANTE: El año que puede ser bisiesto es date.year (el AÑO ACTUAL)
        # porque febrero 29 está en el año actual, no en el anterior
        is_leap_current = SimpleDate.is_leap(date.year)
        
        # Estructura del año Zinkro:
        # - Día Zero: 20/3 (no se cuenta aquí)
        # - Mes 1-13: 13*28 = 364 días
        # - Día 366 en bisiesto: 19/3 del siguiente año (cuando el año actual es bisiesto)
        # Total: 364 días (normal) o 365 días (bisiesto)
        
        # Mapeamos:
        # - Día 1-364: Meses 1-13, días 1-28 cada uno
        # - Día 365 (si el año ACTUAL es bisiesto): Mes indefinido, día especial 366
        
        # Calcular mes y día
        if days_from_prev_zero <= 364:
            # Encaja en los 13 meses normales
            month = (days_from_prev_zero - 1) // 28 + 1
            day = (days_from_prev_zero - 1) % 28 + 1
            return (yearZ, month, day)
        elif days_from_prev_zero == 365 and is_leap_current:
            # Día 366 especial en año bisiesto (19 de marzo cuando el año actual es bisiesto)
            return (yearZ, None, 366)  # Mes = None (indefinido), Día = 366
        else:
            # Esto shouldn't happen
            raise ValueError(f"Fecha fuera de rango: {date} (days={days_from_prev_zero}, is_leap_current={is_leap_current})")

    def zinkro_to_gregorian(self, year: int, month: int, day: int):
        """
        Convierte una fecha Zinkro a fecha gregoriana.
        """
        gregorian_year = year - 10000
        base_date = SimpleDate(gregorian_year, self.start_date.month, self.start_date.day)
        if month is None and day is None:
            # Día 366 Zinkro: corresponde al 29 de febrero gregoriano
            while not self.is_leap(gregorian_year):
                gregorian_year += 1
            return SimpleDate(gregorian_year, 2, 29)
        if month is None:
            days = (year - 10000) * 365 + self.days_in_year
        else:
            days = (year - 10000) * 365 + (month - 1) * self.days_in_month + (day - 1)
        return base_date + days

if __name__ == "__main__":
    # Ejemplo de uso
    # Configura el punto de inicio del calendario
    inicio = SimpleDate.from_string("-10000-03-20")
    cal = ZinkroCalendar(start_date=inicio)

    # Convertir fecha gregoriana a Zinkro
    fecha_gregoriana = SimpleDate.from_string("2025-07-15")
    zinkro = cal.gregorian_to_zinkro(fecha_gregoriana)
    print(f"Fecha gregoriana {fecha_gregoriana} -> Zinkro: {zinkro}")

    # Convertir fecha Zinkro a gregoriana
    fecha_gregoriana2 = cal.zinkro_to_gregorian(year=0, month=7, day=15)
    print(f"Zinkro año 0, mes 7, día 15 -> gregoriana: {fecha_gregoriana2}")

    # Día Zero
    dia_zero = cal.zinkro_to_gregorian(year=0, month=None, day=None)
    print(f"Zinkro año 0, Día Zero -> gregoriana: {dia_zero}")
