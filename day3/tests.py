import tempfile
import unittest, io
from mul import Mul


class MulTests(unittest.TestCase):

    @staticmethod
    def create_temp_file(contents):
        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        temp_file.write(contents)
        temp_file.flush()
        return temp_file

    def test_match_mul_groups(self):
        mul = Mul()
        results = mul.parse_muls("abcdmul(44,46)efgh")
        self.assertEqual(["mul(44,46)"], results)

    def test_match_mul_advent_example(self):
        mul = Mul()
        results = mul.parse_muls("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)):")
        self.assertEqual(["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"], results)

    def test_match_and_multiply(self):
        mul = Mul()
        results = mul.parse_mul("mul(3,7)")
        self.assertEqual([3, 7], results)

    def test_load_file_and_calculate(self):
        mul = Mul()
        f = self.create_temp_file("abcdmul(2,4)\n" +
                                  "1 2 7 8 mul(-2,-2)")
        mul.parse_file(f.name)
        result = mul.process_muls()
        self.assertEqual(12, result)

    def test_load_advent_file_and_calculate(self):
        mul = Mul()
        mul.parse_file("mul.input")
        result = mul.process_muls()
        self.assertEqual(196826776, result)

    def test_load_file_and_calculate_conditional(self):
        mul = Mul()
        f = self.create_temp_file("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
        mul.parse_file(f.name)
        result = mul.process_muls(conditional=True)
        self.assertEqual(48, result)

    def test_load_advent_file_and_calculate_conditional(self):
        mul = Mul()
        mul.parse_file("mul.input")
        result = mul.process_muls(conditional=True)
        self.assertEqual(106780429, result)

    def test_load_file_and_calculate_conditional_edge_case_wrap_lines(self):
        mul = Mul()
        f = self.create_temp_file("do()mul(2,2)don't()\n" +
                                  "mul(3,3)do()mul(4,4)\n" +
                                  "mul(5,5)don't()mul(6,6)")
        mul.parse_file(f.name)
        result = mul.process_muls(conditional=True)
        self.assertEqual(45, result)
