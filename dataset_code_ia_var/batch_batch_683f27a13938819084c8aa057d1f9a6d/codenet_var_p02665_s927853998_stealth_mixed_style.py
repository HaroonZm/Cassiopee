import sys

def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    limit = [1]
    [limit.append((limit[-1]-A[i-1])*2 if i!=N else A[i]) or (sys.exit(print(-1))) if (i>0 and limit[-1]<0) else None for i in range(1,N+1)]

    if not N:
        if A[0]!=1:
            print(-1)
            return

    ans = [A[-1]]
    now_leaf = A[-1]
    for ix in range(N-1, -1, -1):
        v = min(now_leaf + A[ix], limit[ix])
        ans.append(v)
        now_leaf = v

    for idx, a in enumerate(A[:-1]):
        if (ans[N-idx]-a)*2 < A[idx+1]:
            print(-1)
            return
    print(sum(ans))

if __name__=='__main__':
    main()