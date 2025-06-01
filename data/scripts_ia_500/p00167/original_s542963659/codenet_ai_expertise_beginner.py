def bubble_sort():
    n = int(input())
    if n == 0:
        return 0
    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)
    count = 0
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
                count = count + 1
    return count

while True:
    n = int(input())
    if n == 0:
        break
    result = bubble_sort()
    print(result)