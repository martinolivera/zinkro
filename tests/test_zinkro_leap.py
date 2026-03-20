import unittest
from zinkro import SimpleDate, ZinkroCalendar

class TestZinkroLeap(unittest.TestCase):
    def setUp(self):
        self.cal = ZinkroCalendar(start_date=SimpleDate.from_string("-10000-03-20"))

    def test_normal_year_march_1(self):
        # 2025 is not leap
        # 1 de marzo de 2025 pertenece al año anterior (2024)
        date = SimpleDate(2025, 3, 1)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12024, 13, 10))

    def test_leap_year_feb_29(self):
        # 2028 is leap
        # 29 de febrero de 2028 pertenece al año anterior (2027)
        date = SimpleDate(2028, 2, 29)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12027, 13, 10))

    def test_leap_year_march_1(self):
        # 1 de marzo de 2028 pertenece al año anterior (2027)
        date = SimpleDate(2028, 3, 1)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12027, 13, 11))

    def test_leap_year_march_19(self):
        # 18 de marzo de 2028 pertenece al año anterior (2027)
        date = SimpleDate(2028, 3, 18)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12027, 13, 28))

    def test_leap_year_march_19_special_day(self):
        # 19 de marzo de 2028: Día especial 366 (año bisiesto)
        # Pertenece al año anterior (2027) y es el día especial
        date = SimpleDate(2028, 3, 19)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12027, None, 366))

    def test_leap_year_march_20_day_zero(self):
        # 20 de marzo de 2028: Día Zero - ¡CAMBIA EL AÑO!
        date = SimpleDate(2028, 3, 20)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12028, None, 0))

    def test_leap_year_march_21(self):
        # 21 de marzo de 2028: Primer día del año 12028
        date = SimpleDate(2028, 3, 21)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12028, 1, 1))

    def test_normal_year_march_19(self):
        # 19 de marzo de 2025: Día anterior al Día Zero (año normal, sin bisiesto)
        # Pertenece al año anterior (2024)
        date = SimpleDate(2025, 3, 19)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12024, 13, 28))

    def test_normal_year_march_20_day_zero(self):
        # 20 de marzo de 2026: Día Zero (hoy en este momento)
        date = SimpleDate(2026, 3, 20)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12026, None, 0))

    def test_normal_year_march_20(self):
        # 20 de marzo de 2025: Día Zero del año 12025
        date = SimpleDate(2025, 3, 20)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12025, None, 0))

    def test_normal_year_march_21(self):
        date = SimpleDate(2025, 3, 21)
        year, month, day = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12025, 1, 1))

if __name__ == "__main__":
    unittest.main()
