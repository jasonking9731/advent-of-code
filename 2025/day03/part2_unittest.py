import unittest

from part2 import find_repeating_pattern_in_numbers_in_range, total_invalid_ids_in_range, grand_total_invalid_ids_from_range_list

class TestFindRepeatedPatternsInNumberRange(unittest.TestCase):
    def test_data(self):
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(11,22), [11, 22])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(95,115), [99, 111])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(998,1012), [999, 1010])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(1188511880,1188511890), [1188511885])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(222220,222224), [222222])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(1698522,1698528), [])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(446443,446449), [446446])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(38593856,38593862), [38593859])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(565653,565659), [565656])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(824824821,824824827), [824824824])
        self.assertEqual(find_repeating_pattern_in_numbers_in_range(2121212118,2121212124), [2121212121])

class TestTotalInvalidIdsInRange(unittest.TestCase):
    def test_data(self):
        self.assertEqual(total_invalid_ids_in_range("11-22"), 33)
        self.assertEqual(total_invalid_ids_in_range("95-115"), 210)
        self.assertEqual(total_invalid_ids_in_range("998-1012"), 2009)
        self.assertEqual(total_invalid_ids_in_range("1188511880-1188511890"), 1188511885)
        self.assertEqual(total_invalid_ids_in_range("222220-222224"), 222222)
        self.assertEqual(total_invalid_ids_in_range("1698522-1698528"), 0)
        self.assertEqual(total_invalid_ids_in_range("446443-446449"), 446446)
        self.assertEqual(total_invalid_ids_in_range("38593856-38593862"), 38593859)
        self.assertEqual(total_invalid_ids_in_range("565653-565659"), 565656)
        self.assertEqual(total_invalid_ids_in_range("824824821-824824827"), 824824824)
        self.assertEqual(total_invalid_ids_in_range("2121212118-2121212124"), 2121212121)

class TestGrandTotalInvalidIdsFromRangeList(unittest.TestCase):
    def test_data(self):
        input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(',')
        self.assertEqual(grand_total_invalid_ids_from_range_list(input), 4174379265)

if __name__ == "__main__":
    unittest.main(verbosity=2)