from sys import stdin

s = list(map(int, list(stdin.readline().rstrip())))
print(min(s.count(1), s.count(0)) * 2)