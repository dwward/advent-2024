import tempfile
import unittest, io
from order import Order


class OrderTests(unittest.TestCase):

    @staticmethod
    def create_temp_file(contents):
        temp_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        temp_file.write(contents)
        temp_file.flush()
        return temp_file

    def test_add_middle_column_case_1(self):
        order = Order()
        f = self.create_temp_file("1|2\n" +
                                  "2|3\n" +
                                  "\n" +
                                  "4,3,2\n" +
                                  "2,3,4\n" +
                                  "3,1,2\n")
        order.parse_file(f.name)
        result = order.add_middle_column()
        self.assertEqual(3, result[0])
        self.assertEqual(4, result[1])

    def test_add_middle_column_advent_example(self):
        order = Order()
        order.parse_file("example.input")
        result = order.add_middle_column()
        self.assertEqual(143, result[0])

    def test_add_middle_column_advent_input(self):
        order = Order()
        order.parse_file("order.input")
        result = order.add_middle_column()
        self.assertEqual(5991, result[0])

    def test_sort_example_input(self):
        order = Order()
        order.parse_file("example.input")

        # plist = order._sort([75, 97, 47, 61, 53])
        # self.assertEqual([97, 75, 47, 61, 53], plist)

        plist = order._sort([61, 13, 29], )
        self.assertEqual([61, 29, 13], plist)

        # plist = order._sort([97, 13, 75, 29, 47])
        # self.assertEqual([97, 75, 47, 29, 13], plist)
