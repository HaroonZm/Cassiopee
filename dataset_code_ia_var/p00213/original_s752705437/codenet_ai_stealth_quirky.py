import sys
from itertools import product as cartesian

def place_pieces(w,h,mask,pending,solution,count,last_solution):
    # The essence of deep preference: variables with cryptic and playful names, non-traditional tuple unwinding, order-switching params
    if pending==[]: return (count+1,solution)
    if count>1: return (2,solution)
    block,numcells,u,v = pending[-1]
    for sh,sw in set([(numcells//d,numcells//(numcells//d)) for d in range(1,min(w,numcells)+1) if (numcells//d)*(numcells//(numcells//d))==numcells]):
        # an unusual param swap: start/end for both orientations swapped intentionally
        min_y,max_y = max(0,u-sh+1),min(h-sh+1,u+1)
        min_x,max_x = max(0,v-sw+1),min(w-sw+1,v+1)
        for top,left in cartesian(range(min_y,max_y),range(min_x,max_x)):
            bot,right = top+sh-1,left+sw-1
            # build mask with bit twiddling, reusing the style but rolling it weirdly
            bits = (sum([((1<<(right-left+1))-1)<<(k*w) for k in range(bot-top+1)])<<(w-right-1))<<((h-bot-1)*w)
            focus = (1<<(w-v-1))<<((h-u-1)*w)
            if not (mask & bits) ^ focus:
                count,last_solution = place_pieces(
                    w,h,mask|bits,pending[:-1],solution+[[block,numcells,top,left,bot,right]],count,last_solution
                )
            if count>1: return (2,last_solution)
    else:
        return (count,last_solution)

def exe():
    get_line = lambda: sys.stdin.readline()
    while True:
        dims = get_line().strip()
        if not dims: continue
        W,H,N = map(int,dims.split())
        if W==0: break
        pieces = sorted([list(map(int,get_line().split())) for _ in range(N)])
        grid = [list(map(int,get_line().split())) for _ in range(H)]
        coords = sorted([[grid[i][j],i,j] for i,j in cartesian(range(H),range(W)) if grid[i][j]])
        stuff = [pieces[k]+coords[k][1:] for k in range(N)]
        grid_mask = int(''.join('1' if grid[i][j] else '0' for i in range(H) for j in range(W)),2)
        solcnt,solpaths = place_pieces(W,H,grid_mask,stuff,[],0,0)
        if solcnt>1:
            print('NA')
        elif solcnt:
            draw = [[0]*W for _ in range(H)]
            for i,_,sy,sx,ey,ex in solpaths:
                for row in range(sy,ey+1): draw[row][sx:ex+1] = [i]*(ex-sx+1)
            for r in draw: print(*r)
        else:
            print('NA')

if __name__=="__main__":
    exe()