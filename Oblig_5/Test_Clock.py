from Clock import Clock
import unittest

class Test_Clock(unittest.TestCase):
    
    def set_up(self):
        self.__clock = Clock()
    
    def test_inc_sec_from_default_values(self):
        self.__clock.inc_sec()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:00:01")
    
    def test_inc_min_from_default_values(self):
        self.__clock.inc_min()
        self.assertEqual(self.__clock.clock_as_string(), "00:00:0000:00:01:00")

    def test_inc_sec_from_midnight_jan(self):
        self.__clock = Clock(30, 1, 2021, 23, 59, 59)
        self.__clock.inc_sec()
        self.assertEqual(self.__clock.clock_as_string(), "01:02:2021:00:00:00")
        