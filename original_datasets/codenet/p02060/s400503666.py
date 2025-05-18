N = int(input())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
res = 100000

for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            if N < t[0] * i + t[1] * j + t[2] * k:
                if res > p[0]*i + p[1]*j + p[2]*k:
                    res = p[0]*i + p[1]*j + p[2]*k
            else:
                d = (N-t[0]*i-t[1]*j-t[2]*k + t[3] - 1) // t[3]
                if res > p[0]*i + p[1]*j + p[2]*k + p[3]*d:
                    res = p[0]*i + p[1]*j + p[2]*k + p[3]*d
print(res)