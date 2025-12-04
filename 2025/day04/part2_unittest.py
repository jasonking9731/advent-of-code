import unittest

from part2 import count_adjacent_grid_squares, count_rolls_removed_until_remaining_are_surrounded_by_fewer_than_four_rolls_in_grid

class TestCountRollsSurroundedByFewerThanFourRolls(unittest.TestCase):
    def test_input(self):
        test_input = ["..@@.@@@@."]
        test_input.append("@@@.@.@.@@")
        test_input.append("@@@@@.@.@@")
        test_input.append("@.@@@@..@.")
        test_input.append("@@.@@@@.@@")
        test_input.append(".@@@@@@@.@")
        test_input.append(".@.@.@.@@@")
        test_input.append("@.@@@.@@@@")
        test_input.append(".@@@@@@@@.")
        test_input.append("@.@.@@@.@.")
        self.assertEqual(count_rolls_removed_until_remaining_are_surrounded_by_fewer_than_four_rolls_in_grid(test_input), 43)


if __name__ == "__main__":
    unittest.main(verbosity=2)