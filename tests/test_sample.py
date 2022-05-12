from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    # Regular, 3 weekdays OK
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    # Regular, 2 weekdays and 1 weekend day
    def test2(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    # Regular, 1 weekday and 2 weekend day
    def test3(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    # Rewards, 3 weekdays
    def test4(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    # Rewards, 2 weekdays and 1 weekend day
    def test5(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    # Rewards, 1 weekday and 2 weekend day
    def test6(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))