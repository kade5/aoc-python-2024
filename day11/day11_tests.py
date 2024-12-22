import unittest
import day11


class MyTestCase(unittest.TestCase):
    def test_stone_list(self):
        input_str = "0 12 14"
        expected = [0, 12, 14]
        actual = day11.build_initial_stone_list(input_str)
        self.assertListEqual(expected, actual)

        input_str2 = "0"
        expected2 = [0]
        actual2 = day11.build_initial_stone_list(input_str2)
        self.assertListEqual(expected2, actual2)

    def test_stone_0(self):
        stone_list = [0]
        expected = [1]
        actual = day11.blink(stone_list)
        self.assertListEqual(expected, actual)

    def test_stone_even_len(self):
        stone_list = [123456]
        expected = [123, 456]
        actual = day11.blink(stone_list)
        self.assertListEqual(expected, actual)

    def test_stone_none(self):
        stone_list = [113]
        expected = [228712]
        actual = day11.blink(stone_list)
        self.assertListEqual(expected, actual)

    def test_all(self):
        stone_list = [253, 0, 2024, 14168]
        expected = [512072, 1, 20, 24, 28676032]
        actual = day11.blink(stone_list)
        self.assertListEqual(expected, actual)

    def test_part1(self):
        self.assertEqual(55312, day11.part_1("test.txt"))

    def test_blink2(self):
        initial_arr = [125, 17]
        actual = 0
        for num in initial_arr:
            actual += day11.blink2(num, 25)
        self.assertEqual(55312, actual)

if __name__ == '__main__':
    unittest.main()
