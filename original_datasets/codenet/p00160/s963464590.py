def process(x, y, h, w):
    if x+y+h <= 60 and w <= 2:
        return 600
    elif x+y+h <= 80 and w <= 5:
        return 800
    elif x+y+h <= 100 and w <= 10:
        return 1000
    elif x+y+h <= 120 and w <= 15:
        return 1200
    elif x+y+h <= 140 and w <= 20:
        return 1400
    elif x+y+h <= 160 and w <= 25:
        return 1600
    else:
        return 0

result = []
while True:
    n = int(input())
    if n == 0: break
    total = 0
    for _ in range(n):
        x, y, h, w = map(int, input().split())
        total += process(x, y, h, w)
    result.append(total)
print('\n'.join(map(str, result)))