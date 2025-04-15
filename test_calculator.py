# https://github.com/MendezCarl/lab10-CW-AR.git
# Partner 1: Carlos Mendez
# Partner 2: Ahsan Rahul

import unittest
import math
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
        try:
            self.assertRaises(ZeroDivisionError,div(0, 5))
        except:
            print("Zero divison error")

    #     fill in code


    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(log(4, 16),2)
        self.assertEqual(log(2, 4),2)
        self.assertEqual(log(3, 9),2)


    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
        try:
            while self.assertRaises(ValueError):
                log(0,5)
        except:
            print("Error")
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        try:
            while self.assertRaises(ValueError):
                logarithm(0, 5)
        except:
            print("Can't have base equal # <= 0")

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5,hypotenuse(3,4))
        self.assertEqual(5, hypotenuse(-3,4))
        self.assertEqual(5,hypotenuse(-3,-4))

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # Test basic function
        try:
            with self.assertRaises(ValueError):
                square_root(0)
                square_root(-4)
        except:
            print("value can't be less than 1")
        # self.assertRaises(ValueError,square_root(0))
        # self.assertRaises(ValueError,square_root(-4))
        # self.assertEqual(square_root(4), 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()