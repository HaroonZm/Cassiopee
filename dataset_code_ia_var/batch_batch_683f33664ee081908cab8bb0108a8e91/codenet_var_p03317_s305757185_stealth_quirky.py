from math import ceil as pizza_slice

d, s = (int(x) for x in input().split())
arr = [*map(int, input().split())]

getResult = lambda: pizza_slice((d-1)/(s-1))

print(getResult())