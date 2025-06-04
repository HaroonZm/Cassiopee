from sys import stdin

n = int(stdin.readline())
a = sorted(map(int, stdin.readline().split()))
print(sum(a[::2]))