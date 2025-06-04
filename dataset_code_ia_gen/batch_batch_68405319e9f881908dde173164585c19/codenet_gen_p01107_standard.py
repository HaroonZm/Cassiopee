from sys import stdin
from collections import deque

def can_collect_and_return(grid, N, M):
    # positions: entrance and treasures
    corners = [(0,0),(N-1,0),(N-1,M-1),(0,M-1)]

    # Since floors collapse after stepping once (except entrance),
    # Taro can visit each cell only once in his path except entrance which can be revisited any number of times.
    # We need to find if there's a path start->treasure1->treasure2->treasure3->start with that constraint.

    # We'll represent states as (r, c, collected_mask)
    # collected_mask is a 3-bit integer marking which of the 3 treasure chests are collected.
    # Index treasures as: (N-1,0)->0, (N-1,M-1)->1, (0,M-1)->2

    treasure_pos = corners[1:]
    treasure_indices = {pos: idx for idx,pos in enumerate(treasure_pos)}

    # BFS over states with visited tracking
    # visited[r][c][collected_mask]: whether state visited.
    visited = [[[False]*8 for _ in range(M)] for __ in range(N)]
    q = deque()
    start_state = (0,0,0) # start at entrance, no treasure collected
    q.append(start_state)
    visited[0][0][0] = True

    # For entrance cell, can re-enter, so it doesn't collapse.
    # For other cells, visited only once per path, handled by visited array and condition.

    while q:
        r,c,collected = q.popleft()
        # If at entrance and all treasures collected
        if (r,c) == (0,0) and collected == 7:
            return True
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if 0<=nr<N and 0<=nc<M and grid[nr][nc]=='.':
                ncollected = collected
                # Check if stepping onto treasure
                if (nr,nc) in treasure_indices:
                    ncollected |= 1<<treasure_indices[(nr,nc)]
                # If it's entrance cell, can always visit.
                # Otherwise, if visited in this mask, skip.
                if (nr,nc) == (0,0):
                    if not visited[nr][nc][ncollected]:
                        visited[nr][nc][ncollected] = True
                        q.append((nr,nc,ncollected))
                else:
                    # fragile cell: can only be passed once per path, so only unvisited for that state
                    if not visited[nr][nc][ncollected]:
                        visited[nr][nc][ncollected] = True
                        q.append((nr,nc,ncollected))
    return False

def main():
    input_lines = stdin.read().splitlines()
    idx = 0
    while True:
        if idx>=len(input_lines): break
        line = input_lines[idx].strip()
        if not line:
            idx+=1
            continue
        N,M = map(int,line.split())
        if N==0 and M==0:
            break
        idx+=1
        grid = []
        for _ in range(N):
            grid.append(list(input_lines[idx]))
            idx+=1
        # Ensure four corner rooms are enterable per problem statement
        # run logic:
        print("YES" if can_collect_and_return(grid,N,M) else "NO")

if __name__=="__main__":
    main()