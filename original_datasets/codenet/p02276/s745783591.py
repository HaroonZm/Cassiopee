def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

num = int(input())
num_list = [int(s) for s in input().split()]

idx = partition(num_list, 0, len(num_list) - 1)

print(*num_list[:idx], end="")
print(" [" + str(num_list[idx]) + "] ", end="")
print(*num_list[idx+1:])