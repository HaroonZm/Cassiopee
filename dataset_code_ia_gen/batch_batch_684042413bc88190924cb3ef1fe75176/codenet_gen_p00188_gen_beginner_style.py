while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    k = int(input())
    left = 0
    right = n - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        count += 1
        if arr[mid] == k:
            break
        elif k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    print(count)