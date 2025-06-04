# インポートする標準ライブラリ
import sys  # sysライブラリは、標準入力や終了などPythonインタプリタとの対話に用いる

def main():
    # 入力から最初の1行を受け取る
    # input()は1行分の文字列を受け取る、その後split()で空白区切りのリストに分割
    # map(int, ...)で全ての要素をint型に変換
    n, q = map(int, input().split())  # nは要素の個数、qはクエリの回数

    # Pというリスト(配列)を作成する
    # インデックスと同じ数値を要素としたリストをn個作る
    # これは「各要素が自分自身を親（ルート）として始まる」という意味
    P = [i for i in range(n)]  # Union-Findの親配列。各集合の親要素（初期状態では自分自身）

    # sys.stdinは標準入力（複数行）を扱うオブジェクト
    # for文により残り全ての入力行を1行ずつ取り出して処理する
    for line in sys.stdin:
        # strip("\n")により末尾の改行(\n)を除去
        # split()で空白区切り文字列をリストに分割
        order = line.strip("\n").split()  # order[0]はコマンド番号, order[1:],がクエリの引数

        # order[1:]の部分(インデックス1以降)をx, yの二つの整数として取得
        x, y = map(int, order[1:])

        # xがyより大きい場合は変数を入れ替える（小さい側をxに）
        if x > y:
            x, y = y, x  # 入れ替え（Pythonの多重代入で一行）

        # xの属する集合（ルート）を調べる
        # 「xが自身の親かどうか」をwhileで繰り返し、親をたどる
        while True:
            x = P[x]  # xを親で置き換え
            if x == P[x]:  # もし親自身が自分自身（=この集合の頂点）
                break  # ループを抜ける

        # yの属する集合（ルート）を調べる（同様）
        while True:
            y = P[y]
            if y == P[y]:
                break

        # コマンドが"0"の場合、xとyの集合を併合(union)
        if order[0] == "0":
            P[x] = P[y]  # xの親をyの親にすることで併合

        # コマンドが"1"の場合、xとyが同じ集合に属するかどうか判定(same)
        elif order[0] == "1":
            # yとxが等しければ（ルートが同じ）1を、違えば0を出力
            if y == x:
                print(1)
            else:
                print(0)

# Pythonスクリプトとして直接呼び出された時のみmainを実行する
if __name__ == '__main__':
    main()