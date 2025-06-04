def counting_sort(nmax, la):
    counts = [0] * (nmax + 1)
    max_num = 0
    for num in la:
        counts[num] += 1
        if num > max_num:
            max_num = num
    result = []
    i = max_num
    total = len(la)
    while total > 0:
        if counts[i] > 0:
            result += [i] * counts[i]
            total -= counts[i]
        i -= 1
    return result

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = counting_sort(100000, a)
    b = counting_sort(100000, b)
    ans = n
    i = -1
    for k in range(0, n, 2):
        i += 1
        if a[k] > b[i]:
            ans = k + 1
            break
    if ans == n:
        print("NA")
    else:
        print(ans)