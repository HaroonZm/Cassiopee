H, W = map(int, input().split())
S = [input().split() for _ in range(H)]

positions = ((i, j) for i, row in enumerate(S) for j, val in enumerate(row) if val == 'snuke')
i, j = next(positions)
print(f"{chr(65 + j)}{i + 1}")