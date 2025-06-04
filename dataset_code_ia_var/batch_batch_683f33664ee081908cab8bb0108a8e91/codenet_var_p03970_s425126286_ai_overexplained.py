# Import future features to ensure compatibility across Python versions
from __future__ import print_function  # Ensures print() function works as in Python 3 in Python 2.x
from __future__ import unicode_literals  # Makes all string literals in the code unicode by default
from __future__ import division  # Changes division operator '/' to always produce floating point division as in Python 3
from __future__ import absolute_import  # Ensures that imports are absolute by default, as in Python 3

# Import the math module which provides various mathematical functions
import math

# Import the string module which contains common string operations and constants
import string

# Import the itertools module which contains functions that create iterators for efficient looping
import itertools

# Import the fractions module, which provides support for rational number arithmetic
import fractions

# Import the heapq module which provides heap queue (priority queue) algorithms
import heapq

# Import the collections module, which implements specialized container datatypes
import collections

# Import the re module, which provides regular expression matching operations
import re

# Import the array module, which provides an array data structure
import array

# Import the bisect module, which is used for array bisection algorithms
import bisect

# Define a function named array2d which creates a two-dimensional array (list of lists)
# d1: number of rows in the 2D array
# d2: number of columns in the 2D array
# init: the initial value to fill in every cell of the array
def array2d(d1, d2, init = None):
    # The outer list comprehension runs d1 times to make d1 rows
    # The inner list comprehension runs d2 times to fill each row with init value
    # This creates a two-dimensional array filled with init
    return [[init for _ in range(d2)] for _ in range(d1)]

# Take input from the user
# input() reads a line as a string from standard input
# strip() removes any leading and trailing whitespace (including newline)
s = input().strip()

# Define the correct string to compare against
c = "CODEFESTIVAL2016"

# Initialize a counter to count the number of characters that are different
cnt = 0

# Loop over each index 'i' in the range of the length of the correct string 'c'
for i in range(len(c)):
    # Compare the character in the input string 's' at position i with the character in 'c' at position i
    if s[i] != c[i]:  # If the characters are not the same
        cnt += 1      # Increment the counter by 1

# Print the final count, which represents the number of characters that differ between 's' and 'c'
print(cnt)