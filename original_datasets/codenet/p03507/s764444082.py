if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    
    N, K = map(int,input().split())
    WD = [tuple(map(int,input().split())) for _ in range(N)]

    def solve(tgt):
        res = 0
        for w,d in WD:
            res += max(0, (tgt-w)//d+1)
        if res >= K:
            return True
        else:
            return False

    ok = 2*(10 ** 18)  # exist
    ng = 0  # not exist
    while abs(ok - ng) > 1:
        cnt = (ok + ng) // 2
        if solve(cnt):
            ok = cnt
        else:
            ng = cnt
    print(ok)