import unittest

from part1 import count_adjacent_grid_squares, count_rolls_surrounded_by_fewer_than_four_rolls_in_grid

class TestCountRollsSurroundedByFewerThanFourRolls(unittest.TestCase):
    def test_count_adjacent_grid_squares(self):
        self.assertEqual(count_adjacent_grid_squares(0,0,["@..", ".@.", "..."]), 1)
        self.assertEqual(count_adjacent_grid_squares(0,0,["@@.", ".@.", "..."]), 2)
        self.assertEqual(count_adjacent_grid_squares(1,1,["@@.", ".@.", ".@."]), 3)

    def test_simple_grids(self):
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(["...", ".@.", "..."]), 1)
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(["@..", ".@.", "..."]), 2)
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(["@..", ".@.", ".@."]), 3)
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(["@..", ".@.", ".@@"]), 4)
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(["@@.", ".@.", ".@@"]), 4)
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(["@@@", ".@.", "@@@"]), 6)
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(["@@@", "@@@", "@@@"]), 4)

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
        self.assertEqual(count_rolls_surrounded_by_fewer_than_four_rolls_in_grid(test_input), 13)


if __name__ == "__main__":
    unittest.main(verbosity=2)