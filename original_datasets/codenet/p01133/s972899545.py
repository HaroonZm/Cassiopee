def solve():
    from math import sqrt
    from sys import stdin
    f_i = stdin
    
    def dfs(point, remain, elapsed):
        if not remain:
            return True
        
        next_c = set()
        for c in remain:
            new_elapsed = elapsed + adj[point][c]
            if new_elapsed >= from_d[c]:
                return False
            next_c.add((c, new_elapsed))
        
        for c, new_elapsed in next_c:
            remain.remove(c)
            if dfs(c, remain, new_elapsed):
                return True
            remain.add(c)
        
        return False
    
    while True:
        n, hx, hy, dx, dy = map(int, f_i.readline().split())
        if n == 0:
            break
        
        C = [tuple(map(int, f_i.readline().split())) for i in range(n)]
        from_d = tuple(sqrt((cx - dx) ** 2 + (cy - dy) ** 2) for cx, cy in C)
        C.append((hx, hy))
        adj = tuple(tuple(sqrt((px - qx) ** 2 + (py - qy) ** 2) for qx, qy in C) for px, py in C)
        
        if dfs(n, set(range(n)), 0):
            print("YES")
        else:
            print("NO")

solve()