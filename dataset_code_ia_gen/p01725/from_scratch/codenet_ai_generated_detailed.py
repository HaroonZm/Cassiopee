import sys

sys.setrecursionlimit(10**7)

# まず入力の数式文字列をトークンに分解するための関数を作成する。
# トークンは数値（整数）、演算子('+','-','*')、括弧('(','')')のいずれかとなる。
def tokenize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isdigit():
            # 連続する数字をまとめて一つの整数トークンにする
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            tokens.append(int(expr[i:j]))
            i = j
        else:
            tokens.append(c)
            i += 1
    return tokens

# 次にトークン列から構文木（AST）を生成するパーサを書く。
# BNFのルールに従い、expr := (expr) | number | expr op expr となっているが、
# 再帰下降パーサで実装していく。
# ここでは括弧優先で、まず括弧の囲みを再帰的に処理し、最終的にノードを得る。
# ノードは dict の形で { "type": "num", "value": int } または
# { "type": "op", "op": '+|-|*', "left": node, "right": node } とする。

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected=None):
        current = self.peek()
        if expected and current != expected:
            raise ValueError(f"Expected {expected}, got {current}")
        self.pos += 1
        return current

    # expr のパース
    # 構文の形は
    # expr := term { op term }*
    # term := number | '(' expr ')'
    # と再帰的に処理
    # ここでは素直にパースして左右左右と処理し、ASTの形で返す
    def parse_expr(self):
        node = self.parse_term()
        while True:
            op = self.peek()
            if op in ('+', '-', '*'):
                self.consume()
                right = self.parse_term()
                node = {"type": "op", "op": op, "left": node, "right": right}
            else:
                break
        return node

    def parse_term(self):
        t = self.peek()
        if t == '(':
            self.consume('(')
            node = self.parse_expr()
            self.consume(')')
            return node
        elif isinstance(t, int):
            self.consume()
            return {"type": "num", "value": t}
        else:
            raise ValueError(f"Unexpected token: {t}")

# 次にこのASTを使って、演算子の優先順位を任意に設定して式を評価する関数を作る。
# 演算子は左結合であり、同じ優先度の演算は左から順に計算する必要がある。
# (同じ優先順位の演算子群に混じってもよい)
#
# 操作：
# 優先度は3つの演算子それぞれに0~2の整数を割り当てる。
# 優先度が高い演算子から順に計算していく。
# 例えば優先度が {'+':2, '-':2, '*':0} → '+'と'-'が最高優先度、'*'が最低
#
# 実装の方針としては、
# ASTに対して「演算子の優先度付きの評価」関数を定義し、
# ノードを木の形で辿りながら優先度に従って計算をしていく。
#
# しかし通常の再帰的評価は演算子の優先度を動的に考慮できないので、
# 以下のように処理する：
# 1. 最優先度の演算子をすべて計算して木を縮約する。
# 2. 次に2番目の優先度の演算子を計算して木を縮約する。
# 3. 最後に残った演算子を計算して1つの数値にする。
#
# そのためには演算子の優先度毎に分けて順に計算を行う
# ASTの構造を保ったままだと面倒なので、ASTを「トークン列」に戻す関数を用意し、
# 優先度レベルごとに左から演算子を評価し、縮約していく方式を取る。

def ast_to_tokens(node):
    # ASTを中置トークン列に戻す（括弧なし）
    # 中置表現で括弧はなし（構造が木なので優先度調整のため）
    # 例えば node = 3-2*3 のASTは ['3','-','2','*','3'] になる。
    if node["type"] == "num":
        return [node["value"]]
    else:
        left = ast_to_tokens(node["left"])
        right = ast_to_tokens(node["right"])
        return left + [node["op"]] + right

# 演算子の優先度に基づき、トークン列を複数回に分けて処理する。
# トークン列の形は以下の制約：
# 数値と演算子が交互に並ぶリスト。例: [3, '-', 2, '*', 3]
#
# 処理方法:
# 優先度の高い演算子から順に、左から右に演算子をスキャンし、
# 優先度が今回の段階で処理すべきオペレータなら計算して数値を更新し、
# トークン列を縮約していく。
#
# 例えば
# トークン列 = [3, '-', 2, '*', 3]
# 優先度 = {'+':1,'-':2,'*':0}
# なら最高優先度は '-' (2), 次に '+', 最後に '*'
# なので '−' を左から順に計算して縮約し、次に '+' で、最後に '*'
#
# ただし同じ優先度はまとめて処理し、順序は左結合になるようにする。
#
# 便宜上、優先度の順番を決める際、同じ優先度の演算子は同時に扱う。

def evaluate_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError(f"Unknown operator: {op}")

def eval_tokens_with_priority(tokens, ops_to_eval):
    # ops_to_eval: 今回評価する演算子の集合
    # 入力tokensは数値と演算子の交互のリスト
    # 左端から読みながら、演算子がops_to_evalに入ってたら計算を行い縮約
    stack = []
    stack.append(tokens[0])  # 最初の数値を入れる

    i = 1
    while i < len(tokens):
        op = tokens[i]
        val = tokens[i+1]

        if op in ops_to_eval:
            # 最後にpushされてる数値と今回のvalを計算して、数値としてstackに置き換える
            a = stack.pop()
            res = evaluate_op(a, val, op)
            stack.append(res)
        else:
            # 今回はまだ計算しない演算子なので、そのまま追加していく
            stack.append(op)
            stack.append(val)

        i += 2

    return stack

# 最後に、優先度のすべての割り当ての組み合わせ（0~2を+,-,*に割り当てる）
# の中で最大の結果を求める。
# 優先度は3つの演算子に[0,1,2]の値を割り当てる。0は最低、2は最高の優先度。
# 同じ優先度でもよいので全パターンは3^3 = 27通り。
#
# それぞれの優先度割り当てで、
# 優先度の高い順（2->1->0の順）に演算を適用する。
# 同じ優先度の演算子は一度にまとめて処理する。

def main():
    expr = sys.stdin.readline().rstrip('\n')

    tokens = tokenize(expr)

    parser = Parser(tokens)
    ast = parser.parse_expr()

    # ASTをトークン列に変換
    tokens = ast_to_tokens(ast)

    # 全優先度割り当て(0~2)を全探索(27通り)
    ops = ['+', '-', '*']
    max_result = -10**20

    from itertools import product

    for prios in product([0,1,2], repeat=3):
        priority = {op: p for op, p in zip(ops, prios)}

        # 優先度の種類を高い順に重複除去しソート
        levels = sorted(set(priority.values()), reverse=True)

        current_tokens = tokens[:]
        # 優先度の高い順で演算を適用
        for level in levels:
            ops_to_eval = [op for op in ops if priority[op] == level]
            current_tokens = eval_tokens_with_priority(current_tokens, set(ops_to_eval))

        # 演算後は current_tokens は数値一つだけのはず
        assert len(current_tokens) == 1 and isinstance(current_tokens[0], int)

        res = current_tokens[0]
        if res > max_result:
            max_result = res

    print(max_result)

if __name__ == '__main__':
    main()