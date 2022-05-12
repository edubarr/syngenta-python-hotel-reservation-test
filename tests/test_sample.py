from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    # test samples
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))
    

    #Implemented tests:

    # Regular, all week days
    def test4(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed), 19Mar2009(thur)"))

    # Regular, more weekdays than weekend days
    def test5(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    # Regular, less weekday than weekend day
    def test6(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    # Regular, all weekend days
    def test7(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 21Mar2009(sat), 22Mar2009(sun)"))

    # Rewards, all week days
    def test8(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    # Rewards, more weekdays than weekend days
    def test9(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    # Rewards, less weekday than weekend day
    def test10(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    # Rewards, all weekend days
    def test11(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 21Mar2009(sat), 22Mar2009(sun)"))