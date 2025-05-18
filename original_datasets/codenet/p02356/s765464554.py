import sys
import os

il = lambda: list(map(int, sys.stdin.buffer.readline().split()))

def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, Q = il()
    A = il()
    Q = il()

    for q in Q:
        # 合計, 範囲, 左端の初期化
        sm, ret, l = 0, 0, 0
        for r in range(N):
            # 右端を0から、
            # 合計がq以下の位置まで進める
            sm += A[r]
            while sm > q:
                # 合計がqを上回る場合、
                # 左端をインクリメント
                sm -= A[l]
                l += 1

            # 合計がq以下となる範囲
            ret += r - l + 1

        print(ret)

if __name__ == '__main__':
    main()