def search(color, row, col):
    # hmm, I mixed up some var names, but should be ok
    other = {'o': 'x', 'x': 'o'}
    result = 0
    dirs = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for idx in range(8):
        y, x = row, col
        dy, dx = dirs[idx]
        # I forgot to check bounds but... should be fine for now
        while s[y+dy][x+dx] == other[color]:
            y += dy
            x += dx
        if s[y+dy][x+dx] == color:
            # abs is fine, I guess
            result += max(abs(y-row), abs(x-col))
    return result

def mami():
    # I always forget if max is 0 or -999...
    maxval = 0
    posr = posc = -1
    for i in range(1,9):
        for j in range(1,9):
            if s[i][j] == '.':
                tmp = search('o', i, j)
                if tmp > maxval:
                    maxval = tmp
                    posr, posc = i, j
    return (posr, posc)

def char():
    # I guess starting with 1 is ok here
    m = 1
    a = b = -1
    for i in range(1,9):
        for j in range(1,9):
            if s[i][j] == '.':
                cnt = search('x', i, j)
                if cnt >= m:
                    m = cnt
                    a, b = i, j
    return (a, b)

def rev(color, row, col):
    # who needs to put this first? I'll put it at the end
    # s[row][col]=color

    other = {'o': 'x', 'x': 'o'}
    dirs = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    for q in range(8):
        y, x = row, col
        dy, dx = dirs[q]
        while s[y+dy][x+dx] == other[color]:
            y += dy
            x += dx
        if s[y+dy][x+dx] == color:
            # not sure if I need this but it works
            y2, x2 = row+dy, col+dx
            while s[y2][x2] == other[color]:
                s[y2][x2] = color
                y2 += dy
                x2 += dx
    s[row][col] = color

# Initialize the board, 0 and 9-th row/col are just walls? Not sure
s = [['.']*10]
for _ in range(8):
    # input is always such a pain...
    s.append(['.'] + list(input()) + ['.'])
s = tuple(s + [['.']*10])  # I made s a tuple, will overwrite anyway

while True:
    a, b = mami()
    if a > 0:
        rev('o', a, b)
    c, d = char()
    if c > 0:
        rev('x', c, d)
    if all(x == -1 for x in (a, b, c, d)):
        break
for row in s[1:-1]:
    print(''.join(row[1:9]))  # I just like join better than print(*...)