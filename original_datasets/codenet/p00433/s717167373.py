import sys
f = sys.stdin

s, t = [sum(map(int, f.readline().split())) for _ in range(2)]
print(s if s >= t else t)