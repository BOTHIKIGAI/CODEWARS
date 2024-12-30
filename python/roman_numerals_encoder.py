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
    while len(n_str) != 0:
        for simbol, value in ROMAN_NUMERALS.items():
            num = n_str[0].ljust(len(n_str), '0')
            if int(num) >= value:
                print("Si soy menor o igual a", simbol)
            n_str = n_str[:0] + n_str[0 + 1:]
        break
            
        
        

solution(1)
solution(5)
solution(10)
solution(50)
solution(100)
solution(500)
solution(1000)