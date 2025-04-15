# https://github.com/MendezCarl/lab10-CW-AR.git
# Partner 1: Carlos Mendez
# Partner 2: Ahsan Rahul
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError("Number must not be negative")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return b / a

def log(a, b):
    if a <= 1:
        raise ValueError("Base cannot be zero")
    return math.log(b, a)

def exp(a, b):
    return a ** b


def sub(a, b):
    return a-b

def multiply(a,b):
    return a*b


def logarithm(a,b):
    if a<=1:
        raise ValueError("Value must be greater than 1")
    else:
        return log(b,a)

def exponent(a,b):
    return a^b
