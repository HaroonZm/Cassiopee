# from line_profiler import LineProfiler
from collections import deque

def main():
    while(True):
        W, H = map(int, input().split())
        if not W: break
        tx,ty = map(int, input().split())
        kx,ky = map(int, input().split())
        ma = [[False]*(W+2) for _ in range(H+2)]
        for i in range(1,H+1):
            for j,a in enumerate(input().split()):
                ma[i][j+1] = bool(1-int(a))
        from pprint import pprint
        que = deque([[tx,ty,kx,ky,0]])
        pas = set()
        ans = "NA"
        while(que):
            tx,ty,kx,ky,c = que.popleft()
            if c > 100: break
            if tx == kx and ty == ky:
                ans = c
                break
            for dx,dy in [[-1,0],[0,-1],[1,0],[0,1]]:
                tdx, tdy = [ dx, dy] if ma[ty+dy][tx+dx] else [0,0]
                kdx, kdy = [-dx,-dy] if ma[ky-dy][kx-dx] else [0,0]
                if (tx+tdx,ty+tdy,kx+kdx,ky+kdy) in pas: continue
                que.append([tx+tdx,ty+tdy,kx+kdx,ky+kdy,c+1])
                pas.add((tx+tdx,ty+tdy,kx+kdx,ky+kdy))
        print(ans)

if __name__ == "__main__":
    # prf = LineProfiler()
    # prf.add_function(main)
    # prf.runcall(main)
    # prf.print_stats()
    main()