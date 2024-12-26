"""
Given two integers a and b, which can be
positive or negative, find the sum of all
the integers between and including themand
return it. If the two numbers are equal
return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number,
not the explanation about how you get that
number.
"""

def get_sum(a:int, b:int):
    """
    This function return the sum of all 
    the integers between and including
    themand return it
    """
    if a == b:
        return a

    min_num = a if a < b else b
    max_num = a if a > b else b
    total_value = 0 + min_num

    while min_num != max_num:
        min_num += 1
        total_value += min_num

    return total_value