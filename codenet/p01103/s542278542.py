import sys
# python template for atcoder1
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def calcVolume(L, R, T, B, min_wall):
    '''
    池の体積を計算
    '''
    ret = 0
    for w in range(L, R+1):
        for h in range(B, T+1):
            ret += (min_wall-garden[h][w])
    return ret

def pondsVolume(L, R, T, B):
    '''
    池の体積をreturn
    池を作れないなら-1
    '''
    # 池の中で一番高い所
    max_in_pond = 0
    for w in range(L, R+1):
        for h in range(B, T+1):
            max_in_pond = max(max_in_pond, garden[h][w])
    # 周りの壁の一番低い所
    min_wall = float('inf')
    for w in range(L-1, R+2):
        min_wall = min(min_wall, garden[B-1][w], garden[T+1][w])
    for h in range(B-1, T+2):
        min_wall = min(min_wall, garden[h][L-1], garden[h][R+1])

    if min_wall <= max_in_pond:
        return -1
    else:
        return calcVolume(L, R, T, B, min_wall)

while True:
    d, w = map(int, input().split())
    if d == 0:
        break
    garden = [list(map(int, input().split())) for _ in range(d)]
    ans = 0
    wallMin = 0
    # 池の範囲を全探索
    for L in range(1, w-1):
        for B in range(1, d-1):
            for R in range(L, w-1):
                for T in range(B, d-1):
                    ans = max(ans, pondsVolume(L, R, T, B))
    print(ans)