import sys
import re

sys.setrecursionlimit(10**7)

# 有限体の有限体電卓を実装する
# 演算はすべて mod p で行う
# 除算は逆数を求めることで実装する
# 逆数はフェルマーの小定理より x^(p-2) mod p で求める

# 優先度を定義
priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

def pow_mod(base, exp, mod):
    # base^exp % mod の高速累乗
    result = 1
    cur = base % mod
    e = exp
    while e > 0:
        if e & 1:
            result = (result * cur) % mod
        cur = (cur * cur) % mod
        e >>= 1
    return result

def inverse_mod(x, p):
    # フェルマーの小定理により逆元を計算
    # 0 の逆数は存在しないので呼ぶ前にチェック必要
    return pow_mod(x, p-2, p)

def tokenize(exp, p):
    # expをトークンに分割する
    # 数字、演算子、カッコ、空白区切りで区切られている可能性があるが、
    # 2つ以上の空白でもOKなので、正規表現で数値と記号を抜き出す
    # 数字は0〜p-1の範囲である保証はないが後でmod pで値を整えるのでOK
    # トークンの区切りは空白または記号で分ける
    pattern = r'\d+|[+\-*/()]'
    tokens = re.findall(pattern, exp)
    return tokens

def to_postfix(tokens):
    # 中置記法のトークン列を後置記法(RPN)に変換
    stack = []
    output = []
    for t in tokens:
        if t.isdigit():
            output.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # '('をポップ
        else:
            # 演算子
            while stack and stack[-1] != '(' and priority.get(stack[-1], 0) >= priority[t]:
                output.append(stack.pop())
            stack.append(t)
    while stack:
        output.append(stack.pop())
    return output

def eval_rpn(postfix, p):
    # 後置記法の式を評価する
    # 逆数が存在しなければ None を返す (NGの場合)
    stack = []
    for t in postfix:
        if t.isdigit():
            # 数字は mod p で値を確定
            val = int(t) % p
            stack.append(val)
        else:
            # 演算子は2つの値を取り出す
            if len(stack) < 2:
                return None
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                res = (a + b) % p
            elif t == '-':
                res = (a - b) % p
            elif t == '*':
                res = (a * b) % p
            elif t == '/':
                # bの逆数を求める
                if b == 0:
                    return None
                invb = inverse_mod(b, p)
                res = (a * invb) % p
            else:
                return None
            stack.append(res)
    if len(stack) != 1:
        return None
    return stack[0]

def format_exp_no_space(exp):
    # 問題の指定に従い、expの数値、演算子、カッコの前後の空白を除去する
    # ただし「= val (mod p)」の「=」「val」「(」「mod」「p」前後には空白を入れる
    # 具体的にはトークンを連結して中間に空白を入れないだけの処理
    # expは元の式文字列
    # トークンが number or operator, or paren
    # 空白を削除しトークンを繋ぐ
    tokens = tokenize(exp, 2)  # pは使わないここでは
    return ''.join(tokens)

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == '0:':
            break
        # 入力は p:exp の形式で与えられる
        m = re.match(r'^(\d+):\s*(.*)$', line)
        if not m:
            # 入力例外は問題にない想定
            continue
        p = int(m.group(1))
        exp = m.group(2)
        # トークナイズ
        tokens = tokenize(exp, p)
        # 後置記法に変換
        postfix = to_postfix(tokens)
        # 評価
        val = eval_rpn(postfix, p)
        if val is None:
            # NGの場合
            print('NG')
            continue
        # フォーマット出力
        no_space_exp = format_exp_no_space(exp)
        print(f'{no_space_exp} = {val} (mod {p})')

if __name__ == '__main__':
    main()