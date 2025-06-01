while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for _ in range(n)]
    count = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    print(count)