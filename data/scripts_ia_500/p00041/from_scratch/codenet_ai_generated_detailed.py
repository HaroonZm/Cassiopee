import sys
import itertools

# このプログラムの目的：
# 入力された4つの整数を使い、 +, -, * の3つの演算子と括弧を使って結果が10となる式を見つける。
# 条件：
# - 4つの整数を順番を変えてすべて使う。
# - 演算子は +, -, * のみを3回使う。
# - 括弧は最大3組（= 6個）以下で使用可。
# - 複数解があれば最初に見つかった1つのみ出力。
# - 解がなければ0を出力。
# - 入力は複数セットで0 0 0 0で終了。

# 方針：
# 1. 4つの数の順列を全て列挙。
# 2. 演算子の組み合わせは3つのスロットに'+', '-', '*'を全パターン試す。
# 3. 可能な括弧の付け方を全パターン試す。
# 4. 各パターンで計算結果を求め、結果が10ならその式を出力。
# 5. 見つからなければ0を出力。

# 括弧の付け方について考える：
# 式は4つの数a,b,c,dから3回の演算を行うので、
# 式の構造は二分木で表現できるものは限定される。
# 4つの数字なので5通りの結合法(二分木の組み合わせ)がある。

# 具体的な括弧のつけ方パターン（式の構造）：
# フォーマットはオペランドに番号を振ると以下の5パターンとなる。
# (注)ここでの数字は数値のインデックスとして参照。
# (0), (1), (2), (3) は入力された数字の順列の配列の位置となる。

# 1. ((a op b) op c) op d
# 2. (a op (b op c)) op d
# 3. (a op b) op (c op d)
# 4. a op ((b op c) op d)
# 5. a op (b op (c op d))

# これらのパターン全てに対し、演算子の割当てを全て試すことで全組み合わせを網羅する。

# 注意点：
# - 計算は整数のみ。(割り算無しなので)
# - 減算は非可換なので順番を大切にする。
# - 長さ制限1024文字以内であることは問題ないと思われる（念のためチェック）。
# - 計算は例外処理不要（除算無しなので0除算はなし）。

# 演算子の適用を関数化
def apply_op(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    else:  # '*'
        return x * y

# 式の形ごとの評価と文字列構築を関数化
# argsは数字のリスト、opsは3つの演算子リスト
def try_patterns(nums, ops):
    a,b,c,d = nums
    op1, op2, op3 = ops

    # 1. ((a op b) op c) op d
    try:
        val1 = apply_op(apply_op(apply_op(a,b,op1), c, op2), d, op3)
        expr1 = f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"
        if val1 == 10:
            return expr1
    except:
        pass

    # 2. (a op (b op c)) op d
    try:
        val2 = apply_op(apply_op(a, apply_op(b, c, op2), op1), d, op3)
        expr2 = f"({a} {op1} ({b} {op2} {c})) {op3} {d}"
        if val2 == 10:
            return expr2
    except:
        pass

    # 3. (a op b) op (c op d)
    try:
        val3 = apply_op(apply_op(a,b,op1), apply_op(c,d,op3), op2)
        expr3 = f"({a} {op1} {b}) {op2} ({c} {op3} {d})"
        if val3 == 10:
            return expr3
    except:
        pass

    # 4. a op ((b op c) op d)
    try:
        val4 = apply_op(a, apply_op(apply_op(b,c,op2), d, op3), op1)
        expr4 = f"{a} {op1} (({b} {op2} {c}) {op3} {d})"
        if val4 == 10:
            return expr4
    except:
        pass

    # 5. a op (b op (c op d))
    try:
        val5 = apply_op(a, apply_op(b, apply_op(c,d,op3), op2), op1)
        expr5 = f"{a} {op1} ({b} {op2} ({c} {op3} {d}))"
        if val5 == 10:
            return expr5
    except:
        pass

    return None

def main():
    operators = ['+', '-', '*']
    # 入力を読み込み
    for line in sys.stdin:
        # 4つの整数を分割
        parts = line.strip().split()
        if len(parts) < 4:
            continue
        a,b,c,d = map(int, parts)
        # 終了条件
        if a == 0 and b == 0 and c == 0 and d == 0:
            break

        found = False
        # 4つの数の順列を全パターン取得
        for nums in itertools.permutations([a,b,c,d], 4):
            # 3つの演算子の組み合わせを全探索
            for ops in itertools.product(operators, repeat=3):
                expr = try_patterns(nums, ops)
                if expr is not None:
                    # 括弧の数は3組(6個)以下。チェックし問題なければ出力。
                    if expr.count('(') <= 6 and len(expr) <= 1024:
                        # 見つかった式を()を追加して見映えを良くする（問題例に倣う）
                        # 問題例は全体をカッコで囲む形式だったのでそうする（任意）
                        print(f"({expr})")
                        found = True
                        break
            if found:
                break
        if not found:
            print(0)

if __name__ == '__main__':
    main()