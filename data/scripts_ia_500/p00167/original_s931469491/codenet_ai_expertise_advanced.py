def bubble_sort(arr):
    cnt = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
                swapped = True
        if not swapped:
            break
    return cnt

while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    L = [input() for _ in range(n)]
    cnt = bubble_sort(L)
    print(cnt)