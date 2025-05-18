"""
X以下の数をL枚以上取り出せるか？という二分探索を行う。
L枚以上取り出せるか？のテストは尺取法を用いる
"""
N,K,L = map(int,input().split())
A = list(map(int,input().split()))

def is_ok(X):
    r = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(r,N):
            if cnt2 == K-1 and A[j]<=X:
                r = j
                cnt1 += N-j
                if A[i]<=X:
                    cnt2 -= 1
                break
            elif A[j]<=X:
                cnt2 += 1
        else:
            break
    if cnt1 >= L:
        return True
    else:
        return False

def bisearch(high,low):
    while high-low>1:
        mid = (high+low)//2
        if is_ok(mid):
            high = mid
        else:
            low = mid
    return high

print(bisearch(200000,-1))