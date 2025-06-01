h, w = map(int, input().split())
squares = []
for _ in range(h):
    row = input()
    squares.append(list(row))

answer = 0
h_counts = [0] * w

for i in range(h - 1, -1, -1):
    o_count = 0
    for j in range(w - 1, -1, -1):
        if squares[i][j] == 'I':
            h_counts[j] += 1
        elif squares[i][j] == 'O':
            o_count += 1
        else:
            answer += h_counts[j] * o_count

print(answer)