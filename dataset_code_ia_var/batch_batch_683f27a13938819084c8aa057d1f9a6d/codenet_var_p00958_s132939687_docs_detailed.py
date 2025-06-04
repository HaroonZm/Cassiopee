#!/usr/bin/python3

from fractions import Fraction
import os
import sys
import math

class Vec(object):
    """
    A 2D vector class supporting basic vector arithmetic and utility methods.

    Attributes:
        x (int or float): The x-coordinate of the vector.
        y (int or float): The y-coordinate of the vector.
    """

    def __init__(self, x, y):
        """
        Initialize a new Vec instance.
        
        Args:
            x (int or float): The x-coordinate.
            y (int or float): The y-coordinate.
        """
        self.x = x
        self.y = y
        super().__init__()

    def __add__(self, other):
        """
        Add two vectors.
        
        Args:
            other (Vec): The vector to add.
        
        Returns:
            Vec: The resultant vector.
        """
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtract another vector from this vector.
        
        Args:
            other (Vec): The vector to subtract.
        
        Returns:
            Vec: The resultant vector.
        """
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """
        Multiply this vector by a scalar.
        
        Args:
            scalar (int or float): The scalar to multiply with.
        
        Returns:
            Vec: The resultant vector.
        """
        return Vec(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """
        Right multiplication for scalar * Vec.
        
        Args:
            scalar (int or float): The scalar to multiply with.
        
        Returns:
            Vec: The resultant vector.
        """
        return Vec(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """
        Divide this vector by a scalar.
        
        Args:
            scalar (int or float): The scalar to divide by.
        
        Returns:
            Vec: The resultant vector.
        """
        return Vec(self.x / scalar, self.y / scalar)

    def __iadd__(self, other):
        """
        In-place vector addition.
        
        Args:
            other (Vec): The vector to add.
        
        Returns:
            Vec: self after operation.
        """
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        """
        In-place vector subtraction.
        
        Args:
            other (Vec): The vector to subtract.
        
        Returns:
            Vec: self after operation.
        """
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, scalar):
        """
        In-place scalar multiplication.
        
        Args:
            scalar (int or float): The scalar to multiply with.
        
        Returns:
            Vec: self after operation.
        """
        self.x *= scalar
        self.y *= scalar
        return self

    def __idiv__(self, scalar):
        """
        In-place scalar division (Python 2 style, deprecated).
        
        Args:
            scalar (int or float): The scalar to divide by.
        
        Returns:
            Vec: self after operation.
        """
        self.x /= scalar
        self.y /= scalar
        return self

    def __neg__(self):
        """
        Unary negation of the vector.

        Returns:
            Vec: The negated vector.
        """
        return Vec(-self.x, -self.y)

    def __eq__(self, other):
        """
        Compare this vector for equality with another.
        
        Args:
            other (Vec): The vector to compare.
        
        Returns:
            bool: True if coordinates are equal, False otherwise.
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        Compare this vector for inequality with another.
        
        Args:
            other (Vec): The vector to compare.
        
        Returns:
            bool: True if coordinates differ, False otherwise.
        """
        return not self.__eq__(other)

    def __hash__(self):
        """
        Hashcode for using Vec in hashable containers.

        Returns:
            int: Hash value.
        """
        return hash(('Vec', self.x, self.y))

    def dot(self, other):
        """
        Compute the dot product with another vector.
        
        Args:
            other (Vec): The other vector.
        
        Returns:
            int or float: Dot product.
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """
        Compute the cross product with another vector (returns scalar).

        Args:
            other (Vec): The other vector.
        
        Returns:
            int or float: The 2D cross product (scalar).
        """
        return self.x * other.y - self.y * other.x

    def abs2(self):
        """
        Compute the squared Euclidean norm of the vector.

        Returns:
            int or float: The squared norm.
        """
        return self.x * self.x + self.y * self.y

    def __abs__(self):
        """
        Compute the Euclidean norm of the vector.

        Returns:
            float: The length of the vector.
        """
        return math.sqrt(float(self.abs2()))

    def __repr__(self):
        """
        String representation for debugging.

        Returns:
            str: Human-readable string.
        """
        return '({}, {})'.format(self.x, self.y)

