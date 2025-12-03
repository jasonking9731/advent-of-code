import unittest

from part2 import calc_new_dial_position, calc_number_of_clicks_onto_zero

class TestCalcNewDialPosition(unittest.TestCase):
    # if the dial were pointing at 11, a rotation of R8 would cause the dial to
    # point at 19.
    def test_simple_right_rotation(self):
        self.assertEqual(calc_new_dial_position(11,'R', 8), 19)

    # After that, a rotation of L19 would cause it to point at 0.
    def test_simple_left_rotation(self):
        self.assertEqual(calc_new_dial_position(19, 'L', 19), 0)

    # Because the dial is a circle, turning the dial left from 0 one click makes
    # it point at 99.
    def test_one_left_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(0, 'L', 1), 99)

    #  Similarly, turning the dial right from 99 one click makes it point at 0.
    def test_one_right_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(99, 'R', 1), 0)

    # So, if the dial were pointing at 5, a rotation of L10 would cause it to
    # point at 95.
    def test_short_left_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(5, 'L', 10), 95)

    # After that, a rotation of R5 could cause it to point at 0.
    def test_short_right_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(95, 'R', 5), 0)

    def test_long_right_rotation_that_passes_zero_mulitple_times(self):
        self.assertEqual(calc_new_dial_position(50, 'R', 550), 0)

    def test_long_left_rotation_that_passes_zero_mulitple_times(self):
        self.assertEqual(calc_new_dial_position(50, 'L', 550), 0)

class TestCalcNumberOfClickOntoZero(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual(calc_number_of_clicks_onto_zero(50, 'L', 68), 1)
        self.assertEqual(calc_number_of_clicks_onto_zero(82, 'L', 30), 0)
        self.assertEqual(calc_number_of_clicks_onto_zero(52, 'R', 48), 1)
        self.assertEqual(calc_number_of_clicks_onto_zero(0, 'L', 5), 0)
        self.assertEqual(calc_number_of_clicks_onto_zero(95, 'R', 60), 1)
        self.assertEqual(calc_number_of_clicks_onto_zero(55, 'L', 55), 1)
        self.assertEqual(calc_number_of_clicks_onto_zero(0, 'L', 1), 0)
        self.assertEqual(calc_number_of_clicks_onto_zero(99, 'L', 99), 1)
        self.assertEqual(calc_number_of_clicks_onto_zero(0, 'R', 14), 0)
        self.assertEqual(calc_number_of_clicks_onto_zero(14, 'L', 82), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)