from unittest import TestCase
from captain import Captain
from unit import Unit

class TestCaptain(TestCase):
    def test_attack(self):
        # arrange
        unit_to_rally = Unit(5, 10, 0, 0, "us")
        attacking_unit = Unit(5, 10, 1, 1, "them")
        attacking_unit.attack(unit_to_rally)
        captain = Captain(1, 0, "us")
        expected_hit_points = 10

        # act
        captain.attack(unit_to_rally)
        actual_hit_points = unit_to_rally.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)

    def test_attack_not_in_range(self):
        # arrange
        unit_to_rally = Unit(5, 10, 0, 0, "us")
        attacking_unit = Unit(5, 10, 1, 1, "them")
        attacking_unit.attack(unit_to_rally)
        captain = Captain(2, 0, "us")
        expected_hit_points = 5

        # act
        captain.attack(unit_to_rally)
        actual_hit_points = unit_to_rally.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points, actual_hit_points)
