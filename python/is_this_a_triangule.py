"""
Implement a function that accepts 3 integer values
a, b, c. The function should return true if a triangle
can be built with the sides of given length and false
in any other case.

(In this case, all triangles must have surface greater
than 0 to be accepted).

Examples:

Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false 
"""

def is_triangle(a, b, c):
    sides = [a,b,c]
    sides.sort() # 1,2,2
    i = 2
    while i != -1:
        triangular_inequality = sides[i-2] + sides[i-1] > sides[i]
        # [0] + [1] > [2] | 1 + 2 > 2
        # [-1] + [0] > [1] 2 + 1 > 2
        # [-2] + [-1] > [0] 2 + 2 > 1
        if not triangular_inequality:
            return False
        i  -= 1
    return True