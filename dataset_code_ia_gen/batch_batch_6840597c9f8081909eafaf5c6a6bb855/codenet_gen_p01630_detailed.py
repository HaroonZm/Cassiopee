import sys
sys.setrecursionlimit(10**7)

# ノードIDを生成するためのカウンタ
node_id_counter = 0

def get_new_node_id():
    global node_id_counter
    node_id_counter += 1
    return node_id_counter

class BDDNode:
    """
    BDDのノードを表現するクラス
    type:
        'leaf'  ->  終端（0 or 1）
        'var'   ->  変数ノード
    value:
        終端ノードの場合は0か1の値
        変数ノードの場合は変数番号（1からNまで）
    zero, one:
        変数ノードの場合、0エッジ先と1エッジ先のノードID
        終端ノードではNone
    id:
        ノードを一意に識別するID（デフォルトでは自動生成）
    """
    def __init__(self, node_type, value, zero=None, one=None):
        self.type = node_type
        self.value = value
        self.zero = zero
        self.one = one
        self.id = get_new_node_id()

    def __repr__(self):
        if self.type == 'leaf':
            return f"Leaf({self.value})"
        else:
            return f"Var({self.value}, zero={self.zero}, one={self.one})"

def build_bdd(N, truth_table, var_index=1, start=0, length=None):
    """
    真理値表のbit列truth_tableからBDDを構築する関数
    - N: 変数の数
    - truth_table: 真理値テーブルを表す'0'/'1'文字列（長さ2^N）
    - var_index: 現在構築している変数番号(1からNまで)
    - start: truth_tableの区間の開始インデックス
    - length: truth_tableの区間の長さ
    戻り値:
    rootノードIDを返す。ノードはglobalなノード辞書に格納される。
    """
    if length is None:
        length = len(truth_table)
    # 範囲内のtruth_tableの部分を取り出す（スライスして計算してもよいがstart,lengthで処理）
    # length==1なら単一ビット ⇒ 終端ノードを作成
    if length == 1:
        v = int(truth_table[start])
        # 終端ノードはグローバルノード辞書に重複なく1つずつ作ることが多いが、ここでは後で共有化するために個別作成でも良い。
        # ただし共有化のために終端ノードは固定2つ作って辞書に持っておく方法にする。
        # よってここでは0か1の終端ノードIDを返すだけでよい。
        return leaf_nodes[v]

    # 0エッジ側の部分と1エッジ側の部分をさらに分割して再帰で構築
    half = length // 2
    zero_id = build_bdd(N, truth_table, var_index + 1, start, half)
    one_id = build_bdd(N, truth_table, var_index + 1, start + half, half)

    # 簡約化規則(a): zero_id == one_idならこの変数ノード不要なのでzero_idを返す
    if zero_id == one_id:
        return zero_id

    # 簡約化規則(b)は共有辞書で対応
    key = (var_index, zero_id, one_id)
    if key in unique_table:
        return unique_table[key]

    # 新しい変数ノードを作成して登録
    node = BDDNode('var', var_index, zero=zero_id, one=one_id)
    nodes[node.id] = node
    unique_table[key] = node.id
    return node.id

def count_var_nodes(root_id):
    """
    rootノードIDから辿って、変数ノードの個数を数える
    再帰的に訪問済み管理しながら数える。
    """
    visited = set()
    def dfs(nid):
        if nid in visited:
            return 0
        visited.add(nid)
        node = nodes[nid]
        if node.type == 'leaf':
            return 0
        cnt = 1
        cnt += dfs(node.zero)
        cnt += dfs(node.one)
        return cnt
    return dfs(root_id)

# 入力処理
def main():
    import sys
    input = sys.stdin.readline

    while True:
        line = input()
        if not line:
            break
        line = line.strip()
        if line == '':
            break
        N = int(line)
        bit_line = input().strip()

        # グローバル変数初期化
        global node_id_counter, nodes, leaf_nodes, unique_table
        node_id_counter = 0
        nodes = dict()  # ノードID -> BDDNodeオブジェクト
        unique_table = dict()  # (var_index, zero_id, one_id) -> ノードIDの共有辞書

        # 終端ノードを作成しIDを固定で持つ（ID=1が0ノード、ID=2が1ノードになるように作成）
        # 可能な限り終端の共有化に用いる。
        zero_leaf = BDDNode('leaf', 0)
        one_leaf = BDDNode('leaf', 1)
        zero_leaf.id = 1
        one_leaf.id = 2
        nodes[zero_leaf.id] = zero_leaf
        nodes[one_leaf.id] = one_leaf
        leaf_nodes = {0: zero_leaf.id, 1: one_leaf.id}
        # node_id_counterを終端ノード分に更新
        node_id_counter = 2

        # BDD構築
        root_id = build_bdd(N, bit_line)

        # ルートから辿って変数ノードの数をカウント
        ans = count_var_nodes(root_id)
        print(ans)

if __name__ == "__main__":
    main()