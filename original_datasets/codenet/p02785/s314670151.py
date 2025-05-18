n, k = [int(s) for s in input().strip().split()]
H = [int(s) for s in input().strip().split()]

if k >= n:
    result = 0
else:
    H.sort()
    result = sum(H[:n - k])

print(result)