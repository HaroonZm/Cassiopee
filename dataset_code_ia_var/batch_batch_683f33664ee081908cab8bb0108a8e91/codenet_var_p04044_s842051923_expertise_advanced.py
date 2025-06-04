from sys import stdin

n, l = map(int, stdin.readline().split())
print("".join(sorted((stdin.readline().strip() for _ in range(n)))))