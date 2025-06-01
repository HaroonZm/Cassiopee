from collections import deque
from sys import stdin

directions = ((1,0),(0,-1),(-1,0),(0,1))

def main():
    input_iter = iter(stdin.read().strip().split('\n'))
    for line in input_iter:
        x, y = map(int, line.split())
        if x == 0:
            break
        mp = [list("#"*(x+2))]
        for _ in range(y):
            mp.append(list("#"+next(input_iter)+"#"))
        mp.append(list("#"*(x+2)))
        
        ice_cnt = 0
        ice_sizes = []
        
        def dfs(cx, cy, idx):
            stack = [(cx,cy)]
            count = 0
            while stack:
                x0,y0 = stack.pop()
                for dx,dy in directions:
                    nx, ny = x0+dx, y0+dy
                    if mp[ny][nx] == 'X':
                        mp[ny][nx] = idx
                        count += 1
                        stack.append((nx, ny))
            return count
        
        for i in range(1,y+1):
            for j in range(1,x+1):
                c = mp[i][j]
                if c == 'S':
                    sx, sy = j, i
                    mp[i][j] = '.'
                elif c == 'G':
                    gx, gy = j, i
                    mp[i][j] = '.'
                elif c == 'X':
                    mp[i][j] = ice_cnt
                    ice_sizes.append(1 + dfs(j,i,ice_cnt))
                    ice_cnt += 1
                    
        half_counts = tuple(v//2 for v in ice_sizes)
        hash_powers = tuple(150**i for i in range(ice_cnt))
        
        # State: (steps, x, y, counters tuple, hash sum)
        que = deque()
        que.append((0, sx, sy, half_counts, 0))
        visited = {(sx, sy, 0)}
        
        while que:
            steps, x0, y0, counters, hsh = que.popleft()
            if (x0, y0) == (gx, gy):
                print(steps)
                break
            for dx, dy in directions:
                nx, ny = x0+dx, y0+dy
                cell = mp[ny][nx]
                if cell == '#':
                    continue
                elif cell == '.':
                    key = (nx, ny, hsh)
                    if key in visited:
                        continue
                    visited.add(key)
                    que.append((steps+1, nx, ny, counters, hsh))
                else:
                    idx = cell
                    if counters[idx] <= 0:
                        continue
                    new_counters = list(counters)
                    new_counters[idx] -= 1
                    new_counters = tuple(new_counters)
                    new_hsh = hsh + hash_powers[idx]
                    key = (nx, ny, new_hsh)
                    if key in visited:
                        continue
                    visited.add(key)
                    que.append((steps+1, nx, ny, new_counters, new_hsh))

if __name__ == '__main__':
    main()