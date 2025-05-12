"""
AOJ 2426  Treasure Hunt

座標圧縮を二次元でやるっぽい
上の問題たちとちがうのは、ここからここまでが領域１です、みたいな形になっている点か。
また、例４をみると、ある領域の内側に小さな領域があるパターンもあり、小さいほうに入っている宝は両方に所属していることになるっぽい。

さっぱりなので写経
http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=2963309#1

二次元累積和がはじめてなので、そっちの練習がまず先に必要っぽい
"""

from bisect import bisect_left

def main():

    N,M = map(int, input().split())
    treasures = []

    # 宝のx,yの位置（ある宝のx,yの組ではなく、x,y座標的にどこに位置するか）
    Xs = set()
    Ys = set()

    for _ in range(N):
        x,y = map(int, input().split())
        treasures.append((x,y))
        Xs.add(x)
        Ys.add(y)

    # x,yそれぞれで座圧
    Xs = list(Xs)
    Xs.sort()
    Ys = list(Ys)
    Ys.sort()
    

    # 座標xはO番目、みたいな情報を作る
    Xd = {}
    Yd = {}
    for i,x in enumerate(Xs):
        Xd[x] = i
    for i,y in enumerate(Ys):
        Yd[y] = i

    lx = len(Xs)
    ly = len(Ys)
    # ここに宝があるよ、を座圧した情報にする
    compressd_treasures = [[0 for _ in range(lx + 1)] for _ in range(ly + 1)]
    for x,y in treasures:
        # yyy番目のy座標とxxx番目のxxx座標に宝があるよ
        compressd_treasures[Yd[y] + 1][Xd[x] + 1] += 1

    # 左下から右上に向かって、「下や左から（南から？）進んできて何個宝があるか」の累積和をとる
    # ここの操作後、comp~[y][x]で、（一番左下の座標（原点ではない））~(x,y)の長方形の中にある宝の数が得られるから、
    # うまいことやると(x1,y1)~(x2,y2)の範囲の宝の数が得られる
    for y in range(1, ly + 1):
        acc = 0
        for x in range(1, lx + 1):
            # accに足しておいて、xが進むごとに左から右へも累積和をとれる
            acc += compressd_treasures[y][x]
            # 下の所から積み上げて累積和
            compressd_treasures[y][x] = acc + compressd_treasures[y-1][x]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        # それぞれの座標について、何番目の宝まで含みうるか考える
        idx_x1 = bisect_left(Xs, x1)
        idx_x2 = bisect_left(Xs, x2)
        idx_y1 = bisect_left(Ys, y1)
        idx_y2 = bisect_left(Ys, y2)

        # 宝が領域の境界線上にあるとき、加算する(bisectした値と同じものがXs,Ysにあるとき)
        if idx_x2 < lx and Xs[idx_x2] == x2:
            idx_x2 += 1
        if idx_y2 < ly and Ys[idx_y2] == y2:
            idx_y2 += 1
        
        # 累積和で出す。l~r = 0~r - 0~l-1　を二次元にしたバージョン
        ans = compressd_treasures[idx_y2][idx_x2] - compressd_treasures[idx_y2][idx_x1] - compressd_treasures[idx_y1][idx_x2] + compressd_treasures[idx_y1][idx_x1]
        print(ans)

if __name__ =="__main__":
    main()