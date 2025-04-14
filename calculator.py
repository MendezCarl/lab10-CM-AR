# https://github.com/MendezCarl/lab10-CW-AR.git
# Partner 1: Carlos Mendez
# Partner 2: Ahsan Rahul
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
import math

def square_root(a):
    try:
        if a<0:
            raise ValueError
        else:
            return math.sqrt(a)
    except ValueError:
        print("Value must be greater than 0")

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
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a == 0:
        raise ValueError
    log(b, a)

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
        return logarithm(b,a)

def exponent(a,b):
    return a^b
