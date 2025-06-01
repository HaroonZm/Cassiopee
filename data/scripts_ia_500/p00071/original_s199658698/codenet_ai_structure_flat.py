n = int(input())
for i in range(1, n+1):
    input()
    t = []
    for _ in range(8):
        line = input()
        row = []
        for ch in line:
            row.append(int(ch))
        t.append(row)
    x = int(input()) - 1
    y = int(input()) - 1
    q = [[x, y]]
    while q:
        p = q.pop(0)
        x1 = p[0]
        y1 = p[1]
        t[y1][x1] = 0
        for delta in range(1, 4):
            if x1 + delta < 8 and t[y1][x1 + delta] == 1:
                q.append([x1 + delta, y1])
                t[y1][x1 + delta] = 0
            if x1 - delta >= 0 and t[y1][x1 - delta] == 1:
                q.append([x1 - delta, y1])
                t[y1][x1 - delta] = 0
            if y1 + delta < 8 and t[y1 + delta][x1] == 1:
                q.append([x1, y1 + delta])
                t[y1 + delta][x1] = 0
            if y1 - delta >= 0 and t[y1 - delta][x1] == 1:
                q.append([x1, y1 - delta])
                t[y1 - delta][x1] = 0
    print('Data {0}:'.format(i))
    for row in t:
        line = ''
        for val in row:
            line += str(val)
        print(line)