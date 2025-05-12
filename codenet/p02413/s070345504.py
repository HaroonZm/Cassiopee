r, c = [int(i) for i in input().split()]
table = [list(map(int, input().split())) for _ in range(r)]
for row in table:
    row.append(sum(row))
table.append([sum(column) for column in zip(*table)])
for row in table:
    print(*row)