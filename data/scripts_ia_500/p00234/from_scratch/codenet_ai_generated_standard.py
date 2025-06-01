import sys
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        W,H = map(int,input().split())
        if W == 0 and H == 0:
            break
        f,m,o = map(int,input().split())
        grid = [list(map(int,input().split())) for _ in range(H)]
        top_rows = [0]
        # Starting positions: y=1 (index 0), any x in [0,W-1]
        start_positions = [(x,0) for x in range(W)]
        end_y = H-1
        # State dp: x,y,oxygen left, visited oxygen bitmap
        # Oxygen cells IDs
        oxygen_cells = {}
        oxygen_id = 0
        for y in range(H):
            for x in range(W):
                if grid[y][x] > 0:
                    oxygen_cells[(x,y)] = oxygen_id
                    oxygen_id += 1
        INF = 10**15
        # visited: dict with keys=(x,y,oxygen_left, mask) values=min_cost
        # Use Dijkstra: heapq with (cost,x,y,oxygen_left,mask)
        heap = []
        dist = dict()
        for x,y in start_positions:
            o2 = o
            mask = 0
            cost = 0
            # If starting cell is oxygen cell, must consume oxygen replenishment
            if grid[y][x] > 0:
                # Need to replenish oxygen
                ox_id = oxygen_cells[(x,y)]
                o2 = min(m, o2 + grid[y][x])
                mask |= 1 << ox_id
            # cost is zero because starting cell does not need to be dug?
            # Problem states: digging cost for soil cells, oxygen cells no dig cost.
            # As per problem, from starting cell, digging cost only when passing through soil cells.
            # So start cost 0
            dist[(x,y,o2,mask)] = 0
            heapq.heappush(heap,(0,x,y,o2,mask))
        res = INF
        while heap:
            c,x,y,o2,mask = heapq.heappop(heap)
            if dist.get((x,y,o2,mask),INF) < c:
                continue
            if y == end_y and o2 > 0:
                # Arrived at bottom row with positive oxygen left
                res = c if c<=f else res
                continue
            for dx,dy in [(-1,0),(1,0),(0,1)]:
                nx,ny = x+dx,y+dy
                if 0 <= nx < W and 0 <= ny < H:
                    no2 = o2 - 1
                    if no2 <= 0:
                        continue
                    cell = grid[ny][nx]
                    nmask = mask
                    # Must dig soil cells, pay cost
                    # Oxygen cells, must replenish oxygen once upon arrival
                    if cell < 0:
                        nc = c + (-cell)
                    else:
                        # oxygen cell
                        ox_id = oxygen_cells[(nx,ny)]
                        # must replenish oxygen if not yet done
                        if not (mask & (1 << ox_id)):
                            no2 = min(m, no2 + cell)
                            nmask = mask | (1 << ox_id)
                        nc = c
                    state = (nx,ny,no2,nmask)
                    if dist.get(state,INF) > nc:
                        dist[state] = nc
                        heapq.heappush(heap,(nc,nx,ny,no2,nmask))
        print(res if res!=INF else "NA")

if __name__ == "__main__":
    solve()