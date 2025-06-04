def weird_style():
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    def f(): return list(map(int, input().split()))
    arr2 = f()
    res = 0
    i = 0
    while i < n:
        tmp = 0
        if i > 0:
            for j in range(i+1):
                tmp += arr1[j]
        else:
            tmp = arr1[0]
        def get_b():
            total = 0
            k = i
            while k <= n-1:
                total += arr2[k]
                k += 1
            return total
        b_part = get_b()
        y = tmp + b_part
        if y >= res: res = y
        i = i + 1
    print(res)
weird_style()