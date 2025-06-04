def main():
    from functools import reduce

    class State:
        def __init__(self, board, scores):
            self.board = [row[:] for row in board]
            self.scores = scores

        def clone(self):
            return State(self.board, self.scores)

    def flatten(xs): return [item for sublist in xs for item in sublist]

    def parse_input():
        lines = []
        while True:
            try: lines.append(input())
            except EOFError: break
            if len(lines) == 7: break
        n = int(lines[0])
        mat = [list(map(int, x.split())) for x in lines[1:6]]
        sc = list(map(int, lines[6].split()))
        return n, mat, sc

    moves = ((1,0), (0,-1), (-1,0), (0,1))

    def simulate2(b, s):
        _b = [row[:] for row in b]
        total, multi = 0, 1
        while 1:
            delset = set()
            for r in range(5):
                for l in range(5,2,-1):
                    for k in range(5-l+1):
                        x = _b[r][k]
                        if x!=0 and all(_b[r][j]==x for j in range(k,k+l)):
                            delset |= {(j,r) for j in range(k,k+l)}
            for c in range(5):
                col = [_b[r][c] for r in range(5)]
                for l in range(5,2,-1):
                    for k in range(5-l+1):
                        y = col[k]
                        if y!=0 and all(col[j]==y for j in range(k,k+l)):
                            delset |= {(c,j) for j in range(k,k+l)}
            if not delset: break
            for x,y in delset:
                total += s[_b[y][x]-1]*multi
                _b[y][x] = 0
            for c in range(5):
                filtered = list(filter(lambda r: _b[r][c]!=0, range(5)))
                fixed = [0]*(5-len(filtered))+[ _b[r][c] for r in filtered ]
                for r in range(5):
                    _b[r][c]=fixed[r]
            multi+=1
        return total

    def dfs_mess(xy, step, field, ss):
        from operator import itemgetter
        res = simulate2(field, ss)
        if step==0: return res
        x0,y0=xy
        for dx,dy in moves:
            xx,yy=x0+dx,y0+dy
            if 0<=xx<5 and 0<=yy<5:
                field[y0][x0],field[yy][xx]=field[yy][xx],field[y0][x0]
                tmp = dfs_mess((xx,yy), step-1, field, ss)
                res = max(res,tmp)
                field[y0][x0],field[yy][xx]=field[yy][xx],field[y0][x0]
        return res

    while True:
        try:
            n = int(input())
        except:
            break
        if n == -1: break
        board = []
        for _ in range(5):
            board.append([int(x) for x in input().split()])
        scores = list(map(int, input().split()))
        max_score = 0
        for yy in range(5):
            for xx in range(5):
                candidate = dfs_mess((xx,yy), n, [row[:] for row in board], scores)
                if candidate>max_score: max_score=candidate
        print(max_score)

main()