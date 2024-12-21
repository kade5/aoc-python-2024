import unittest
import utils


class MyTestCase(unittest.TestCase):
    def test_file_string(self):
        self.assertEqual(utils.read_file_into_string("test/input/test.txt"), "27 10647 103 9 0 5524 4594227 902936")



if __name__ == '__main__':
    unittest.main()
