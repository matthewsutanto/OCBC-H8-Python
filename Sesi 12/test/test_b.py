import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(12-5,7)

if __name__ == '__main__':
    unittest.main()