import sys

# この２行は
#   a   1 0 1 0
#   b   1 1 0 0
# こうしても、作れる集合の内訳が変わらない
#   a   1 0 1 0
#   b^a 0 1 1 0
# {両方未選択, 上だけ選択, 下だけ選択, 両方選択}: {φ, a, b, a^b} == {φ, a, b^a, b}
# これは列方向に対しても同じことなので、掃き出し法チックなことをして
#   1 0 ... 0 0 0
#   0 1 ... 0 0 0
#   : :     : : :
#   0 0 ... 1 0 0
#   0 0 ... 0 0 0
# こんな形にできる
# ここで、行の選び方で'1'のある行を1つでも含むような選び方は、
# その'1'の場所の列(どれでもいいので1つ)を選択するかしないかで、
# 全体の和が偶数, 奇数となるパターンがちょうど半分ずつとなる。
# よって、以下が答え
# (行の全体の選び方 - '1'のある行を１つも含めない選び方) * 列の全体の選び方 / 2

n, m = map(int, input().split())
MOD = 998244353
rows = []
for line in sys.stdin:
    b = ''.join(line.rstrip().split())
    rows.append(int(b, base=2))

independent_row = 0
while rows:
    x = max(rows)
    if x == 0:
        break
    independent_row += 1
    y = 1 << (x.bit_length() - 1)
    rows = [r ^ x if r & y else r for r in rows if r != x]

ans = (pow(2, n + m - 1, MOD) - pow(2, n + m - independent_row - 1, MOD)) % MOD
print(ans)