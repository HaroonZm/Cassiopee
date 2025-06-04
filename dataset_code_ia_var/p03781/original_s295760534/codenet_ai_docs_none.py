import sys

X = int(input())
a = 1
cnt = 0

if X == 1:
    print("1")
else:
    while a < X:
        a = int(cnt * (cnt + 1) / 2)
        cnt = cnt + 1
    print(cnt - 1)