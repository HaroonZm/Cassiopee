from sys import stdin as s
Z, Y = map(int, s.readline().split())
answer = (Z - Y) * (Z >= Y)
print(abs(answer) if Z >= Y else 0)