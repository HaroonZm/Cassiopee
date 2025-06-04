K = int(input())
if K % 2 == 0:
    res = (K * K) // 4
    print(res)
else:
    res = (K * K - 1) // 4
    print(res)