from sys import stdin

N = stdin.readline().rstrip()
print("No" if any(c == 'L' for c in N[::2]) or any(c == 'R' for c in N[1::2]) else "Yes")