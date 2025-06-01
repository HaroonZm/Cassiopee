from sys import stdin
lst = sorted(map(int, stdin.read().split()))
print("yes" if lst[0] == lst[3] == lst[4] == lst[7] == lst[8] == lst[11] else "no")