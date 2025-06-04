#!/usr/bin/env python3

import numpy as np
import sys

# Read function for binary standard input (not used in the rewritten code but present in the original script)
read = sys.stdin.buffer.read

def main():
    """
    Main function that reads input, processes matrix operations,
    and counts the number of result vectors that produce a positive sum.
    
    The program solves the following:
      - Takes an integer n (number of rows), m (number of columns), and c (constant bias).
      - Reads a list of m integers as list l.
      - Then reads n rows of m integers each, forming a 2D list p.
      - For each row in p, calculates the dot product with l, adds c, and increments a counter if the result is positive.
      - Prints the total count.
    """
    # Read n (number of rows), m (number of columns), and c (constant offset) from standard input
    n, m, c = map(int, input().split())
    
    # Read the list l of m integers (weights or coefficients)
    l = list(map(int, input().split()))
    
    # Read n rows, each containing m integers, to form the input matrix p
    p = [list(map(int, input().split())) for _ in range(n)]
    
    # Initialize a counter to track how many rows lead to a positive total
    count = 0
    
    # Iterate through each row (vector) in the matrix p
    for sor in p:
        # Start with constant c as the initial value
        tmp = c
        
        # For each element in the row, multiply by the corresponding element in l and add to tmp
        for i, j in enumerate(sor):
            tmp = tmp + j * l[i]
        
        # If the computed value is positive, increment the count
        if tmp > 0:
            count += 1
    
    # Output the final count
    print(count)

if __name__ == '__main__':
    # Call the main function when the script is run directly
    main()