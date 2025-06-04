s = input()

n = len(s)

pairs = {('(', ')'), (')', '('), ('{', '}'), ('}', '{'), ('[', ']'), (']', '['), ('i', 'i'), ('w', 'w')}
# 左右対称の条件を満たすか
def is_pair(a, b):
    return (a, b) in pairs

# dp[i][j] は s[i..j] から条件を満たす線対称な部分列の最大長
dp = [[0]*(n) for _ in range(n)]

# 部分列が "iwi" を含むかどうかの情報を持つ配列
has_iwi = [[False]*(n) for _ in range(n)]

for length in range(1, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        sub = s[i:j+1]
        # まず部分列 s[i..j] に "iwi" が含まれているか判定
        # 部分列の文字列 (連続部分ではない) で "iwi" を含むかは判定が難しいので
        # ここでは部分文字列自身（連続部分）に "iwi" があるかだけで判定し、部分列判定は後で総合的に行う手法をとる
        # よってここは単純に s[i..j] に "iwi" の連続があるかチェック
        if "iwi" in sub:
            has_iwi[i][j] = True
        else:
            # 長さ1ならFalse、そのほかはDPの遷移により決定するため一旦Falseにしておく
            has_iwi[i][j] = False

        if length == 1:
            # 長さ1の文字は "i" または "w" または括弧だが
            # 問題のルールで中身が 'i' または 'w' のみなら左右対称は i, w, 空文字列なので、
            # 括弧単独は左右対称ではない(条件で定義されていないものはNG)
            # したがって、単一文字で左右対称なのは 'i' と 'w' のみ
            if s[i] == 'i' or s[i] == 'w':
                dp[i][j] = 1
            else:
                dp[i][j] = 0
        else:
            # いろいろ試す
            # ① 両端を対応する左右対称な括弧や i,w で挟んで内部が線対称ならOK
            if is_pair(s[i], s[j]):
                inside_len = dp[i+1][j-1] if i+1 <= j-1 else 0
                inside_has_iwi = has_iwi[i+1][j-1] if i+1 <= j-1 else False
                # 間の部分列が線対称で、かつ "iwi" を含むか
                # 外側に i or w がつくなら"iwi"の部分は中に残る、括弧の場合は "iwi" は内部にある必要あり
                if inside_len > 0 or (j - i + 1 <= 3 and sub == "iwi"):
                    # この文字列が 'iwi' を含むか更新する
                    has_iwi[i][j] = has_iwi[i][j] or inside_has_iwi or (sub == "iwi")
                    if has_iwi[i][j]:
                        dp[i][j] = max(dp[i][j], inside_len + 2)
                    else:
                        # 'iwi' 含まないなら長さにはならない条件
                        dp[i][j] = max(dp[i][j], 0)
            # ② 左端と右端を使わない場合の遷移
            for k in range(i, j):
                # 組み合わせで最大値を更新
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])
                has_iwi[i][j] = has_iwi[i][j] or (has_iwi[i][k] or has_iwi[k+1][j])

            # もし s[i..j] 自身に "iwi" 文字列があれば、部分列で3文字の "iwi" は成立するので長さ3以上反映
            if sub == "iwi":
                has_iwi[i][j] = True
                dp[i][j] = max(dp[i][j], 3)

# dp[0][n-1] は s全体から作れる最大の対象文字列長だが
# ただし "iwi" を含む部分列として、条件に合わせてdp計算時に判定して更新したのでこのままで良い
print(dp[0][n-1])