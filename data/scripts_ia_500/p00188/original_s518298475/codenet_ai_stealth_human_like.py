while True:
    n = input()
    if n == 0:
        break
    L = [input() for i in range(n)]
    v = input()
    left, right = 0, len(L) - 1
    count = 0
    while left <= right:
        mid = (left + right) // 2   # middle index, integer division
        if L[mid] == v:
            print(count + 1)  # found it, print count+1 and stop
            break
        elif L[mid] < v:
            left = mid + 1
        else:  # if L[mid] > v
            right = mid - 1
        count += 1
    else:
        print(count)  # not found, print count here