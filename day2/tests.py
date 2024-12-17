import tempfile
import unittest, io
from levels import Levels


class LevelsTest(unittest.TestCase):

    @staticmethod
    def create_temp_file(contents):
        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        temp_file.write(contents)
        temp_file.flush()
        return temp_file

    def test_is_safe_true_decreases_1_or_2(self):
        levels = Levels()
        result = levels._is_safe([7, 6, 4, 2, 1])
        self.assertEqual(True, result)

    # 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    def test_is_safe_false_increase_of_5(self):
        levels = Levels()
        result = levels._is_safe([1, 2, 7, 8, 9])
        self.assertEqual(False, result)

    # 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    def test_is_safe_false_decrease_of_4(self):
        levels = Levels()
        result = levels._is_safe([9, 7, 6, 2, 1])
        self.assertEqual(False, result)

    # 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    def test_is_safe_false_not_strictly_monotonic_1_3_3_2(self):
        levels = Levels()
        result = levels._is_safe([1, 3, 2, 4, 5])
        self.assertEqual(False, result)

    # 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    def test_is_safe_false_not_strictly_monotonic_4_4(self):
        levels = Levels()
        result = levels._is_safe([8, 6, 4, 4, 1])
        self.assertEqual(False, result)

    # 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
    def test_is_safe_true_monotonic_1_2_3(self):
        levels = Levels()
        result = levels._is_safe([1, 3, 6, 7, 9])
        self.assertEqual(True, result)

    def test_count_safe_levels(self):
        f = self.create_temp_file("1 2 7 8 9\n1 3 5 7 9")
        try:
            levels = Levels()
            levels.parse_file(f.name)
            result = levels.count_safe()
            self.assertEqual(1, result)
        finally:
            f.close()

    def test_count_safe_level_advent_example(self):
        f = self.create_temp_file("7 6 4 2 1\n" +
                                  "1 2 7 8 9\n" +
                                  "9 7 6 2 1\n" +
                                  "1 3 2 4 5\n" +
                                  "8 6 4 4 1\n" +
                                  "1 3 6 7 9")
        try:
            levels = Levels()
            levels.parse_file(f.name)
            result = levels.count_safe()
            self.assertEqual(2, result)
        finally:
            f.close()

    def test_advent_input_file(self):
        levels = Levels()
        levels.parse_file("levels.input")
        result = levels.count_safe()
        self.assertEqual(516, result)

    def test_dampen_true_decreases_1_or_2(self):
        levels = Levels()
        result = levels._is_safe([7, 6, 4, 2, 1], True)
        self.assertEqual(True, result)

    # 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    def test_dampen_false_increase_of_5(self):
        levels = Levels()
        result = levels._is_safe([1, 2, 7, 8, 9], True)
        self.assertEqual(False, result)

    # 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    def test_dampen_false_decrease_of_4(self):
        levels = Levels()
        result = levels._is_safe([9, 7, 6, 2, 1], True)
        self.assertEqual(False, result)

    # 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    def test_dampen_true_not_strictly_monotonic_1_3_3_2(self):
        levels = Levels()
        result = levels._is_safe([1, 3, 2, 4, 5], True)
        self.assertEqual(True, result)

    # 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    def test_dampen_true_not_strictly_monotonic_4_4(self):
        levels = Levels()
        result = levels._is_safe([8, 6, 4, 4, 1], True)
        self.assertEqual(True, result)

    # 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
    def test_dampen_true_monotonic_1_2_3(self):
        levels = Levels()
        result = levels._is_safe([1, 3, 6, 7, 9], True)
        self.assertEqual(True, result)

    def test_count_safe_level_dampened_advent_example(self):
        f = self.create_temp_file("7 6 4 2 1\n" +
                                  "1 2 7 8 9\n" +
                                  "9 7 6 2 1\n" +
                                  "1 3 2 4 5\n" +
                                  "8 6 4 4 1\n" +
                                  "1 3 6 7 9")
        try:
            levels = Levels()
            levels.parse_file(f.name)
            result = levels.count_safe(dampened=True)
            self.assertEqual(4, result)
        finally:
            f.close()

    def test_dampen_true_edge_case_error_in_first_index_increasing(self):
        levels = Levels()
        result = levels._is_safe([5, 1, 2, 3, 4], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_error_in_first_index_decreasing(self):
        levels = Levels()
        result = levels._is_safe([2, 5, 4, 3, 2], True)
        self.assertEqual(True, result)

    def test_advent_input_file_dampened(self):
        levels = Levels()
        levels.parse_file("levels.input")
        result = levels.count_safe(dampened=True)
        self.assertEqual(561, result)

    def test_dampen_true_edge_case_error_pyramid_1(self):
        levels = Levels()
        result = levels._is_safe([1, 2, 1], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_error_pyramid_2(self):
        levels = Levels()
        result = levels._is_safe([2, 1, 2], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_error_valley_1(self):
        levels = Levels()
        result = levels._is_safe([5, 4, 5, 6], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_error_plateau_1(self):
        levels = Levels()
        result = levels._is_safe([1, 1, 4], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_error_plateau_2(self):
        levels = Levels()
        result = levels._is_safe([4, 4, 1], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_error_descends_at_end(self):
        levels = Levels()
        result = levels._is_safe([16, 19, 21, 24, 21], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_1(self):
        levels = Levels()
        result = levels._is_safe([4, 3, 2, 1, 2], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_2(self):
        levels = Levels()
        result = levels._is_safe([1, 2, 3, 4, 3], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_3(self):
        levels = Levels()
        result = levels._is_safe([1, 0, 1, 2, 3], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_4(self):
        levels = Levels()
        result = levels._is_safe([5, 6, 5, 4, 3], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_5(self):
        levels = Levels()
        result = levels._is_safe([1, 0, 0], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_6(self):
        levels = Levels()
        result = levels._is_safe([0, 1, 1], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_7(self):
        levels = Levels()
        result = levels._is_safe([0, 0, 1], True)
        self.assertEqual(True, result)

    def test_dampen_true_edge_case_8(self):
        levels = Levels()
        result = levels._is_safe([1, 1, 0], True)
        self.assertEqual(True, result)