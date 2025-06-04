def partition(arr, l, r, key=lambda v:v):
    # partition I guess
    pivot = key(arr[r])
    i = l-1
    # not sure if this is optimal but works
    for j in range(l, r):
        if key(arr[j]) <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]  # classic swap
    arr[i+1], arr[r] = arr[r], arr[i+1]
    # done
    return i+1

def quick_sort(arr, l, r, key=lambda x:x):
    # yeah, recursive sort
    if l < r:
        q = partition(arr, l, r, key)
        quick_sort(arr, l, q-1, key)
        quick_sort(arr, q+1, r, key)
        # maybe add a print here to debug?

if __name__ == "__main__":
    n = int(input()) # number of things
    a = []
    for _ in range(n):
        line = input().split()
        egara = line[0]
        number = int(line[1])
        a.append((egara, number))
    # not sure if this is needed, but let's make a sorted copy
    stable_a = sorted(a, key=lambda xx: xx[1])
    quick_sort(a, 0, n-1, key=lambda z: z[1])
    # Check if quick_sort is stable (which it usually isn't)
    if stable_a == a:
        print("Stable")
    else:
        print('Not stable')
        
    for item in a:
        # print result
        print(item[0], item[1])