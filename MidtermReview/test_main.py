from multiprocessing.managers import Value
from unittest import TestCase
from main import Burger

class TestBurger(TestCase):
    def test_get_total_cost(self):
        # arrange
        expected_total_cost = 1.05
        burger = Burger(1, 100, 1)
        burger.set_actual_weight_in_grams(105)
        burger.add_topping("nothing")

        # act
        actual_cost = burger.get_total_cost()

        # assert
        self.assertEqual(expected_total_cost, actual_cost)

    def test_set_actual_weight_in_grams_raises_exception(self):

        burger = Burger(1,1,1)
        self.assertRaises(ValueError, burger.set_actual_weight_in_grams, 10000)

    def test_set_actual_weight_in_grams(self):
        expected_weight_in_grams = 500
        burger = Burger(1,1,1)

        burger.set_actual_weight_in_grams(expected_weight_in_grams)
        actual_weight_in_grams = burger.get_weight_in_grams()

        self.assertEqual(expected_weight_in_grams, actual_weight_in_grams)