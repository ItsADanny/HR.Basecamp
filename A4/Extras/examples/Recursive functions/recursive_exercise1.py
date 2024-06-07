"""
Exercise 1:
------------------------------------------------------------------------------------------------------------------------
Write a recursive function to find the sum of the digits of a number.

HINT:
Use n//10 and n%10.
------------------------------------------------------------------------------------------------------------------------
"""

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)