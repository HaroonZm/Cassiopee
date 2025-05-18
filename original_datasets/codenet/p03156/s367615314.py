n = int(input())
a, b = [int(item) for item in input().split()]
p = [int(item) for item in input().split()]

p1 = 0; p2 = 0; p3 = 0
for item in p:
    if item <= a:
        p1 += 1
    elif item <= b:
        p2 += 1
    else:
        p3 += 1
print(min(p1, p2, p3))