import sys
sys.setrecursionlimit(10**7)

# 問題概要：
# 与えられた論理式は ?, 0, 1, &, |, () から構成される。
# ? は未確定の値であり、その ? を 0 or 1 に確定しなければならない場合がある。
# 左から読み進め、ある ? を 0 or 1 にしても結果が変わらなければ操作不要。
# 結果が変わる可能性があれば1円払って 0 or 1 に決める。
# 評価結果を 0 に確定させる場合と 1 に確定させる場合、支払う最小金額を求める。

# ポイント：
# 短絡評価(ショートサーキット)を考慮し、? の値によって論理和・論理積の結果が変わるかどうかを判断する。
# 木構造にパースして、各ノードで (0にしたい場合の最小コスト, 1にしたい場合の最小コスト) を計算する。

# アプローチ：
# 1. 字句解析と再帰下降パーサで抽象構文木(AST)を作成する。
# 2. ASTの各ノードに対して、評価結果が0か1に確定するためのコストを再帰的に計算。
# 3. ?ノードは0 か 1 に固定するコストは1、固定しないなら0（固定せず結果が確定しなければペナルティは大きいが問題の定義上そんなケースはない）。
# 4. & や | ノードは左右の子ノードからのコストを元に、式全体として0または1を確定させる最小コストを計算。
# 5. 最終的にAST全体のコスト(0に確定させる最小コスト, 1に確定させる最小コスト)を出力。

# ASTノード定義
class Node:
    def __init__(self, kind, left=None, right=None, val=None, pos=None):
        # kind: 'or', 'and', 'term'
        # left, right: 子ノード
        # val: '?', '0', '1' (termノード)
        self.kind = kind
        self.left = left
        self.right = right
        self.val = val
        self.pos = pos  # '?'の位置(左からの番号)を保持

# 字句解析器
class Lexer:
    def __init__(self, s):
        self.s = s
        self.i = 0
        self.n = len(s)

    def peek(self):
        if self.i >= self.n:
            return None
        return self.s[self.i]

    def next(self):
        if self.i >= self.n:
            return None
        c = self.s[self.i]
        self.i += 1
        return c


# パーサ
class Parser:
    def __init__(self, s):
        self.lexer = Lexer(s)
        self.qpos = 0  # ?の左からの通し番号

    # <formula> ::= <or-expr>
    def formula(self):
        return self.or_expr()

    # <or-expr> ::= <and-expr> | <or-expr> "|" <and-expr>
    def or_expr(self):
        node = self.and_expr()
        while True:
            c = self.lexer.peek()
            if c == '|':
                self.lexer.next()
                right = self.and_expr()
                node = Node('or', left=node, right=right)
            else:
                break
        return node

    # <and-expr> ::= <term> | <and-expr> "&" <term>
    def and_expr(self):
        node = self.term()
        while True:
            c = self.lexer.peek()
            if c == '&':
                self.lexer.next()
                right = self.term()
                node = Node('and', left=node, right=right)
            else:
                break
        return node

    # <term> ::= "(" <or-expr> ")" | "?"
    # または '0'や'1'も出てくる場合も念のため対応（問題文では0,1は入力式に明記されていないが、安全のため）
    def term(self):
        c = self.lexer.peek()
        if c == '(':
            self.lexer.next()
            node = self.or_expr()
            if self.lexer.next() != ')':
                raise Exception("')' expected")
            return node
        elif c == '?':
            self.lexer.next()
            # ? は左から何番目かの番号を付与
            self.qpos += 1
            return Node('term', val='?', pos=self.qpos)
        elif c == '0' or c == '1':
            self.lexer.next()
            return Node('term', val=c)
        else:
            raise Exception(f"Unexpected char {c}")

# 最小コスト計算部
# 返す値は (cost_when_result_0, cost_when_result_1) のタプル
def min_cost(node):
    # ノードがtermの場合
    if node.kind == 'term':
        if node.val == '?':
            # ? を固定しなければ結果確定しないので基本はコストゼロで確定できないと考えるが、
            # 問題では ? を固定しないと不確定な場合は払う必要あり。
            # 0に確定したいなら ? を0に固定してコスト1、もしくは1に固定してコスト1
            # 固定しなければ結果不確定なのでコストは無限大
            # ここでそれぞれ、0にしたいなら1円払って0固定、1にしたいなら1円払って1固定
            # 固定しなくても良い場合は0（その場合は左右の評価で判断される）
            # ここでは、コストは固定する方が1、それ以外は大きな値を返す。
            INF = 10**15
            # 0に確定したい場合：?を0に固定でコスト1
            cost0 = 1
            # 1に確定したい場合：?を1に固定でコスト1
            cost1 = 1
            return (cost0, cost1)
        elif node.val == '0':
            # 0の値は確定なのでコスト0
            return (0, 10**15)
        elif node.val == '1':
            # 1の値は確定なのでコスト0
            return (10**15, 0)
        else:
            raise Exception("term val invalid")
    elif node.kind == 'and':
        # & の左と右のノードを計算
        left0, left1 = min_cost(node.left)
        right0, right1 = min_cost(node.right)
        # (a & b) == 0 となるための最小コスト
        # 結果が0になるのはaが0 or bが0
        # つまり (a&b) == 0 を確定するためには次のうち最小コストを採る：
        # - aが0で確定 ＋ bは何でもOK(0 or 1)
        # - bが0で確定 ＋ aは何でもOK(0 or 1)
        # → 左が0、右が0どちらかの組み合わせの最小コストを取る
        cost0 = min(left0 + min(right0, right1), right0 + min(left0, left1))

        # (a & b) == 1 の場合、両方が1で確定しなければならない
        cost1 = left1 + right1

        return (cost0, cost1)
    elif node.kind == 'or':
        # | の左と右のノードを計算
        left0, left1 = min_cost(node.left)
        right0, right1 = min_cost(node.right)
        # (a | b) == 0 場合、
        # 両方が0で確定しなければならない
        cost0 = left0 + right0

        # (a | b) == 1 の場合、
        # 左が1 or 右が1 どちらかでよい
        cost1 = min(left1 + min(right0, right1), right1 + min(left0, left1))

        return (cost0, cost1)
    else:
        raise Exception("unknown node kind")


# メイン処理
def main():
    s = sys.stdin.readline().strip()
    parser = Parser(s)
    root = parser.formula()

    # 現状の?の数
    # 0や1が現れない制約に従って動くが、もしかすると?の数は0かもしれない
    # ?の数は parser.qpos でわかる

    cost0, cost1 = min_cost(root)
    print(cost0, cost1)

if __name__ == "__main__":
    main()