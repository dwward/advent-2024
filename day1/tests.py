import tempfile
import unittest, io
from distances import Distances

class DistanceTest(unittest.TestCase):

    @staticmethod
    def create_temp_file(contents):
        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        temp_file.write(contents)
        temp_file.flush()
        return temp_file

    def test_distance_one_liner(self):
        f = self.create_temp_file("4   3")
        try:
            distances = Distances()
            distances.parse_file(f.name)
            result = distances.distance()
            self.assertEqual(1, result)
        finally:
            f.close()

    def test_distance_multi_liner(self):
        f = self.create_temp_file("7   5\n5   5\n5   7\n")
        try:
            distances = Distances()
            distances.parse_file(f.name)
            result = distances.distance()
            self.assertEqual(0, result)
        finally:
            f.close()

    def test_distance_parse_advent_file(self):
        distances = Distances()
        distances.parse_file("distances.input")
        result = distances.distance()
        self.assertEqual(1388114, result)

    def test_similarity_one_liner(self):
        f = self.create_temp_file("4   3")
        try:
            distances = Distances()
            distances.parse_file(f.name)
            result = distances.similarity()
            self.assertEqual(0, result)
        finally:
            f.close()

    def test_similarity_multi_liner(self):
        f = self.create_temp_file("7   5\n5   5\n5   7\n")
        try:
            distances = Distances()
            distances.parse_file(f.name)
            result = distances.similarity()
            self.assertEqual(27, result)
        finally:
            f.close()

    def test_similarity_parse_advent_file(self):
        distances = Distances()
        distances.parse_file("distances.input")
        result = distances.similarity()
        self.assertEqual(23529853, result)

if __name__ == '__main__':
    unittest.main()
