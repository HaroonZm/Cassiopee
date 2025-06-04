a = map(int, raw_input().split())
a.sort()
a.reverse()
i = 0
while i < len(a):
    print a[i],
    i += 1