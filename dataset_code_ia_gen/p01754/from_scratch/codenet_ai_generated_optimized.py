import sys
input = sys.stdin.readline

N,P,Q = map(int, input().split())
C = [int(input()) for _ in range(N)]

offset = 500000
dp_prev = [-10**15]*(2*offset+1)
dp_prev[Q+offset] = 0

for i in range(N):
    dp_curr = [-10**15]*(2*offset+1)
    for j in range(2*offset+1):
        if dp_prev[j]==-10**15:
            continue
        # 食堂に行く: 自炊パワー-1
        if j>0:
            val = dp_prev[j]+C[i]
            if val > dp_curr[j-1]:
                dp_curr[j-1] = val
        # 自炊する: 自炊パワー+1
        if j<2*offset:
            val = dp_prev[j] + P*(j - offset)
            if val > dp_curr[j+1]:
                dp_curr[j+1] = val
    dp_prev = dp_curr

print(max(dp_prev))