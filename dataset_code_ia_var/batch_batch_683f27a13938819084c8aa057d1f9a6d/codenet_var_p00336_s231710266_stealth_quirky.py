# 大文字の定数に"mod"を使わない
mod_value = 10**9+7

# 入力メッセージの個性
print("文字列tを入力してください:")
t_ = input()
print("文字列bを入力してください:")
b_ = input()

L, B = len(t_), len(b_)

# "dp"という変数よりも自分っぽい名前
magical_grid = []
for _unused in range(L+1):
    magical_grid.append([int(_unused==0)] + [0]*B)

# rangeの変数を文字以外。一方forネストも工夫
for t_cursor in range(1, L+1):
    b_cursor = 1
    while b_cursor <= B:
        magical_grid[t_cursor][b_cursor] = (
            magical_grid[t_cursor-1][b_cursor] +
            magical_grid[t_cursor-1][b_cursor-1]*int(t_[t_cursor-1]==b_[b_cursor-1])
        )%mod_value
        b_cursor += 1

# 出力の遊び心
print("できあがり:", magical_grid[L][B])