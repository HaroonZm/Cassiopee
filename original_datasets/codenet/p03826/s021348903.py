a, b ,c, d = map(int, input().split())

area1 = a*b
area2 = c*d

if area1 > area2:
    print(area1)
elif area2 >= area1:
    print(area2)