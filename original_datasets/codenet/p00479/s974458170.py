def getN():
    return int(input())

def getlist():
    return list(map(int, input().split()))

def solve(n, pos):
    x,y = pos
    if x > n // 2:
        x = n - x + 1
    if y > n // 2:
        y = n - y + 1

    if x == y:
        color = ( (x-1) % 3 ) + 1
    else:
        definitive = min(x,y)
        color = ((definitive - 1) % 3) + 1
    return color

n = getN()
k = getN()

for i in range(k):
    pos = getlist()
    print(solve(n, pos))