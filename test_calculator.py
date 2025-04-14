# https://github.com/MendezCarl/lab10-CW-AR.git
# Partner 1: Carlos Mendez
# Partner 2: Ahsan Rahul

import unittest
from multiprocessing.managers import Value

from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, -100), 0)
        self.assertNotEqual(add(9, 10), 21)

    def test_subtract(self): # 3 assertions
    #     fill in code
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(1, -1), 2)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(1, multiply(-1,-1))
        self.assertEqual(-1, multiply(1,-1))
        self.assertEqual(1,multiply(1,1))

    def test_divide(self):# 3 assertions
        self.assertEqual(div(2,8), 4)
        self.assertEqual(div(-2,8), -4)
        self.assertEqual(div(-2,-8), 4)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ValueError) as context:
            div(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    #     fill in code


    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(log(4, 16), 2)
        self.assertEqual(log(2, 4), 2)
        self.assertEqual(log(3, 9), 2)


    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        with self.assertRaises(ValueError) as e:
            log(0, 7)
        assert e in str(e)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        self.assertRaises(ValueError, logarithm(0,5))

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5,hypotenuse(3,4))
        self.assertEqual(5, hypotenuse(-3,4))
        self.assertEqual(5,hypotenuse(-3,-4))

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # Test basic function
        self.assertRaises(ValueError,(0))
        self.assertRaises(ValueError,square_root(-4))
        self.assertEqual(square_root(4), 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()