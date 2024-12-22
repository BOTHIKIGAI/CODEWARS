"""
In this kata you will create a function that takes a
list of non-negative integers and strings and returns
a new list with the strings filtered out.
"""

def filter_list(l: list):
    """
    A function to return a list only
    with strings
    """
    ls = []
    for element in l:
        if isinstance(element, int):
            ls.append(element)
    return ls

# Interesting solution
"""
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
"""
