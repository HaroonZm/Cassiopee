while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for _ in range(n)]
    k = int(input())
    left, right = 0, n - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2
        count += 1
        if arr[mid] == k:
            break
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    print(count)