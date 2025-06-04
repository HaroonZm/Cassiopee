h, w, n = map(int, input().split())
removed = set()
for _ in range(n):
    a, b = map(int, input().split())
    removed.add((a, b))

# 初めはすべての場所に横棒がある (a ≡ b mod 2)
# 横棒がある場所は (a, b) (1<=a<=h, 1<=b<=w-1) で a % 2 == b % 2
# 除外された横棒は removed にある
# なので通る横棒は (a,b) で a%2==b%2 かつ (a,b) not in removed

# 横棒は上下に繋がる縦棒の交換を表す
# 縦棒の位置を1からwとして考え、上から下に移動し横棒があれば隣の縦棒と交換を行う

pos = list(range(1, w+1))
for a in range(1, h+1):
    for b in range(1, w):
        if (a % 2 == b % 2) and ((a, b) not in removed):
            # pos[b-1] と pos[b] を交換
            pos[b-1], pos[b] = pos[b], pos[b-1]

# pos[i]は上端のi+1番目の縦棒が下端でどの位置になるかを示す
# 出力は上端のi番目の縦棒が下端で何番目かなので、posから逆のマップを作る
answer = [0]*w
for i in range(w):
    answer[pos[i]-1] = i+1

for x in answer:
    print(x)