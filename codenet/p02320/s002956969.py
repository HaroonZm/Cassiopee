import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_G&lang=ja
from collections import deque

def main():
    n, wn = MI()
    dp = [0] * (wn + 1)
    for _ in range(n):
        v, w, m = MI()
        # wのmodごとに１つの数列として扱う
        for md in range(w):
            # スライド最大値をいれておくdeque
            q = deque()
            # インデックスのmodが等しい要素だけ取り出した数列のi番目に対しての処理
            for i in range((wn - md) // w + 1):
                # 更新したい場所の今の値を、先頭まで戻したと仮定した値で持っておく
                val = dp[i * w + md] - v * i
                # deque内は単調減少にしたいのでこれから追加するval以下の値は削除
                while q and q[-1][1] <= val: q.pop()
                # 今の値を追加
                q.append((i, val))
                # dequeの先頭を使って更新
                dp[i * w + md] = q[0][1] + v * i
                # 先頭が次に範囲外に出るようであれば削除
                if q[0][0] == i - m: q.popleft()
    print(dp[-1])

main()