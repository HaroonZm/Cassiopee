n = int(input())
a = list(map(int, input().split()))
q = int(input())
commands = [tuple(map(int, input().split())) for _ in range(q)]

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

if is_sorted(a):
    print(0)
else:
    result = -1
    for i, (x, y) in enumerate(commands, 1):
        a[x-1], a[y-1] = a[y-1], a[x-1]
        if is_sorted(a):
            result = i
            break
    print(result)