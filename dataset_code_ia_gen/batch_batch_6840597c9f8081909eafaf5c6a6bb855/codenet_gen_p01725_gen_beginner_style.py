import sys
sys.setrecursionlimit(10**7)

s = input()

# トークンに分解する関数
def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            num = c
            i += 1
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            tokens.append(num)
            continue
        elif c in "+-*()":
            tokens.append(c)
        i += 1
    return tokens

tokens = tokenize(s)

# 再帰下降パースでASTを構築
# ASTノードは (op, left, right) または数値(int)

pos = 0
def parse_expr():
    global pos
    if tokens[pos] == '(':
        pos += 1
        node = parse_expr()
        pos += 1  # ')'
        return node
    elif tokens[pos].isdigit() or tokens[pos][0].isdigit():
        val = int(tokens[pos])
        pos += 1
        return val
    else:
        # expr op expr
        left = parse_expr()
        if pos == len(tokens):
            return left
        if tokens[pos] in '+-*':
            op = tokens[pos]
            pos += 1
            right = parse_expr()
            return (op, left, right)
        else:
            return left

pos = 0
ast = parse_expr()

# 演算子の優先順位の割り当てを考える
# + - * の3つの演算子の優先順位は1〜3まで（同じ順位でもよい）自由に設定できる
# 全ての組み合わせを試す（3^3=27通り）
from itertools import product

ops = ['+', '-', '*']

# あるASTを優先順位priを参照して計算する関数
def eval_ast(node, pri):
    # pri: dictで、op -> 優先順位の数字（小さいほど優先度高い）
    if type(node) == int:
        return node

    # node = (op, left, right)
    op = node[0]
    left = node[1]
    right = node[2]

    # 演算子が複数ある場合、演算子の優先順位に基づいて、再帰的に分割して左結合で計算する必要がある。
    # しかしASTは1つのopで作られていて優先度は考慮されていないので、
    # ASTをもう一度優先順位に基づいて再構築する必要がある。
    # ここでは簡単化のため、一度ASTを文字式に戻し、
    # トークンに分解してから、優先順位を考慮した方法で評価する方法をとる。

    # なのでここでeval_astは使わず、文字列に戻して別関数eval_with_priorityを呼ぶ。

def to_infix(node):
    if type(node) == int:
        return str(node)
    else:
        op, left, right = node
        left_s = to_infix(left)
        right_s = to_infix(right)
        return left_s + op + right_s

expr_str = to_infix(ast)

tokens2 = tokenize(expr_str)

# 優先順位priをもとに計算する関数
def eval_with_priority(tokens, pri):
    # pri: dict op->順位（数値小さいほど優先度高い）
    # tokensは数字と演算子が交互に並ぶ（括弧なし）
    # 左結合かつ同順位の演算子は左から処理

    # 括弧はないので単純に優先度の順位順に処理していく
    # 数字はint,演算子は文字のトークンリストで計算していく
    tokens = tokens[:]
    levels = sorted(set(pri.values()))
    for level in levels:
        i = 0
        while i < len(tokens):
            if tokens[i] in ops and pri[tokens[i]] == level:
                a = int(tokens[i-1])
                b = int(tokens[i+1])
                if tokens[i] == '+':
                    res = a + b
                elif tokens[i] == '-':
                    res = a - b
                else:
                    res = a * b
                tokens = tokens[:i-1] + [str(res)] + tokens[i+2:]
                i -= 1
            else:
                i += 1
    return int(tokens[0])

max_val = -10**20

for p in product([1,2,3], repeat=3):
    pri = {}
    for i, o in enumerate(ops):
        pri[o] = p[i]
    val = eval_with_priority(tokens2, pri)
    if val > max_val:
        max_val = val

print(max_val)