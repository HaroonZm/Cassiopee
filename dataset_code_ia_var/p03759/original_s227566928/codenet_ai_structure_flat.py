a, b, c = map(int, input().split())
lst = [a, b, c]
lst.sort()
a = lst[0]
b = lst[1]
c = lst[2]
if c - b == b - a:
    print('YES')
else:
    print('NO')