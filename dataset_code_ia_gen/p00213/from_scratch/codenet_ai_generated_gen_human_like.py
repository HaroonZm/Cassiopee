import sys

def parse_input():
    datasets = []
    lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(lines):
            break
        X, Y, n = map(int, lines[idx].split())
        idx += 1
        if X == 0 and Y == 0 and n == 0:
            break
        buyers = []
        for _ in range(n):
            b, k = map(int, lines[idx].split())
            buyers.append((b, k))
            idx += 1
        s = []
        for _ in range(Y):
            row = list(map(int, lines[idx].split()))
            s.append(row)
            idx += 1
        datasets.append((X, Y, n, buyers, s))
    return datasets

def check_rectangle_area(x1, y1, x2, y2, lx, ly):
    return (x2 - x1 + 1) * (y2 - y1 + 1) == lx * ly

def solve_dataset(X, Y, n, buyers, s):
    # buyers: list of (b_i, k_i)
    # s: Y rows x X cols matrix (row major)
    # Need to assign rectangles for each buyer so that:
    # - The union is the whole field
    # - Each rectangle is rectangular (normal rectangle)
    # - rectangle area == k_i for buyer i
    # - rectangle contains the positions of the buyer's boards (s_ij == b_i)
    # - no overlap, cover whole area
    
    # We try to find all rectangles for each buyer consistent with all boards placed
    
    # For each buyer b_i, locate positions of its boards
    boards_pos = {b: [] for b,k in buyers}
    for y in range(Y):
        for x in range(X):
            cell = s[y][x]
            if cell != 0:
                if cell in boards_pos:
                    boards_pos[cell].append( (x,y) )
                else:
                    # board number not in buyers? ignore, problem says buyer numbers from 1 to n
                    pass

    # For any buyer, check if #boards > 0, then the rectangle must contain all boards
    # possible rectangle candidates must:
    # - cover all board positions assigned to that buyer
    # - have area == k_i
    
    candidate_rectangles = {}
    for b,k in buyers:
        pos = boards_pos[b]
        if len(pos) == 0:
            # buyer with no boards, can be any rectangle with area k
            # we will try all rectangles of area k inside grid later
            candidate_rectangles[b] = []
            continue
        # determine min/max bounding box to find candidates
        xs = [p[0] for p in pos]
        ys = [p[1] for p in pos]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        # The rectangle must contain (minx,miny) to (maxx,maxy)
        base_area = (maxx - minx + 1) * (maxy - miny + 1)
        # area must be k
        candidates = []
        # Try to expand rectangle around minx,maxx,miny,maxy to achieve area k
        # We try all rectangles containing the min bounding box with area k
        # So rectangle must have area k and contain bounding box
        for x1 in range(0, minx+1):
            for y1 in range(0, miny+1):
                for x2 in range(maxx, X):
                    for y2 in range(maxy, Y):
                        w = x2 - x1 + 1
                        h = y2 - y1 + 1
                        area = w*h
                        if area == k:
                            # check contains all boards
                            # (already guaranteed minx,maxx,miny,maxy inside)
                            candidates.append( (x1,y1,x2,y2) )
        candidate_rectangles[b] = candidates

    # For buyers with no boards, try all rectangles of area k anywhere
    for b,k in buyers:
        if len(boards_pos[b]) == 0:
            candidates = []
            for x1 in range(X):
                for y1 in range(Y):
                    for x2 in range(x1, X):
                        for y2 in range(y1, Y):
                            w = x2 - x1 + 1
                            h = y2 - y1 + 1
                            if w*h == k:
                                candidates.append((x1,y1,x2,y2))
            candidate_rectangles[b] = candidates

    # Now we have a set of candidate rectangles per buyer
    # Problem: assign one candidate rectangle per buyer with no overlap and cover all area
    # Also check if assigned rectangle contains all boards for that buyer

    # Because X,Y <=10, n<=15, we can DFS over buyers and try to assign rectangles
    # If multiple solutions found -> print NA
    # If no solution -> NA
    # If one solution -> output that

    # The whole field must be covered exactly by these rectangles, no overlaps

    # Prepare some helper functions
    def rect_cells(rect):
        x1,y1,x2,y2 = rect
        cells = []
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                cells.append((x,y))
        return cells

    solutions = []
    used_area = [[False]*X for _ in range(Y)]

    def is_valid(rect,used):
        x1,y1,x2,y2 = rect
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if used[y][x]:
                    return False
        return True

    def set_used(rect,used,val):
        x1,y1,x2,y2=rect
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                used[y][x] = val

    buyer_list = [b for b,k in buyers]

    assigned_rects = [None]*len(buyer_list)

    def dfs(i):
        if len(solutions) > 1:
            return
        if i == len(buyer_list):
            # check if covered all area
            # used_area after assignment must be full True
            # actually used_area is to track coverage
            # but currently used_area reflects only last assignment, we need full coverage check
            # Instead, we check all cells covered by assigned_rects:
            cover_check = [[False]*X for _ in range(Y)]
            for r in assigned_rects:
                if r is None:
                    return
                x1,y1,x2,y2 = r
                for y in range(y1,y2+1):
                    for x in range(x1,x2+1):
                        if cover_check[y][x]:
                            # overlap
                            return
                        cover_check[y][x] = True
            # check full coverage
            for y in range(Y):
                for x in range(X):
                    if not cover_check[y][x]:
                        return
            # check if for each buyer all its boards are inside assigned rectangle
            for idx,b in enumerate(buyer_list):
                r = assigned_rects[idx]
                x1,y1,x2,y2 = r
                for (bx,by) in boards_pos[b]:
                    if not (x1 <= bx <= x2 and y1 <= by <= y2):
                        return
                # also area matches k
                area = (x2 - x1 + 1)*(y2 - y1 + 1)
                k = 0
                for bb,kk in buyers:
                    if bb==b:
                        k=kk
                        break
                if k != area:
                    return
            # valid solution
            solutions.append( list(assigned_rects) )
            return
        b = buyer_list[i]
        for rect in candidate_rectangles[b]:
            if not is_valid(rect, used_area):
                continue
            # assign
            set_used(rect, used_area, True)
            assigned_rects[i] = rect
            dfs(i+1)
            assigned_rects[i] = None
            set_used(rect, used_area, False)

    dfs(0)

    if len(solutions) != 1:
        return None

    # Build output grid; for each buyer fill cells with buyer number
    grid = [[0]*X for _ in range(Y)]
    sol = solutions[0]
    for idx,b in enumerate(buyer_list):
        x1,y1,x2,y2 = sol[idx]
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                grid[y][x] = b
    return grid

def main():
    datasets = parse_input()
    for data in datasets:
        X,Y,n,buyers,s = data
        res = solve_dataset(X,Y,n,buyers,s)
        if res is None:
            print("NA")
        else:
            for y in range(Y):
                print(" ".join(str(res[y][x]) for x in range(X)))

if __name__ == "__main__":
    main()