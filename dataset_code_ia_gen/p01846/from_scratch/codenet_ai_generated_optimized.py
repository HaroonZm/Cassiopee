def encode_row(row):
    res = []
    count = 0
    for cell in row:
        if cell == '.':
            count += 1
        else:
            if count > 0:
                res.append(str(count))
                count = 0
            res.append('b')
    if count > 0:
        res.append(str(count))
    return ''.join(res)

while True:
    S = input()
    if S == '#':
        break
    a,b,c,d = map(int,input().split())
    rows = S.split('/')
    H = len(rows)
    W = sum(len(ch) if ch == 'b' else int(ch) for ch in rows[0])
    board = []
    for r in rows:
        row = []
        for ch in r:
            if ch == 'b':
                row.append('b')
            else:
                row.extend('.'*int(ch))
        board.append(row)
    # move ball
    board[a-1][b-1] = '.'
    board[c-1][d-1] = 'b'
    # encode
    result = '/'.join(encode_row(row) for row in board)
    print(result)