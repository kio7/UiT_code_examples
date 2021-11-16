from Clock import Clock
import unittest

class Test_Clock(unittest.TestCase):
    
    def setUp(self):
        self.__clock = Clock()
    
    # From Default values
    def test_inc_sec_from_default_values(self):
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:00:01")
    
    def test_inc_min_from_default_values(self):
        self.__clock.inc_minute()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:01:00")

    def test_inc_hour_from_default_values(self):
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:01:00:00")
    
    def test_inc_day_from_default_values(self):
        self.__clock.inc_day()
        self.assertEqual(self.__clock.clock_as_string(), "01:00:0000:00:00:00")
    
    def test_inc_month_from_default_values(self):
        self.__clock.inc_month()
        self.assertEqual(self.__clock.clock_as_string(), "00:01:0000:00:00:00")
    
    def test_inc_year_from_default_values(self):
        self.__clock.inc_year()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0001:00:00:00")
    
    # Border and "sunshine" scenarios
    def test_inc_sec_from_midnight_jan(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:00:00:00")
    
    def test_inc_min_from_midnight_jan(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.inc_minute()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:00:00:59")
    
    def test_inc_hour_from_midnight_jan(self):
        self.__clock = Clock(31, 1, 2021, 23, 59, 59)
        self.__clock.inc_hour()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:00:59:59")
    
    def test_inc_day_from_new_years(self):
        self.__clock = Clock(31, 12, 2021, 23, 59, 59)
        self.__clock.inc_day()
        self.assertEqual(self.__clock.clock_as_string(), "01:01:2022:23:59:59")
    
    def test_inc_month_from_new_years(self):
        self.__clock = Clock(31, 12, 2021, 23, 59, 59)
        self.__clock.inc_month()
        self.assertEqual(self.__clock.clock_as_string(), "31:01:2022:23:59:59")
    
    def test_inc_year_for_fun(self):
        self.__clock = Clock(5, 12, 2500, 12, 45, 00)
        self.__clock.inc_year()
        self.assertEqual(self.__clock.clock_as_string(), "05:12:2501:12:45:00")
    
    # Leap Year Tests
    def test_leap_year(self):
        self.__clock = Clock(28, 2, 2000, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "29:02:2000:00:00:00")

    def test_not_leap_year(self):
        self.__clock = Clock(28, 2, 2001, 23, 59, 59)
        self.__clock.inc_second()
        self.assertEqual(self.__clock.clock_as_string(), "01:03:2001:00:00:00")
    
if __name__ == "__main__":
    unittest.main()
