from sys import stdin, stdout

def bubble_sort(arr):
    cnt = 0
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                cnt += 1
                swapped = True
        if not swapped:
            break
    return cnt

input_iter = iter(map(int, stdin.read().split()))
while (n := next(input_iter)) != 0:
    arr = [next(input_iter) for _ in range(n)]
    stdout.write(str(bubble_sort(arr)) + '\n')