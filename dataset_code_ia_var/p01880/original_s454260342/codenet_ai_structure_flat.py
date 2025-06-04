N = int(input())
A = [int(x) for x in input().split()]
ans = -1
for i in range(N):
    for j in range(i + 1, N):
        prod = A[i] * A[j]
        num = [int(x) for x in str(prod)]
        ok = True
        for k in range(len(num) - 1):
            if num[k] + 1 != num[k + 1]:
                ok = False
                break
        if ok and ans < prod:
            ans = prod
print(ans)