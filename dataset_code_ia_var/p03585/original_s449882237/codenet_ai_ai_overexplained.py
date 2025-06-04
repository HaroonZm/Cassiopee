class Bit:
    # 参考1: http://hos.ac/slides/20140319_bit.pdf
    # 参考2: https://atcoder.jp/contests/arc046/submissions/6264201
    # 検証: https://atcoder.jp/contests/arc046/submissions/7435621
    # 「values」の0番目の要素は使わない（便宜上1-indexed配列とするため）
    # 配列長を2の冪数+1にして二分探索の条件を減らす

    def __init__(self, a):
        # 「a」がイテラブル（リスト，タプル等）の場合
        if hasattr(a, "__iter__"):
            le = len(a)  # 「a」の長さ（要素数）を取得
            # ビット長を使って「le」より大きい最小の2の冪を計算（1 << n は 2^n）
            self.n = 1 << le.bit_length()
            # 長さ n+1 の配列「values」を用意（0番目使わず1-indexed）
            self.values = values = [0] * (self.n + 1)
            # 1番目からle番目までにaの値を代入（a[:]でaの複製リスト）
            values[1:le + 1] = a[:]
            # 1からnまで、BITの性質に従って内部配列を構築
            for i in range(1, self.n):
                # i & -i はiの最下位ビットだけ残す
                # i+(i&-i)で親ノードを計算し、値を加算
                values[i + (i & -i)] += values[i]
        # 「a」が整数（数値）の場合
        elif isinstance(a, int):
            # 「a」個分の0値配列を内部的に作成（要素0で初期化）
            self.n = 1 << a.bit_length()  # a以上の最小の2の冪
            self.values = [0] * (self.n + 1)
        else:
            # 上記以外の型は許可しない
            raise TypeError

    def add(self, i, val):
        # i番目以降の要素に値「val」を加算する
        # これはBITの基本構造
        n, values = self.n, self.values  # ショートカット
        while i <= n:  # 配列長を超えない範囲で
            values[i] += val  # 実際に値を加算
            i += i & -i       # 次の更新対象インデックスへ飛ぶ

    def sum(self, i):  # (0, i]区間の累積和
        # values[1]からvalues[i]までの合計値を返す（iは1-indexed）
        values = self.values
        res = 0  # 結果の初期化
        while i > 0:  # 0になるまで
            res += values[i]  # 今のインデックスの値を加算
            i -= i & -i       # 下位ビット分だけ引いて遡る
        return res  # 合計値を返す

    def bisect_left(self, v):  
        # 添字iでsum(i) >= v となる最小の i を返す
        # つまり累積和がvを超える最初のインデックスを探す（1-indexed）
        n, values = self.n, self.values
        if v > values[n]:  # 全体の合計より大きい値を要求されたら失敗
            return None
        i, step = 0, n >> 1  # 探索インデックス, ステップ幅（半分から始める）
        while step:
            # まだ累積和が足りない場合、iを一気に右側に進め、vから部分和を引く
            if values[i + step] < v:
                i += step
                v -= values[i]
            # ステップ幅を半分に減らしていく（二分探索）
            step >>= 1
        return i + 1  # 1-indexed なので +1 して返す

def inversion_number(arr):
    # 「arr」の転倒数を計算する
    n = len(arr)  # 配列の長さ
    # 配列の各インデックスをarrの値でソート（値が小さい順にインデックスの並び替え）
    arr = sorted(range(n), key=lambda x: arr[x])
    bit = Bit(n)  # n要素のBITで準備
    # 総組み合わせ数 nC2 = n*(n-1)/2 をセット（転倒数の最大値）
    res = n * (n-1) >> 1  # >>1は//2
    for val in arr:
        # 転倒数を累積的に計算
        res -= bit.sum(val+1)  # 既出のインデックス位置以下のカウント分だけ減らす
        bit.add(val+1, 1)      # その位置を1増やす（訪問済み印）
    return res

N = int(input())  # 標準入力から整数を1つ読み込む（データ数N）
# N回、標準入力から3つの整数を読み込む。各行listでまとめてABCに格納
ABC = [list(map(int, input().split())) for _ in range(N)]
A, B, C = zip(*ABC)  # ABCをそれぞれA列, B列, C列で取り出す（各タプル）

# 転倒数の閾値：全対組の丁度半分以上を求めるため
th = N*(N-1)//2 // 2 + 1  

def solve(A, B, C):
    # A, B, C はそれぞれ等長のリスト
    # 目標：ある x に対し (-A*x + C)/B, そのときの転倒数が th 以上になる最大のxを探す

    # 小さめの配列と大きめ（N<100かで場合分け）
    if N < 100:
        ok = -1e10  # 二分探索の下端（十分小さい値）
        ng = 1e10   # 二分探索の上端（十分大きい値）
        n_iteration = 70  # ミッド値探索の繰り返し回数（精度用）
    else:
        ok = -1e4
        ng = 1e4
        n_iteration = 46

    # xを大きくしたときYが順序逆転しやすいよう、A/Bの降順に並べる
    # zip(A, B, C)でまとめたタプルを key=lambda x:-x[0]/x[1] で降順
    A, B, C = zip(*sorted(zip(A, B, C), key=lambda x: -x[0]/x[1]))

    for _ in range(n_iteration):
        x = (ok+ng) * 0.5  # 探索区間の中央値を毎回更新
        # Y[i] = (-A[i]*x + C[i])/B[i] を全て計算
        Y = [(-a*x + c)/b for a, b, c in zip(A, B, C)]
        inv_num = inversion_number(Y)  # Yの転倒数
        # 転倒数がしきい値（中央値）を超えている場合は「よりxを大きく」, 逆なら「小さく」
        if inv_num >= th:
            ok = x  # 今のxが条件を満たす場合なので下端を更新（右詰め）
        else:
            ng = x  # 今のxでは足りないので上端を更新（左詰め）
    return ok  # 転倒数が中央値以上となる最大のxを返す

# 「A, B, C」と「B, A, C」のそれぞれに対してsolveを適用し、結果を表示
print(solve(A, B, C), solve(B, A, C))