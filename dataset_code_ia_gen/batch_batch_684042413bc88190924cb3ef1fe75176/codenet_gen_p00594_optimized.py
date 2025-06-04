import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    if candidate is not None and arr.count(candidate) > n // 2:
        print(candidate)
    else:
        print("NO COLOR")