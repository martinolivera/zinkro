#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejemplos de uso del calendario Zinkro
Demostraciones prácticas de conversión entre calendarios gregoriano y Zinkro
"""

from zinkro import SimpleDate, ZinkroCalendar

def print_section(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")

def main():
    # Inicializar el calendario Zinkro
    # El inicio es el 20 de marzo de -10000 (Era Holocena)
    cal = ZinkroCalendar(start_date=SimpleDate.from_string("-10000-03-20"))
    
    print_section("CALENDARIO ZINKRO - EJEMPLOS DE USO")
    
    # Ejemplo 1: Hoy es Día Zero
    print_section("1. Hoy es Día Zero (20 de marzo de 2026)")
    today = SimpleDate(2026, 3, 20)
    result = cal.gregorian_to_zinkro(today)
    print(f"Fecha Gregoriana: 2026-03-20 (Equinoccio de Primavera)")
    print(f"Fecha Zinkro: Día Zero (Año 0, Día Fuera del Tiempo)")
    print(f"Resultado de conversión: {result}")
    print(f"Interpretación: Es un Día Zero especial (reflexión, renovación)")
    
    # Ejemplo 2: Primer día del año Zinkro 12026
    print_section("2. Primer día del año Zinkro 12026")
    first_day = SimpleDate(2026, 3, 21)
    result = cal.gregorian_to_zinkro(first_day)
    print(f"Fecha Gregoriana: 2026-03-21")
    print(f"Fecha Zinkro: Año {result[0]}, Mes {result[1]}, Día {result[2]}")
    print(f"Interpretación: Primer día del mes 1 (Primavera) del año 12026 HE")
    
    # Ejemplo 3: Febrero en año bisiesto
    print_section("3. Febrero 29 en año bisiesto")
    leap_feb = SimpleDate(2028, 2, 29)
    result = cal.gregorian_to_zinkro(leap_feb)
    print(f"Fecha Gregoriana: 2028-02-29 (Año bisiesto)")
    print(f"Fecha Zinkro: Año {result[0]}, Mes 13 (Último mes), Día {result[2]}")
    print(f"Interpretación: Febrero 29 se mapea al mes 13 en el año Zinkro")
    
    # Ejemplo 4: Día en el mes 2 (Abril)
    print_section("4. Una fecha en Abril")
    april_day = SimpleDate(2026, 4, 15)
    result = cal.gregorian_to_zinkro(april_day)
    print(f"Fecha Gregoriana: 2026-04-15")
    print(f"Fecha Zinkro: Año {result[0]}, Mes {result[1]}, Día {result[2]}")
    print(f"Interpretación: {15 - 20} días después del Día Zero")
    
    # Ejemplo 5: Día en el mes 13 (Diciembre)
    print_section("5. Una fecha en Diciembre")
    dec_day = SimpleDate(2026, 12, 15)
    result = cal.gregorian_to_zinkro(dec_day)
    print(f"Fecha Gregoriana: 2026-12-15")
    print(f"Fecha Zinkro: Año {result[0]}, Mes {result[1]}, Día {result[2]}")
    
    # Ejemplo 6: Próximo Día Zero (2027)
    print_section("6. Próximo Día Zero (20 de marzo de 2027)")
    next_zero = SimpleDate(2027, 3, 20)
    result = cal.gregorian_to_zinkro(next_zero)
    print(f"Fecha Gregoriana: 2027-03-20")
    print(f"Fecha Zinkro: {result}")
    print(f"Interpretación: El Día Zero se repite cada año el 20 de marzo")
    
    # Ejemplo 7: Años especiales - Año bisiesto
    print_section("7. Propiedades de los años bisiestos")
    print(f"¿2028 es bisiesto? {SimpleDate.is_leap(2028)}")
    print(f"¿2025 es bisiesto? {SimpleDate.is_leap(2025)}")
    print(f"¿2000 es bisiesto? {SimpleDate.is_leap(2000)}")
    print(f"¿1900 es bisiesto? {SimpleDate.is_leap(1900)}")
    
    # Ejemplo 8: Ciclo completo de un año Zinkro
    print_section("8. Meses del año Zinkro 12026")
    print(f"{'Mes':<5} {'Gregoriano desde':<20} {'Gregoriano hasta':<20}")
    print("-" * 45)
    
    months_start = [
        (1, 2026, 3, 21),   # Mes 1: 21 de marzo
        (2, 2026, 4, 18),   # Mes 2: 18 de abril
        (3, 2026, 5, 16),   # Mes 3: 16 de mayo
        (4, 2026, 6, 13),   # Mes 4: 13 de junio
        (5, 2026, 7, 11),   # Mes 5: 11 de julio
        (6, 2026, 8, 8),    # Mes 6: 8 de agosto
        (7, 2026, 9, 5),    # Mes 7: 5 de septiembre
        (8, 2026, 10, 3),   # Mes 8: 3 de octubre
        (9, 2026, 10, 31),  # Mes 9: 31 de octubre
        (10, 2026, 11, 28), # Mes 10: 28 de noviembre
        (11, 2026, 12, 26), # Mes 11: 26 de diciembre
        (12, 2027, 1, 23),  # Mes 12: 23 de enero
        (13, 2027, 2, 20),  # Mes 13: 20 de febrero
    ]
    
    for month, year, month_g, day_g in months_start:
        print(f"{month:<5} {year}-{month_g:02d}-{day_g:02d}         hasta 28 días después")
    
    print_section("CONCLUSIÓN")
    print(f"✓ El calendario Zinkro transforma el tiempo gregoriano")
    print(f"✓ Cada año inicia el 21 de marzo (después del Día Zero del 20)")
    print(f"✓ 13 meses de 28 días cada uno = 364 días + 1 Día Zero = 365 días")
    print(f"✓ En años bisiestos: 364 + 2 días especiales = 366 días")
    print(f"✓ Sincronizado con el equinoccio de primavera")

if __name__ == "__main__":
    main()
