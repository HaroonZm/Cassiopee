h_w = input().split()
H = int(h_w[0])
W = int(h_w[1])
N = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

tiles = []
for i in range(N):
    for j in range(a[i]):
        tiles.append(i+1)

row_start = 0
reverse_row = False
for i in range(H):
    row = []
    for j in range(W):
        row.append(tiles[row_start + j])
    if reverse_row:
        row = row[::-1]
    for num in row:
        print(num, end=' ')
    print()
    row_start += W
    reverse_row = not reverse_row