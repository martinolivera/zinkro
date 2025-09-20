import unittest
from zinkro import SimpleDate, ZinkroCalendar

class TestZinkroLeap(unittest.TestCase):
    def setUp(self):
        self.cal = ZinkroCalendar(start_date=SimpleDate.from_string("-10000-03-21"))

    def test_normal_year_march_1(self):
        # 2025 is not leap
        date = SimpleDate(2025, 3, 1)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12025, 13, 9))
        self.assertFalse(extra)

    def test_leap_year_feb_29(self):
        # 2028 is leap
        date = SimpleDate(2028, 2, 29)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12028, 13, 9))
        self.assertFalse(extra)

    def test_leap_year_march_1(self):
        date = SimpleDate(2028, 3, 1)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12028, 13, 10))
        self.assertFalse(extra)

    def test_leap_year_march_19(self):
        date = SimpleDate(2028, 3, 19)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12028, 13, 28))
        self.assertFalse(extra)

    def test_leap_year_march_20(self):
        date = SimpleDate(2028, 3, 20)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day, extra), (12028, None, None, 'dia366'))

    def test_leap_year_march_21(self):
        date = SimpleDate(2028, 3, 21)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day, extra), (0, None, None, True))

    def test_normal_year_march_19(self):
        date = SimpleDate(2025, 3, 19)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12025, 13, 27))
        self.assertFalse(extra)

    def test_normal_year_march_20(self):
        date = SimpleDate(2025, 3, 20)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day), (12025, 13, 28))
        self.assertFalse(extra)

    def test_normal_year_march_21(self):
        date = SimpleDate(2025, 3, 21)
        year, month, day, extra = self.cal.gregorian_to_zinkro(date)
        self.assertEqual((year, month, day, extra), (0, None, None, True))

if __name__ == "__main__":
    unittest.main()
