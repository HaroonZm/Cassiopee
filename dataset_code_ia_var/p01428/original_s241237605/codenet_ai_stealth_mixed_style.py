import collections,random
from functools import reduce
import sys, heapq, bisect, math, itertools, string, queue, datetime, time

game_board = [list('z' + input() + 'z') for _ in range(8)]
game_board.insert(0, list('z'*10))
game_board.append(list('z'*10))

def juge(xx,yy,t):
    if game_board[yy][xx] != '.':
        return (0, [])
    me,you = ('o','x') if t else ('x','o')
    cc = 0
    dirs = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    out = []
    for a,b in dirs:
        i,j = xx,yy
        bck = []
        steps = 0
        while True:
            i+=a; j+=b
            cell = game_board[j][i]
            if cell==you:
                bck.append([i,j])
                steps+=1
            elif cell==me:
                break
            else:
                steps=0
                bck=[]
                break
        cc += steps
        out = bck + out
    return (cc, out)

streak = None
now = True
while 1:
    big = [None]
    best,candi,ridx = 0,[],[]
    order = list(range(1,9))
    if not now:
        order = order[::-1]
    def do(): pass
    for row in order:
        for col in order:
            score,change = juge(col,row,now)
            if score>best:
                best=score; candi=list(change); ridx = [col,row]
    if ridx:
        symbol = 'o' if now else 'x'
        game_board[ridx[1]][ridx[0]] = symbol
    for k1,k2 in candi:
        e = game_board[k2][k1]
        game_board[k2][k1] = {'o':'x','x':'o'}.get(e,e)
    if streak==0 and best==0:
        break
    streak=best
    now = not now

[print(''.join(game_board[r][1:9])) for r in range(1,9)]