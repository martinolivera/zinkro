import unittest
import datetime
from zinkro import ZinkroCalendar

class TestZinkroCalendar(unittest.TestCase):
    def setUp(self):
        self.start_date = datetime.date(2025, 1, 1)
        self.cal = ZinkroCalendar(start_date=self.start_date)

    def test_gregorian_to_zinkro_regular_day(self):
        # 2025-01-01 debe ser año 0, mes 1, día 1
        result = self.cal.gregorian_to_zinkro(datetime.date(2025, 1, 1))
        self.assertEqual(result, (0, 1, 1, False))

    def test_gregorian_to_zinkro_dia_zero(self):
        # Día Zero: 2025-12-31
        result = self.cal.gregorian_to_zinkro(datetime.date(2025, 12, 31))
        self.assertEqual(result, (0, None, None, True))

    def test_zinkro_to_gregorian_regular_day(self):
        # año 0, mes 1, día 1 debe ser 2025-01-01
        result = self.cal.zinkro_to_gregorian(0, 1, 1)
        self.assertEqual(result, datetime.date(2025, 1, 1))

    def test_zinkro_to_gregorian_dia_zero(self):
        # año 0, Día Zero debe ser 2025-12-31
        result = self.cal.zinkro_to_gregorian(0, None, None)
        self.assertEqual(result, datetime.date(2025, 12, 31))

    def test_conversion_inverse(self):
        # Prueba inversa: gregoriana -> zinkro -> gregoriana
        date = datetime.date(2026, 2, 15)
        zinkro = self.cal.gregorian_to_zinkro(date)
        back = self.cal.zinkro_to_gregorian(*zinkro[:3])
        self.assertEqual(date, back)

if __name__ == "__main__":
    unittest.main()
