import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

# 右隣の要素を計算できるように円環扱い
def next_idx(x):
    return (x + 1) % N

def prev_idx(x):
    return (x - 1) % N

ans = 0
for start in range(N):
    taken = [False]*N
    joi_sum = A[start]
    taken[start] = True
    # ioiの順番 = True, joiの順番 = False。初手はjoiがとったのでioiのターンから
    turn_ioi = True
    # 取りうるピースの条件を満たすものを探索する関数
    def available_pieces():
        res = []
        for i in range(N):
            if taken[i]:
                continue
            # 両隣のどちらかが取得済みなら取れる
            if taken[prev_idx(i)] or taken[next_idx(i)]:
                res.append(i)
        return res

    while True:
        av = available_pieces()
        if not av:
            break
        if turn_ioi:
            # ioiはサイズ最大のやつを取る
            m = max(av, key=lambda x: A[x])
            taken[m] = True
            turn_ioi = False
        else:
            # joiは好きなやつを取れる → Joiはこの時点で最大和狙いたいが、
            # 贅沢に全探索不可→代わりにとりうる最大サイズとってよい（問題文より好きに取れるから最大値で良い)
            m = max(av, key=lambda x: A[x])
            taken[m] = True
            joi_sum += A[m]
            turn_ioi = True
    ans = max(ans, joi_sum)
print(ans)