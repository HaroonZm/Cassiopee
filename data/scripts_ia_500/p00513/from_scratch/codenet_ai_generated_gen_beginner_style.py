n = int(input())
areas = [int(input()) for _ in range(n)]

def is_possible(area):
    # area = 2*x*y + x + y  (x,y positive integers)
    # try all x from 1 to area, see if y is integer and positive
    for x in range(1, area+1):
        numerator = area - x
        denominator = 2*x + 1
        if numerator % denominator == 0:
            y = numerator // denominator
            if y > 0:
                return True
        if x > area:
            break
    return False

count = 0
for a in areas:
    if not is_possible(a):
        count += 1

print(count)