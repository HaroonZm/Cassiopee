s = input()
n = len(s)
if n == 0:
    print(0)
else:
    count = 0
    prev = s[0]
    for i in range(1, n):
        if s[i] != prev:
            count += 1
            prev = s[i]
    print(count)