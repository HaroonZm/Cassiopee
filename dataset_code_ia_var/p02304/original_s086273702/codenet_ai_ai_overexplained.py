from bisect import bisect_left, bisect_right, insort_left  # bisectを使うことでリストのソート済み検索・挿入ができる
from collections import deque  # dequeは両端キュー、効率よく要素の追加・削除ができる

class BinarySearchTree:
    def __init__(self, ls: list=[]):
        '''
        Pythonでソート済みで値を保持するset的データ構造。
        C++のsetに相当。ここでは標準ライブラリbisectで二分検索や挿入・削除を行う。
        ls ... 初期リスト。これをソートして保持する。
        '''
        # まずリストlsをソートし、deque型（両端キュー。popやappendが速い）で保持する
        self.bst = deque(sorted(ls))

    def __repr__(self):
        # インスタンスをprintしたときに"BST:[要素...]"と表示される
        return f'BST:{self.bst}'

    def __len__(self):
        # このクラスの要素数（長さ）を返す
        return len(self.bst)

    def __getitem__(self, idx):
        # インスタンス[index]で要素にアクセスできる
        return self.bst[idx]

    def size(self):
        # 要素数を返す。len()と同じ
        return len(self.bst)

    def insert(self, x):
        # xをソートされた順序で追加する
        # insort_leftは同じ値なら左側に挿入（安定）
        insort_left(self.bst, x)

    def remove(self, x):
        '''
        xをリストから削除。xが必ず存在している必要がある。
        同じ値が複数あった場合は左側を優先的に消す。
        '''
        del self.bst[self.find(x)]  # findで位置（インデックス）を調べて削除

    def bisect_left(self, x):
        '''
        xをソート順を保って挿入できる最左位置（左端）を返す。
        C++でいうlower_boundと同じ
        '''
        return bisect_left(self.bst, x)

    def bisect_right(self, x):
        '''
        xを挿入できる最右位置（右端）を返す。
        C++でいうupper_boundと同じ
        '''
        return bisect_right(self.bst, x)

    def find(self, x):
        '''
        xがリストの中で先頭から何番目かを調べる。
        無ければ例外を投げる。
        '''
        idx = bisect_left(self.bst, x)  # 挿入可能な最左位置を調べる
        if idx != len(self.bst) and self.bst[idx] == x:  # その場所にxがあればindexを返す
            return idx
        # 無ければエラー。removeの内部で使っているため、必ずある前提。
        raise ValueError

# --- 入力処理 ---

# Nは線分の本数
N = int(input())  # 数字1つ入力

lines = []  # 線分情報を格納するリスト
for _ in range(N):  # N行繰り返す
    # １行に4個の整数 x1 y1 x2 y2（2点の座標）が空白区切りで来る
    x1, y1, x2, y2 = list(map(int, input().split()))
    # 線分の端点を「左端(下端)」→「右端(上端)」と表すため入れ替え補正
    if y1 == y2:  # 水平線分（上下方向に動かない）
        # x1がx2より大きければ入れ替えて左→右にする
        if x1 > x2:
            x1, x2 = x2, x1
    else:  # 垂直線分
        # y1がy2より大きければ入れ替えて下→上にする
        if y1 > y2:
            y1, y2 = y2, y1
    # 補正した(x1, y1) -> (x2, y2)として保存
    lines.append((x1, y1, x2, y2))

# --- 端点（イベント）生成 ---
# 線分交差カウントのために「端点」イベントのリストを作る

# 各端点種別（識別用定数, 小さい順に重要）
BOTTOM = 0  # 縦線の「下端」
LEFT = 1    # 横線の「左端」
RIGHT = 2   # 横線の「右端」
TOP = 3     # 縦線の「上端」

endpoints = []  # 端点のリスト
for x1, y1, x2, y2 in lines:
    if y1 == y2:  # 水平線の場合
        # 左端点イベント追加 (y座標, 端点種別, x座標, 右のx)
        endpoints.append((y1, LEFT, x1, x2))
        # 右端点イベント追加 (同様にy座標, 端点種別, x座標, ダミー-1)
        endpoints.append((y2, RIGHT, x2, -1))
    else:  # 垂直線の場合
        # 下端点イベント追加 (y座標, 端点種別, x座標, ダミー-1)
        endpoints.append((y1, BOTTOM, x1, -1))
        # 上端点イベント追加 (y座標, 端点種別, x座標, ダミー-1)
        endpoints.append((y2, TOP, x2, -1))

# y座標・種別で昇順ソート。yの下から走査のため、イベント順番を担保
endpoints.sort()

# --- スイープライン処理開始 ---

bst = BinarySearchTree()  # 現在の交点検出に利用する「x座標の集合」（縦線のみ記録）
ans = 0  # 交点数の答え

for y, p_type, x, x_t in endpoints:
    # p_type: 端点の種別
    if p_type == TOP:
        # 縦線の上端（終了）：そのx座標をbstから削除する
        bst.remove(x)
    elif p_type == BOTTOM:
        # 縦線の下端（開始）：そのx座標をbstに挿入する
        bst.insert(x)
    elif p_type == LEFT:
        # 横線の左端（線分の始点）
        # 水平線y=y1に対し、xがx1からx2まである
        # 今bstにはy1をまたぐ全ての縦線のx座標が登録されている
        # その区間[x1, x2]に含まれるx座標の個数が交点の数
        s = bst.bisect_left(x)      # x1より大きい/等しい縦線は何番目からか
        t = bst.bisect_right(x_t)   # x2以下の縦線は何番目までか（上限含む）
        ans += t - s                # その差が交差する本数（個数）
    # RIGHT端点（水平線の終点）は何もしない（線分は左端だけで交差を数えられる）

print(ans)  # 答え（交点総数）を出力