import re
import math

def parse_polynomial(S):
    # 入力の多項式を項ごとに分けて符号も分ける
    # 正負を検出しながら項を抽出するため、項の間に空白を入れたりはしない
    # 項の形: [+|-]?(係数)?x^(指数), [+|-]?(係数)?x, [+|-]?定数
    terms = []
    pos = 0
    while pos < len(S):
        if pos == 0:
            # 最初の項は符号がなくても可
            if S[pos] in '+-':
                sign = S[pos]
                pos += 1
            else:
                sign = '+'
        else:
            sign = S[pos]
            pos += 1
        # 次の+か-までを項として切り出す
        start = pos
        while pos < len(S) and S[pos] not in '+-':
            pos += 1
        term_str = sign + S[start:pos]
        terms.append(term_str)
    # 項ごとに (次数, 係数) のタプルを作る
    result = []
    for term in terms:
        # termは例: '+3x^4', '-x^3', '+2x', '-1'
        m = re.fullmatch(r'([+-])(?:(\d+)?x(?:\^([2-5]))?|(\d+))', term)
        if not m:
            # 係数が省略されているxも判別するため別途処理
            # xのみ、+x, -xのときにマッチしない場合
            m2 = re.fullmatch(r'([+-])x(?:\^([2-5]))?', term)
            if m2:
                sign2, exp2 = m2.group(1), m2.group(2)
                coef = 1 if sign2 == '+' else -1
                exp = int(exp2) if exp2 else 1
                result.append((exp, coef))
            else:
                # それ以外の例: +4 のみ
                m3 = re.fullmatch(r'([+-])(\d+)', term)
                if m3:
                    sign3, val3 = m3.group(1), m3.group(2)
                    coef = int(val3)
                    if sign3 == '-':
                        coef = -coef
                    result.append((0, coef))
                else:
                    raise ValueError('parse error: ' + term)
        else:
            sign1 = m.group(1)
            coef_str = m.group(2)
            exp_str = m.group(3)
            const_str = m.group(4)
            if const_str is not None:
                # 定数項
                coef = int(const_str)
                if sign1 == '-':
                    coef = -coef
                result.append((0, coef))
            else:
                # xの項
                exp = int(exp_str) if exp_str else 1
                coef = int(coef_str) if coef_str else 1
                if sign1 == '-':
                    coef = -coef
                result.append((exp, coef))
    # 塔辞降順になっているためそのままでよい
    return result

def solve():
    S = input()
    terms = parse_polynomial(S)
    # terms = [(次数, 係数), ...], 最大次数はn、最大次数の係数は1
    # 多項式は (x+r1)(x+r2)...(x+rn)の形に因数分解可能で、r_iは定数項（0でない整数）

    # 多項式の次数取得
    max_exp = terms[0][0]
    # 項数 = max_exp + 1 と思われる
    n = max_exp

    # 係数リストを指数降順に並べる
    coef_list = [0]*(n+1)
    for exp, c in terms:
        coef_list[n-exp] = c
    # coef_list は　高次から低次までの係数リスト
    # 例: n=2なら coef_list[0] x^2 + coef_list[1] x + coef_list[2]

    # 定数項積 = 定数項の係数 (0次の項)
    const_term = coef_list[-1]

    # 定数項は0でない相異なる整数
    abs_const = abs(const_term)

    # (x+r1)(x+r2)...(x+rn) の形だと r_i の積は定数項, 和は -coef_list[1] / coef_list[0] ,など
    # すべての r_i を探す必要があるが、
    # 各 r_i は divisor(const_term) の中の一つで、相異なる整数

    # まずは一次式の数 = n

    # r_i の候補: 定数項の約数の正負両方
    def divisors(x):
        x = abs(x)
        res = set()
        for i in range(1,int(math.isqrt(x))+1):
            if x % i == 0:
                res.add(i)
                res.add(x//i)
        return res

    cand_roots = list(divisors(const_term))
    cand_vals = []
    for v in cand_roots:
        cand_vals.append(v)
        cand_vals.append(-v)

    # 全ての相異なるn個の組み合わせを試して、因数分解できるかチェックするのは計算量的に多いが n<=5で十分可能

    from itertools import combinations

    # ただし、組み合わせではなく順列で繰り返しやると計算が多いので
    # n個の異なる値の順列全列挙は多いので
    # ここでは combinations で探索し、判定も順序未定でよい候補なら対応できる

    # 項の係数が全部合致するか判定
    def check_roots(roots):
        # roots = [r1,...,rn]
        # 多項式の係数は coef_list
        # 係数を計算する、多項式は ∏(x + r_i) として展開
        # 順序はバラバラでも和や積で再現されるため、積の多項式を計算
        # 多項式計算を再帰で実装
        poly = [1] # 初期多項式 1

        for r in roots:
            # (x + r) と polyの乗算
            new_poly = [0]*(len(poly)+1)
            for i in range(len(poly)):
                new_poly[i] += poly[i]   # x * poly  の次数シフト
            for i in range(len(poly)):
                new_poly[i+1] += poly[i]  # ここは x^i -> x^{i+1}
            # 上2行は勘違いしてるので修正: (x+r) * poly:
            new_poly = [0]*(len(poly)+1)
            for i in range(len(poly)):
                new_poly[i] += poly[i]*r
            for i in range(len(poly)):
                new_poly[i+1] += poly[i]
            poly = new_poly

        # polyは次数昇順順なので coef_list と比べるため反転させる
        poly_rev = poly[::-1]
        if len(poly_rev) != len(coef_list):
            return False
        for a,b in zip(poly_rev, coef_list):
            if abs(a-b) > 1e-9:
                return False
        return True

    # 候補のn個のセットを生成しチェック
    # rootsは定数項の異なる整数である必要あり
    found_roots = None
    from itertools import permutations

    cand_vals_set = set(cand_vals)
    # n <= 5 で domesticなので組み合わせを深く列挙可
    # ただし順序は複数あるが、先に組み合わせで確認し、
    # 見つかったらそれで良い

    for comb in combinations(cand_vals_set, n):
        if len(set(comb)) != n:
            continue
        # rootsは相異なる整数
        # 積を計算して coef_list に一致するかチェック
        # 順序は任意だが、多項式は並び換えても結果は同じなので組み合わせだけチェックすれば良い
        if check_roots(comb):
            found_roots = comb
            break

    # 定数項の小さい順に並べて出力 (絶対値は条件にないので符号込みの比較)
    found_roots = sorted(found_roots)

    # 出力は (x+r1)(x+r2)...
    # r_i が負なら (x-r_i') の形で出力
    res = []
    for r in found_roots:
        if r >= 0:
            res.append(f'(x+{r})')
        else:
            res.append(f'(x{r})')  # 例えば r = -2 => (x-2)
    print(''.join(res))

if __name__ == '__main__':
    solve()