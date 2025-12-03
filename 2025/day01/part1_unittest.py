import unittest

from part1 import calc_new_dial_position, count_whenever_dial_lands_on_zero_during_sequence

class TestCalcNewDialPosition(unittest.TestCase):
    # if the dial were pointing at 11, a rotation of R8 would cause the dial to
    # point at 19.
    def test_simple_right_rotation(self):
        self.assertEqual(calc_new_dial_position(11,"R8"), 19)

    # After that, a rotation of L19 would cause it to point at 0.
    def test_simple_left_rotation(self):
        self.assertEqual(calc_new_dial_position(19,"L19"), 0)

    # Because the dial is a circle, turning the dial left from 0 one click makes
    # it point at 99.
    def test_one_left_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(0,"L1"), 99)

    #  Similarly, turning the dial right from 99 one click makes it point at 0.
    def test_one_right_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(99,"R1"), 0)

    # So, if the dial were pointing at 5, a rotation of L10 would cause it to
    # point at 95.
    def test_short_left_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(5,"L10"), 95)

    # After that, a rotation of R5 could cause it to point at 0.
    def test_short_right_rotation_that_passes_zero(self):
        self.assertEqual(calc_new_dial_position(95,"R5"), 0)

class TestCountWheneverDialLandsOnZeroDuringSequence(unittest.TestCase):
    def test_input(self):
        rotation_sequence = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        self.assertEqual(count_whenever_dial_lands_on_zero_during_sequence(50, rotation_sequence), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)