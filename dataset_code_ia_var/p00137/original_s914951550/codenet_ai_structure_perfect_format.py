def f(s):
    for j in range(10):
        s = s * s
        s = int(s / 100)
        s = s % 10000
        print(s)

n = int(input())
t = [int(input()) for i in range(n)]
for i in range(n):
    print("Case {0}:".format(i + 1))
    f(t[i])