import sys

mod = 1000000007
inf = float('inf')
sys.setrecursionlimit(10**6)

a_b_line = sys.stdin.readline().rstrip()
a, b = a_b_line.split()

if a < b:
    print('<')
elif a == b:
    print('=')
else:
    print('>')