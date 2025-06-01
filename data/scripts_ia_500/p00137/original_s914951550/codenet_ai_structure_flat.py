n = int(input())
t = []
for i in range(n):
    t.append(int(input()))
for i in range(n):
    print("Case {0}:".format(i+1))
    s = t[i]
    for j in range(10):
        s = s * s
        s = int(s / 100)
        s = s % 10000
        print(s)