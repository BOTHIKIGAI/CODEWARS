"""
Create a function taking a positive
integer between 1 and 3999 (both included)
as its parameter and returning a string
containing the Roman Numeral representation
of that integer.

Modern Roman numerals are written by expressing
each digit separately starting with the leftmost
digit and skipping any digit with a value of zero.
There cannot be more than 3 identical symbols in a row.

In Roman numerals:

1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.
Example:

   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""

def solution(n):
    ROMAN_NUMERALS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    n_str = str(n)
    len_n_str = len(n_str)
    num_div = []
    for part in n_str:
        num = part.ljust((len_n_str), '0')
        len_n_str -= 1 
        num_div.append(num)
    print(num_div)
    print("------")
    for num in num_div:
        if not int(num):
            pass
        else:
            print(num)
    

solution(1)
solution(5)
solution(10)
solution(50)
solution(100)
solution(500)
solution(1000)

solution(3)
solution(8)
solution(16)
solution(78)
solution(236)
solution(119)
solution(802)
solution(1354)
solution(2354)
