def LCM(x, y):
    set1 = set(range(x, x*y+1, x))
    set2 = set(range(y, x*y+1, y))
    set3 = set1&set2
    return min(set3)
a, b = map(int, input().split())
print(LCM(a, b))