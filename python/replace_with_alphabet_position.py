"""
In this kata you are required to, given a
string, replace every letter with its
position in the alphabet.

If anything in the text isn't a letter,
ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example

Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 
          1 20 20 23 5 12 22 5 15 3 12 15 3
          11"
"""

def alphabet_position(text: str) -> str:
    """
    This function replace every letter
    with its position in the alphabet.
    
    return: a string with numbers
    """
    result = ""
    # iterate for each letter of the string
    for letter in text:
        # recovering the asscii value
        ascii_value = ord(letter.lower())
        # Conditional of the accepted alphabet rank
        if 96 < ascii_value < 123:
            # Calculate the value of the assci value 
            # so that it is equivalent to the alphabet
            end_value = str(ascii_value - 96)
            result += end_value + " "
    # Return value without trailing space
    return result[:-1]

# Interesting solution
"""
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""