def inp():
    """
    Reads a single line from standard input, with trailing whitespace removed.

    Returns:
        str: The input line, stripped of trailing whitespace.
    """
    return sys.stdin.readline().rstrip()

def read_int():
    """
    Reads an integer from one line of standard input.

    Returns:
        int: The integer value read.
    """
    return int(inp())

def read_ints():
    """
    Reads a line from standard input and parses it into a list of integers.

    Returns:
        list of int: The list of integers read from input.
    """
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    """
    Debug print: behaves as print() only if DEBUG is set in the environment.
    """
    if DEBUG:
        print(*value, sep=sep, end=end)

DEBUG = 'DEBUG' in os.environ

def main():
    """
    Entry point of the program.
    Reads the number of points and their coordinates,
    then computes and prints the result by calling solve().
    """
    M = read_int()
    A = [Vec(*read_ints()) for _ in range(M)]  # Read M points into Vec instances
    print(solve(M, A))

def solve(M, A):
    """
    Solves the main computational geometry problem.
    For a set of points, computes the maximum number of unordered pairs of lines among the points
    that have the same (normalized) direction-cosine but may not coincide.
    
    Args:
        M (int): Number of points.
        A (list of Vec): List of points as Vec instances.
    
    Returns:
        int: The maximum number of unordered pairs with the particular property.
    """
    # D[i][j]: normalized direction identifier for vector from A[i] to A[j]
    D = [[None] * M for _ in range(M)]
    last_did = 0  # Used to generate new direction IDs
    did_map = {}  # Maps unique direction-cosine (fractional) representatives to ID

    # Calculate and assign direction IDs between each pair of points
    for i in range(M):
        for j in range(i + 1, M):
            v = A[j] - A[i]  # Vector from point i to point j
            # Standardize direction: always point upwards (positive y) or right (positive x if y=0)
            if v.y < 0 or (v.y == 0 and v.x < 0):
                v = -v
            # Calculate normalized "direction cosine" using squared components
            c = Fraction(v.x ** 2, v.abs2())
            # Consider sign for further uniqueness if x < 0
            if v.x < 0:
                c = -c
            # Map unique c to a direction ID
            if c not in did_map:
                did_map[c] = last_did
                did = last_did
                last_did += 1
            else:
                did = did_map[c]
            D[i][j] = did
            D[j][i] = did  # Symmetry

    used = [False] * M  # Tracks which points are currently used in the pairings
    m = {}  # Dictionary mapping direction ID to count of currently used lines in that direction
    best = 0  # Keep track of the best solution found

    def rec(i):
        """
        Recursive search (backtracking).
        Enumerates all possible ways to pair up unused points,
        accumulating pairs by direction and updating the best score found.

        Args:
            i (int): The current index to consider.
        """
        nonlocal best
        # Skip used points
        while i < M and used[i]:
            i += 1
        # If all points are used, evaluate the current configuration
        if i == M:
            s = 0
            # Count unordered pairs for each direction found (c * (c-1) // 2 for c lines per direction)
            for c in m.values():
                s += c * (c - 1) // 2
            best = max(best, s)
            return

        used[i] = True  # Mark point i as used
        # Try pairing point i with each other unused point j > i
        for j in range(i + 1, M):
            if used[j]:
                continue
            used[j] = True  # Use point j for the pair (i, j)
            d = D[i][j]  # Direction ID for the current pair
            m[d] = m.get(d, 0) + 1  # Increment count for that direction
            rec(i + 1)  # Recurse to find further pairings
            # Backtrack: restore state for next iteration
            m[d] -= 1
            if m[d] == 0:
                del m[d]
            used[j] = False
        used[i] = False  # Unmark i for upper-level calls

    # Start recursive search from the first point
    rec(0)
    return best

if __name__ == '__main__':
    main()