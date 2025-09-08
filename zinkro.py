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

    def to_ordinal(self):
        # Calcula el número de días desde el año 0-01-01 (no gregoriano)
        # No considera años bisiestos
        y = self.year
        m = self.month
        d = self.day
        # Días por año y mes
        days = y * 365 + (m - 1) * 30 + (d - 1)
        # Ajuste simple para meses reales
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if m > 1:
            days += sum(month_days[:m-1]) - (30 * (m-1))
        return days

    @staticmethod
    def from_ordinal(n: int):
        # Convierte un número de días a una fecha simple
        # No considera años bisiestos
        year = n // 365
        rem = n % 365
        # Aproximación: meses de 30 días
        month = rem // 30 + 1
        day = rem % 30 + 1
        # Ajuste para meses reales
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i, md in enumerate(month_days):
            if rem < md:
                month = i + 1
                day = rem + 1
                break
            rem -= md
        return SimpleDate(year, month, day)

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
        delta_days = date - self.start_date
        year = delta_days // 365
        day_of_year = delta_days % 365
        if day_of_year == self.days_in_year:
            return (year, None, None, True)  # Día Zero
        month = day_of_year // self.days_in_month + 1
        day = day_of_year % self.days_in_month + 1
        return (year, month, day, False)

    def zinkro_to_gregorian(self, year: int, month: int, day: int):
        """
        Convierte una fecha Zinkro a fecha gregoriana.
        """
        if month is None:
            # Día Zero
            days = year * 365 + self.days_in_year
        else:
            days = year * 365 + (month - 1) * self.days_in_month + (day - 1)
        return self.start_date + days

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
