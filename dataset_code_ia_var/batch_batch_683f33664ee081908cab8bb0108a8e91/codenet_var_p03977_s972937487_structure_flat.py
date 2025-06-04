n = int(input())
for _ in range(n):
    s = input().split()
    i = int(s[0])
    j = int(s[1])
    if i % 2 == 0:
        print(127 * i - j)
    else:
        print(127 * (i - 1) + j)