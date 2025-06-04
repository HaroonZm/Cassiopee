score = 0

while True:
    h = int(input())
    if h == 0:
        break
    w = 5

    field = []
    for _ in range(h):
        row = list(map(int, input().split()))
        field.append(row)

    def delete(field):
        changed = False
        global score
        for row in field:
            start = -1
            count = 1
            for i in range(1, w):
                if row[i] == row[i - 1]:
                    if count == 1:
                        start = i - 1
                    count += 1
                else:
                    if count >= 3 and row[i - 1] is not None:
                        for j in range(start, start + count):
                            row[j] = None
                        score += count * row[start]
                        changed = True
                    count = 1
            if count >= 3 and row[w - 1] is not None:
                for j in range(start, start + count):
                    row[j] = None
                score += count * row[start]
                changed = True
        return changed

    def drop(field):
        for col in range(w):
            stack = []
            for row in range(h):
                if field[row][col] is not None:
                    stack.append(field[row][col])
            for row in range(h - 1, -1, -1):
                if stack:
                    field[row][col] = stack.pop()
                else:
                    field[row][col] = None

    while True:
        changed = delete(field)
        if not changed:
            break
        drop(field)
    print(score)