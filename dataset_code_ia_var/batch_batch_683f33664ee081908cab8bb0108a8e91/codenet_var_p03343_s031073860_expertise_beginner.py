INF = 1 << 60

def read_int_list():
    return list(map(int, input().split()))

N, K, Q = read_int_list()
A = read_int_list()
A.append(-INF)

def get_lub(y):
    result = []
    l = 0
    for i in range(N+1):
        if A[i] < y:
            temp = A[l:i]
            temp.sort()
            if len(temp) >= K-1:
                for x in temp[:len(temp)-K+1]:
                    result.append(x)
            l = i + 1
    result.sort()
    if len(result) >= Q:
        return result[Q-1]
    else:
        return INF

ans = INF
for value in A[:-1]:
    other = get_lub(value)
    if other - value < ans:
        ans = other - value

print(ans)