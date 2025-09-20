from typing import Tuple

# Clase simple para manejar fechas (año, mes, día) incluyendo años negativos
class SimpleDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def from_string(s: str):
        # Permite formato "-10000-03-21" o "2026-03-21"
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

    def gregorian_to_zinkro(self, date) -> Tuple[int, int, int, bool]:
        """
        Convierte una fecha gregoriana a fecha Zinkro.
        Retorna (año, mes, día, es_dia_zero)
        """
        # Calcular días totales desde el inicio Holoceno
        delta_days = date - self.start_date
        # Calcular año Zinkro y día dentro del año Zinkro considerando bisiestos
        yearZ = 0
        dias_restantes = delta_days
        while True:
            es_bisiesto = SimpleDate.is_leap(self.start_date.year + yearZ)
            dias_en_este_ano = 365 + (1 if es_bisiesto else 0)
            if dias_restantes < dias_en_este_ano:
                break
            dias_restantes -= dias_en_este_ano
            yearZ += 1
        # Día Zero: 21 de marzo de cualquier año
        if (date.month == 3 and date.day == 21):
            # Si es el inicio absoluto, año 0
            if delta_days == 0:
                return (0, None, None, True)
            # Si es otro año, Día Zero de ese año
            return (0, None, None, True)
        # Día 366 (extra) en año bisiesto
        if SimpleDate.is_leap(self.start_date.year + yearZ) and dias_restantes == 365:
            return (yearZ + 1, None, None, 'dia366')
            # Mapeo especial para fechas gregorianas de año bisiesto
        if SimpleDate.is_leap(date.year):
            # 29 de febrero
            if date.month == 2 and date.day == 29:
                return (yearZ + 1, 13, 9, False)
            # 1-19 de marzo
            if date.month == 3 and 1 <= date.day <= 19:
                return (yearZ + 1, 13, date.day + 9, False)
            if date.month == 3 and date.day == 20:
                return (yearZ + 1, None, None, 'dia366')
        else:
            # Año normal: 1-19 de marzo sumar +8, 20 de marzo es día 28
            if date.month == 3 and 1 <= date.day <= 19:
                return (yearZ + 1, 13, date.day + 8, False)
            if date.month == 3 and date.day == 20:
                return (yearZ + 1, 13, 28, False)
            if date.month == 3 and date.day == 20:
                return (yearZ + 1, None, None, 'dia366')
        # Normal: calcular mes y día Zinkro
        month = dias_restantes // self.days_in_month + 1
        day = dias_restantes % self.days_in_month + 1
        return (yearZ + 1, month, day, False)

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
    inicio = SimpleDate.from_string("-10000-03-21")
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
