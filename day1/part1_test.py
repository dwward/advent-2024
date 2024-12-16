import tempfile
import unittest, io
from distances import Distances

class MyTestCase(unittest.TestCase):

    @staticmethod
    def create_temp_file(contents):
        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        temp_file.write(contents)
        temp_file.flush()
        return temp_file

    def test_calculate_oneliner(self):
        f = self.create_temp_file("4   3")
        try:
            distances = Distances()
            distances.parse_file(f.name)
            result = distances.calculate()
            self.assertEqual(result, 1)
        finally:
            f.close()  # Close the file

    def test_calculate_multiline(self):
        f = self.create_temp_file("7   5\n5   5\n5   7\n")
        try:
            distances = Distances()
            distances.parse_file(f.name)
            result = distances.calculate()
            self.assertEqual(result, 0)
        finally:
            f.close()  # Close the file

    def test_calculate_parse_advent_file(self):
        distances = Distances()
        distances.parse_file("part1.input")
        result = distances.calculate()
        self.assertEqual(result, 1388114)



if __name__ == '__main__':
    unittest.main()
