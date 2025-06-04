from sys import stdin
from itertools import pairwise

def min_grade_diff(n, grades):
    grades = sorted(map(int, grades))
    return min(b - a for a, b in pairwise(grades))

for line in stdin:
    n = int(line)
    if n == 0:
        break
    grades = stdin.readline().split()
    print(min_grade_diff(n, grades))