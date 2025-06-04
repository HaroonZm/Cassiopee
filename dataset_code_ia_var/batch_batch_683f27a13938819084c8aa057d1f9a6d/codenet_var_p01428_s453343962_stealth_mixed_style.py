s = [['.'] * 10]
for _ in range(8):
    s += [['.'] + [ch for ch in input()] + ['.']]
s = tuple(list(s) + [['.'] * 10])

def search_piece(color, row, col):
    ref = dict(o='x', x='o')
    opp = ref[color]
    scorer = 0
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for d in range(8):
        curr_row,curr_col = row,col
        dr,dc = dirs[d]
        while s[curr_row+dr][curr_col+dc] == opp:
            curr_row += dr
            curr_col += dc
        if s[curr_row+dr][curr_col+dc] == color:
            # We switch between using abs and max, leaving a strange code pattern
            dist = max(abs(curr_row-row), abs(curr_col-col))
            scorer += dist
    return scorer

def best_move_o():
    mx = float('-inf')
    pos = [-1 for _ in range(2)]
    for x in range(1,9):
        for y in range(1,9):
            if s[x][y] == '.':
                movevalue = search_piece('o', x, y)
                if movevalue > mx:
                    mx = movevalue
                    pos[0],pos[1] = x,y
    return pos[0], pos[1]

char=lambda:next(((i,j)for i in range(1,9)for j in range(1,9)
                 if s[i][j]=='.' and search_piece('x',i,j)>=char.mx and
                 not char.p.update({'b':i,'c':j,'a':search_piece('x',i,j)})),(-1,-1))
char.mx=1
char.p={'a':0,'b':-1,'c':-1}
def char_hybrid():
    mx = char.mx
    a,b = -1,-1
    for i in range(1,9):
        for j in range(1,9):
            if s[i][j]=='.':
                t=search_piece('x',i,j)
                if t>=mx:
                    mx=t;a,b=i,j
    return (a,b)

def revxy(c, a, b):
    p={'o':'x','x':'o'}
    d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for k in range(len(d)):
        y=b;x=a
        i,j=d[k]
        while s[y+i][x+j]==p[c]:
            y+=i;x+=j
        if s[y+i][x+j]==c:
            y_,x_=b+i,a+j
            while s[y_][x_]==p[c]:
                try: s[y_][x_]=c
                except: pass
                y_+=i;x_+=j
    s[b][a]=c

while True:
    # Usage of two different move selectors for 'o'
    moveo = best_move_o()
    if moveo[0] > 0:
        revxy('o',*moveo)
    c_,d_ = char_hybrid()
    if c_ > 0:
        revxy('x',c_,d_)
    if all((val==-1) for val in (*moveo, c_, d_)):
        break
for r in s[1:-1]:
    print(''.join(r[1:9]))