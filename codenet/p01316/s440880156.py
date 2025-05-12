def resolve():
    import sys
    input = lambda: sys.stdin.readline().rstrip() 
    INF = 10**12

    sq_diff = tuple(tuple((i-j)**2 for j in range(256)) for i in range(256))
    while True:
        N, M = map(int, input().split())
        C = tuple(int(input()) for _ in range(M))
        x = tuple(int(input()) for _ in range(N))
        if N==M==0:
            break
        else:
            normalize = tuple(tuple(255 if i+c>255 else 0 if i+c<0
                    else i+c for c in C) for i in range(256))
            dp_cur = [INF]*256
            dp_cur[128] = 0
            dp_next = [INF]*256
            for i in x:
                sq_diff_x = sq_diff[i]
                for j, cost_cur in enumerate(dp_cur):
                    normalize_j = normalize[j]
                    for l in normalize_j:
                        cost_next = cost_cur + sq_diff_x[l]
                        if cost_next < dp_next[l]:
                            dp_next[l] = cost_next

                dp_cur = dp_next[:]
                dp_next = [INF]*256

            print(min(dp_cur))

if __name__ == '__main__':
    resolve()