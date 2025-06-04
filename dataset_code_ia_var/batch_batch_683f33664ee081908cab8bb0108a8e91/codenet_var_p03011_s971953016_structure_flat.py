import sys
mod = 1000000007
inf = float('inf')
sys.setrecursionlimit(10**6)

# Read input, split, convert to int, and sort
line = sys.stdin.readline().rstrip()
L = list(map(int, line.split()))
L.sort()
print(L[0] + L[1])