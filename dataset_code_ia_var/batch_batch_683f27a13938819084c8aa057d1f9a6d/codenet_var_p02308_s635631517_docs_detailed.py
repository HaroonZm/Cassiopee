#!/usr/bin/env python

import sys
import math
import itertools as it
from collections import deque

# Increase the recursion limit to handle deep recursions, if any.
sys.setrecursionlimit(10000000)

def read_circle():
    """
    Read the circle parameters (center x, center y, and radius r) from standard input.

    Returns:
        tuple: (x, y, r) where x and y are floats for the circle center, r is the float radius.
    """
    x, y, r = map(float, raw_input().split())
    return x, y, r

def read_number_of_queries():
    """
    Read the integer number of queries from standard input.

    Returns:
        int: Number of queries to process.
    """
    q = input()
    return q

def read_segment():
    """
    Read the coordinates of a line segment from standard input.

    Returns:
        tuple: (x1, y1, x2, y2) all as floats, representing the segment from (x1, y1) to (x2, y2).
    """
    x1, y1, x2, y2 = map(float, raw_input().split())
    return x1, y1, x2, y2

def compute_tangent_points(x, y, r, x1, y1, x2, y2):
    """
    Compute the two tangent points from the circle center to the line defined by segment endpoints.

    Args:
        x (float): x-coordinate of the circle center.
        y (float): y-coordinate of the circle center.
        r (float): Radius of the circle.
        x1 (float): x-coordinate of the first point of the segment.
        y1 (float): y-coordinate of the first point of the segment.
        x2 (float): x-coordinate of the second point of the segment.
        y2 (float): y-coordinate of the second point of the segment.

    Returns:
        list: Two points [(xA, yA), (xB, yB)] corresponding to the points of intersection with sorted order.
    """
    # Compute direction vector of the line segment
    vx = x2 - x1
    vy = y2 - y1
    # Compute squared norm of the line segment's direction vector
    norm = vx * vx + vy * vy
    # Project the vector from point (x1, y1) to circle center (x, y) onto the line direction
    inn = vx * (x - x1) + vy * (y - y1)
    # Find closest point (xc, yc) on the line to the circle center
    xc = x1 + vx * inn / norm
    yc = y1 + vy * inn / norm

    # By Pythagoras: the intersection points are at distance 'rem' from (xc, yc) along the line
    dist2 = (xc - x) ** 2 + (yc - y) ** 2
    rem = math.sqrt(max(0, r ** 2 - dist2))

    # Normalize the direction vector and get offset to intersection points
    norm_sqrt = math.sqrt(norm)
    dx = vx / norm_sqrt * rem
    dy = vy / norm_sqrt * rem

    # The two intersection points (possibly the same point if just tangent)
    point1 = (xc + dx, yc + dy)
    point2 = (xc - dx, yc - dy)

    # Return sorted order for stability in output
    return sorted([point1, point2])

def print_points(points):
    """
    Print the coordinates of two points with high precision, formatted as required.

    Args:
        points (list): List of two 2D points to output.
    """
    print "%.10f %.10f %.10f %.10f" % (points[0][0], points[0][1], points[1][0], points[1][1])

def main():
    """
    Main execution function: reads input, processes queries, computes and prints intersection points.
    """
    # Read circle parameters
    x, y, r = read_circle()
    # Read number of segment queries
    q = read_number_of_queries()
    # Process each query
    for _ in range(q):
        x1, y1, x2, y2 = read_segment()
        points = compute_tangent_points(x, y, r, x1, y1, x2, y2)
        print_points(points)

if __name__ == "__main__":
    main()