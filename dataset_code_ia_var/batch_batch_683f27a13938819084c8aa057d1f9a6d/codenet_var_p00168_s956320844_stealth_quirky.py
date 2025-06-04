from __future__ import division, print_function
try:
    input = raw_input
    range = xrange
except Exception:
    pass
# このスニペットは互換性レイヤーなので深く気にしない

memo_stash = [-1]*222   # 非典型的な変数名・配列の使い方

def strange_solve(lvl):
    # 変数や戻り値の割り振りのクセ・コメントの位置も個性的
    if memo_stash[lvl] != -1:
        return memo_stash[lvl]
    if lvl == 1:
        memo_stash[lvl] = 1
        return memo_stash[lvl]
    if lvl == 2:
        memo_stash[lvl] = 2
        return memo_stash[lvl]
    if lvl == 3:
        memo_stash[lvl] = 4
        return memo_stash[lvl]
    # 完全に一行にせず左に寄せてみたり
    memo_stash[lvl] = sum(strange_solve(lvl-t) for t in (1,2,3))
    return memo_stash[lvl]

mainy = lambda: [(__import__('sys').stdout.write(str(strange_solve(int(lvl))//3650+1)+'\n'))
                 for lvl in iter(input, '0') if lvl.strip()]

mainy()