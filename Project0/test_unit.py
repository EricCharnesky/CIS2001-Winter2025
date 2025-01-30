from unittest import TestCase
from unit import Unit

class TestUnit(TestCase):
    def test_init(self):

        # arrange
        expected_attack_power = 5
        expected_hit_points = 6
        expected_range = 7
        expected_x_position = 8
        expected_y_position = 9
        expected_team = "team"
        expected_is_alive = True

        # act
        unit = Unit(expected_attack_power, expected_hit_points, expected_x_position, expected_y_position, expected_team, expected_range)
        actual_attack_power = unit.get_attack_power()
        actual_hit_points = unit.get_hit_points()
        actual_range = unit.get_range()
        actual_x_position = unit.get_x_position()
        actual_y_position = unit.get_y_position()
        actual_team = unit.get_team()
        actual_is_alive = unit.is_alive()

        # assert
        self.assertEqual(expected_attack_power, actual_attack_power)
        self.assertEqual(expected_hit_points, actual_hit_points)
        self.assertEqual(expected_range, actual_range)
        self.assertEqual(expected_x_position, actual_x_position)
        self.assertEqual(expected_y_position, actual_y_position)
        self.assertEqual(expected_team, actual_team)
        self.assertEqual(expected_is_alive, actual_is_alive)


    def test_attack_successful(self):
        # arrange
        unit_to_attack = Unit(5, 10, 0, 0, "them")
        attacking_unit = Unit(5, 10, 1, 1, "us")
        expected_hit_points_after_attack = 5

        # act
        attacking_unit.attack(unit_to_attack)
        actual_hit_points = unit_to_attack.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points_after_attack, actual_hit_points)

    def test_attack_hit_points_dont_go_below_0(self):
        # arrange
        unit_to_attack = Unit(5, 10, 0, 0, "them")
        attacking_unit = Unit(50, 10, 1, 1, "us")
        expected_hit_points_after_attack = 0

        # act
        attacking_unit.attack(unit_to_attack)
        actual_hit_points = unit_to_attack.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points_after_attack, actual_hit_points)

    def test_attack_dont_attack_same_team(self):
        # arrange
        unit_to_attack = Unit(5, 10, 0, 0, "us")
        attacking_unit = Unit(5, 10, 1, 1, "us")
        expected_hit_points_after_attack = 10

        # act
        attacking_unit.attack(unit_to_attack)
        actual_hit_points = unit_to_attack.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points_after_attack, actual_hit_points)

    def test_attack_dont_attack_out_of_range(self):
        # arrange
        unit_to_attack = Unit(5, 10, 0, 0, "us")
        attacking_unit = Unit(5, 10, 5, 5, "us")
        expected_hit_points_after_attack = 10

        # act
        attacking_unit.attack(unit_to_attack)
        actual_hit_points = unit_to_attack.get_hit_points()

        # assert
        self.assertEqual(expected_hit_points_after_attack, actual_hit_points)
