def slove():
    import sys
    import bisect
    import collections
    import fractions
    import heapq
    import itertools
    input = sys.stdin.readline
    n, m = list(map(int, input().rstrip('\n').split()))
    ks = [list(map(int, input().rstrip('\n').split())) for _ in range(m)]
    p = list(map(int, input().rstrip('\n').split()))
    a_cnt = 0
    for v in itertools.product([True, False], repeat=n):
        b = True
        for j, vv in enumerate(ks):
            cnt = 0
            for i in range(vv[0]):
                if v[vv[i+1]-1]:
                    cnt += 1
            if cnt % 2 != p[j]:
                b = False
                break
        if b:
            a_cnt += 1
    print(a_cnt)

if __name__ == '__main__':
    slove()