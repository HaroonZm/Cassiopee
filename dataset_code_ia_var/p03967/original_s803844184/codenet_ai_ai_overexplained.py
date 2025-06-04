# 定数の初期化部分
mod = 10 ** 9 + 7  # よく使われる大きな素数。主に計算途中でのオーバーフローを防ぐためのMOD演算（剰余）に使う
mod2 = 2 ** 61 + 1  # もう一つの大きな素数。用途はMOD演算

# 標準ライブラリのimport
from collections import deque  # データ構造のdeque（両端キュー）を使うため
import heapq  # ヒープキュー（優先度付きキュー）を使うため
import time  # 時間計測などに使う
from bisect import bisect_left, insort_left, bisect_right  # 二分探索やソート済みリストへの挿入（効率的な探索・操作）
import sys  # 標準入力・標準出力など、システム関連の機能を利用するため

# 標準入力の高速化: sys.stdin.readline()をinputとして使う
input = sys.stdin.readline

# 0~9の数字をリストにしたもの。後で利用するために定義
_NUMINT_ALL = list(range(10))

# メイン関数の定義
def main():
    # solveという関数を呼び出して答えを得る
    ans = solve()

    # ansがTrueまたはFalseの場合、YesNo関数を呼ぶ（TrueならYes、FalseならNoを出力）
    if ans is True or ans is False:
        YesNo(ans)
    # ansがNone以外の値（例えば数字やリスト）の場合は、そのままprintする
    elif ans is not None:
        print(ans)

# 問題ごとに個別に実装するメインロジック
def solve():
    # 入力を整数もしくはリストとして受け取る iip関数を利用
    s = iip()
    # curを-1で初期化。意味はコードの流れで決まる
    cur = -1
    # 結果（答え）を0で初期化
    ans = 0
    # 入力sについてループ
    for i in s:
        # curが0より大きい場合
        if cur > 0:
            ans += 1  # ansに1を加算
        # 文字が"p"だった場合
        if i == "p":
            ans -= 1  # ansから1減算
        # curの符号を反転。-1→1, 1→-1
        cur *= -1
    # 結果をprint。mainの条件によらず必ず出力する
    print(ans)

# ここからはよく使う汎用関数の集まり（ライブラリ集）

