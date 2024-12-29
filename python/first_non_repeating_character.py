"""
Write a function named first_non_repeating_letter†
that takes a stringinput, and returns the
first character that is not repeated
anywhere in the string.

For example, if given the input 'stress',
the function should return 't', since the
letter t only occurs once in the string,
and occurs first in the string.

As an added challenge, upper- and lowercase
letters are considered the same character,
but the function should return the correct
case for the initial letter. For example,
the input 'sTreSS' should return 'T'.

If a string contains all repeating characters,
it should return an empty string ("");

† Note: the function is called
firstNonRepeatingLetter for historical reasons,
but your function should handle any Unicode
character.
"""

def first_non_repeating_letter(s):
    """
    Finds the first non-repeating letter
    in a string.

    Args:
        s (str): The input string.

    Returns:
        str: The first non-repeating letter.
             If all letters are repeated,
             returns an empty string.
    """
    s_lower = s.lower()
    for letter in s_lower:
        if s_lower.count(letter) == 1:
            return s[s_lower.index(letter)]
    return ''
