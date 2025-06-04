import sys
sys.setrecursionlimit(10**7)

S = sys.stdin.readline().strip()
k = int(sys.stdin.readline().strip())
n = len(S)

dp_len = [[0]*(n) for _ in range(n)]
dp_cnt = [[-1]*(n) for _ in range(n)]

def min_pal_len(i,j):
    if i > j: return 0
    if i == j: return 1
    if dp_len[i][j]: return dp_len[i][j]
    if S[i] == S[j]:
        dp_len[i][j] = 2 + min_pal_len(i+1,j-1)
    else:
        dp_len[i][j] = min(min_pal_len(i+1,j), min_pal_len(i,j-1)) + 2
    return dp_len[i][j]

def count(i,j):
    if i > j: return 1
    if i == j: return 1
    if dp_cnt[i][j] != -1: return dp_cnt[i][j]
    res = 0
    if S[i] == S[j]:
        if min_pal_len(i,j) == 2 + min_pal_len(i+1,j-1):
            res = count(i+1,j-1)
    else:
        ml = min_pal_len(i,j)
        if ml == min_pal_len(i+1,j) + 2:
            res += count(i+1,j)
        if ml == min_pal_len(i,j-1) + 2:
            res += count(i,j-1)
    dp_cnt[i][j] = min(res, 10**18+1)
    return dp_cnt[i][j]

min_pal_len(0,n-1)
total = count(0,n-1)
if total < k:
    print("NONE")
    sys.exit()

def build(i,j,k):
    if i > j:
        return ""
    if i == j:
        return S[i]
    if S[i] == S[j]:
        cnt_ = count(i+1,j-1)
        if cnt_ >= k:
            return S[i] + build(i+1,j-1,k) + S[j]
        else:
            return None  # should not happen, k <= total
    else:
        ml = min_pal_len(i,j)
        res = ""
        if ml == min_pal_len(i+1,j)+2:
            c = count(i+1,j)
            if c >= k:
                return S[i] + build(i+1,j,k) + S[i]
            else:
                k -= c
        if ml == min_pal_len(i,j-1)+2:
            c = count(i,j-1)
            if c >= k:
                return S[j] + build(i,j-1,k) + S[j]
            else:
                k -= c
        return None

print(build(0,n-1,k))