# 切り上げ除算を実行（1.3→2, -1.3→-1のような動作）
def kiriage_warizan(a, b):
    return -(-a // b)

# input文字列をint型としてリストで返す。listed=Falseで1個なら値のみ返す
def iip(listed=True):  # 数字のinputをlistで受け取る（デフォルトでTrue）
    d = input().rstrip("\n").split()  # 入力行を除外し、空白区切りでリスト化
    try:
        # 各要素をintに変換
        ret = [int(i) for i in d]
    except:
        # int変換できなければ、1桁の数字（0~9）はint化、それ以外はそのまま
        ret = [int(i) if i in _NUMINT_ALL else i for i in d]
        if len(ret) == 1:
            return ret[0]  # 要素が一つなら値だけ返す

    # listed=Falseかつ長さ1のとき値だけ返す
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret

# 複数回 iip() を呼び、縦に並んだ複数行の値をリストでまとめる
def iipt(l, listed=False, num_only=True):
    ret = []
    for i in range(l):
        ret.append(iip(listed=listed))
    return ret

# 最大公約数: リストAの最大公約数を求める（ユークリッド互除法的だが非効率）
def saidai_kouyakusuu(A):
    l = len(A)
    while True:
        m = min(A)  # 最小値
        mx = max(A)  # 最大値
        if m == mx:
            return m  # すべて等しい→最大公約数
        for i in range(l):
            if A[i] % m == 0:
                A[i] = m  # 割り切れるのでmに
            else:
                A[i] %= m  # そうでなければmで割った余り

# グラフ構築時の辺情報リスト作成（未使用かつ不完全な実装に見える）
def make_graph_edge_flat(N):
    ret = []
    for i in range(N - 1):
        a, b, c = iip()
        a -= 1  # 0-indexedに直す
        b -= 1
        ret[a].append((b, c))
        ret[b].append((a, c))
    return ret

# タプルのリストlをindex番目の値でソート。lがリストでなければ一度リスト化してsortedの結果を返す
def sort_tuples(l, index):
    if isinstance(l, list):
        l.sort(key=lambda x: x[index])
        return l
    else:
        l = list(l)
        return sorted(l, key=lambda x: x[index])

# リストlの要素ごとに個数をカウントし、辞書で返す
def count_elements(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

# リストlのindex番目を安全に取得。範囲外なら例外もしくはdefault値で返す
def safeget(l, index, default="exception"):
    if index >= len(l):
        if default == "exception":
            raise Exception("".join(["safegetに不正な値 ", index, "が渡されました。配列の長さは", len(l), "です"]))
        else:
            return default
    elif index < 0:
        if default == "exception":
            raise Exception("".join(["safegetに不正な値 ", index, "が渡されました。負の値は許可されていません"]))
        else:
            return default
    else:
        return l[index]

# 文字列sを文字ごとにソートして結合した新しい文字列を返す
def sortstr(s):
    return "".join(sorted(s))

# 入力文字列を、startcode（標準は"a"のASCIIコード）との差分リストにして返す
def iip_ord(startcode="a"):
    if isinstance(startcode, str):
        startcode = ord(startcode)
    return [ord(i) - startcode for i in input()]

# 真理値や0/1の値を「Yes」「No」と出力する
def YesNo(s):
    if s:
        print("Yes")
    else:
        print("No")

# リストや二次元リストを一つずつprintする
def fprint(s):
    for i in s:
        print(i)

# 長さNのビット列すべてをリストで返す（二進数全列挙）
def bitall(N):
    ret = []
    for i in range(2 ** N):
        a = []
        n = i  # iの値を操作するための変数nを導入
        for j in range(N):
            a.append(n % 2)  # nを2で割った余り（iの各ビット）
            n //= 2  # nを2で割って次の桁へ
        ret.append(a)
    return ret

# リストsの中身をスペース区切りで出力
def split_print_space(s):
    print(" ".join([str(i) for i in s]))

# リストsの中身を改行区切りで出力
def split_print_enter(s):
    print("\n".join([str(i) for i in s]))

# 素因数分解。nを素数で割れるまで割り、割った素数をリストで返す
def soinsuu_bunkai(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            ret.append(i)
        if i > n:
            break
    if n != 1:
        ret.append(n)
    return ret

# nCr（組み合わせ数）をmodで計算する。test=Trueなら出力
def conbination(n, r, mod, test=False):
    if n <= 0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0
    if r == 1:
        return n
    ret = 1
    for i in range(n - r + 1, n + 1):
        ret *= i  # 分子部分
        ret = ret % mod  # 毎回mod

    bunbo = 1
    for i in range(1, r + 1):
        bunbo *= i  # 分母部分
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod  # 分母の逆元を掛けて最終的なnCrを求める
    if test:
        # printで詳細を出したいときだけ
        pass
    return ret

# nのmodにおける逆元を計算する
def inv(n, mod):
    return power(n, mod - 2, mod)  # フェルマーの小定理利用

# nのp乗をmodで計算（繰り返し二乗法）
def power(n, p, mod_=mod):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p // 2, mod_) ** 2) % mod_
    if p % 2 == 1:
        return (n * power(n, p - 1, mod_)) % mod_

# 二分探索でmax/min（関数funcに対して）。side=leftで左側, rightで右側
def nibutan_func(func, target, left, right, side="left"):
    l = left
    r = right
    x = (l + r) // 2
    while r - l > 1:
        x = (l + r) // 2
        if func(x) == target:
            return x
        elif func(x) > target:
            r = x
        else:
            l = x

    if side == "left" or func(x) == target:
        return l
    else:
        return r

# ソート済リストlist_に対しtargetを探す二分探索
def nibutan_list(list_, target, side="left"):
    if not isinstance(list_, list):
        list_ = list(list_)
    l = 0
    r = len(list_)
    x = (l + r) // 2
    while r - l > 1:
        x = (l + r) // 2
        if list_[x] == target:
            return x
        elif list_[x] > target:
            r = x
        else:
            l = x

    if side == "left" or list_[x] == target:
        return l
    else:
        return r

# Union Find Tree（素集合データ構造）のクラス
class UfTree():
    # 初期化（maxnum: 要素数）
    def __init__(self, maxnum):
        # 親を自分自身で初期化
        self.parent = list(range(maxnum))
        # 各木のサイズを1で初期化
        self._size = [1] * maxnum
        # ランク(根の深さに等しい)
        self.rank = [0] * maxnum

    # 頂点aが属する集合のサイズを返す
    def size(self, a):
        return self._size[self.root(a)]

    # 頂点aの親を再帰的にたどって根（リーダー）を返す
    def root(self, a):
        rank = 0
        cur = a
        while True:
            if self.parent[cur] == cur:
                # 経路圧縮も可能（コメントアウトされているが）
                return cur
            else:
                # 経路圧縮代わりの一段短縮
                self.parent[cur] = self.parent[self.parent[cur]]
                cur = self.parent[cur]
                rank += 1

    # a, bを同じグループにまとめる
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:  # すでに同じ親なら何もしない
            return self
        # サイズを更新し、rbの親をraへ付け替える
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        return self

# Pythonファイルとして直接実行されたときだけmain()を呼ぶ
if __name__ == "__main__":
    main()