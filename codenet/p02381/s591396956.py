import math
while True:
    num = int(input())
    if num == 0: break
    array = [int(i) for i in input().split()]
    mean = sum(array) / num
    a = 0
    for i in range(num):
        a += (array[i] - mean) ** 2
    a /= num
    a = math.sqrt(a)
    print(a)