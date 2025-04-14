# https://github.com/MendezCarl/lab10-CW-AR.git
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a+b

def subract(a, b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero")
    else:
        return b/a

def logarithm(a,b):
    if a<=1:
        raise ValueError("Value must be greater than 1")
    else:
        return logarithm(b,a)

def exponent(a,b):
    return a^b