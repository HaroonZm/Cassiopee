BIG_NUM = 10**18

N = int(input())
H = list(map(int, input().split(" ")))

l = [BIG_NUM] * (N+10)
l[0] = 0

for i in range(1, N):
    l[i] = min(
        l[i-1] + abs(H[i] - H[i-1]),
        l[i-2] + abs(H[i] - H[i-2]),
    )

print(l[N-1])