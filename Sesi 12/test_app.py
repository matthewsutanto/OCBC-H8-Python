#Testcase and nose 2
import unittest
import connex_app
# pip install nose2
# python -m nose2
class testSum(unittest.TestCase):
    def setUp(self):
        connex_app.app.testing = True
        self.app = connex_app.app.test_client()
    def test_sum(self):
        self.assertEqual (sum([1,2,3]), 6 , "Should be 6")
    def test_sum_tuple(self):
        self.assertEqual(sum([1,2,2]),6, "Should be 6") 
    
if __name__ == "__main__":
    unittest.main()
    # print("Everything passed")

# pytest
# def test_sum():
#     assert sum([1,2,3]) == 6 , "Should be 6"
# def test_sum_tuple():
#     assert sum([1,2,2]) == 6, "Should be 6"
