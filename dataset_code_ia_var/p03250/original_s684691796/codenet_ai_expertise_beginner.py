cards = input().split()
a = int(cards[0])
b = int(cards[1])
c = int(cards[2])

if a >= b and a >= c:
    max1 = a
    if b >= c:
        max2 = b
        max3 = c
    else:
        max2 = c
        max3 = b
elif b >= a and b >= c:
    max1 = b
    if a >= c:
        max2 = a
        max3 = c
    else:
        max2 = c
        max3 = a
else:
    max1 = c
    if a >= b:
        max2 = a
        max3 = b
    else:
        max2 = b
        max3 = a

ans = max1 * 10 + max2 + max3
print(ans)