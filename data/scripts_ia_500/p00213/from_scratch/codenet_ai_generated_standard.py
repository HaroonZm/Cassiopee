import sys
sys.setrecursionlimit(10**7)

def rects_match(rect, b, k):
    return rect['b'] == b and rect['area'] == k

def solve():
    input = sys.stdin.readline
    while True:
        X, Y, n = map(int, input().split())
        if X == 0 and Y == 0 and n == 0:
            break
        buyers = [None]*(n+1)
        for i in range(1, n+1):
            b, k = map(int, input().split())
            buyers[b] = k
        s = [list(map(int, input().split())) for _ in range(Y)]

        # Count actual counts per buyer (to verify)
        count_actual = [0]*(n+1)
        for y in range(Y):
            for x in range(X):
                if s[y][x] != 0:
                    count_actual[s[y][x]] +=1

        # All buyers appear with the correct count?
        ok = True
        for b in range(1, n+1):
            if buyers[b] != count_actual[b]:
                ok = False
                break
        if not ok:
            print("NA")
            continue

        # If no buyers
        if n == 0:
            for _ in range(Y):
                print(" ".join(map(str, s[_])))
            continue

        # Collect known signs (y,x,b)
        known = []
        for y in range(Y):
            for x in range(X):
                if s[y][x] !=0:
                    known.append((y,x,s[y][x]))

        # To store possible rectangle for each b:
        rects = {}

        # For each buyer find all possible rectangles of area k with all known signs inside
        # Find min/max coords for known points of each buyer
        from collections import defaultdict

        positions = defaultdict(list)
        for y,x,bid in known:
            positions[bid].append((y,x))

        # Check all rectangles for each buyer matching area and containing known points
        def all_in_rect(bid, ry1, rx1, ry2, rx2):
            for (y,x) in positions[bid]:
                if not (ry1 <= y <= ry2 and rx1 <= x <= rx2):
                    return False
            return True

        candidates = {}

        for b in range(1, n+1):
            k = buyers[b]
            pls = positions[b]
            if not pls:
                # no sign: we must find rectangle of area k somewhere with no conflicts
                candidates[b] = []
                for ry1 in range(Y):
                    for ry2 in range(ry1,Y):
                        for rx1 in range(X):
                            for rx2 in range(rx1,X):
                                if (ry2-ry1+1)*(rx2-rx1+1) == k:
                                    # check no known from other buyers inside
                                    conflict = False
                                    for y in range(ry1, ry2+1):
                                        for x in range(rx1, rx2+1):
                                            sb = s[y][x]
                                            if sb != 0 and sb != b:
                                                conflict = True
                                                break
                                        if conflict:
                                            break
                                    if not conflict:
                                        candidates.setdefault(b,[]).append((ry1, ry2, rx1, rx2))
                if not candidates[b]:
                    # no possible rect for this b
                    candidates[b] = []
            else:
                # must contain all signs of b, try minimal rect enclosing signs and expand to area k
                miny = min(p[0] for p in pls)
                maxy = max(p[0] for p in pls)
                minx = min(p[1] for p in pls)
                maxx = max(p[1] for p in pls)
                base_h = maxy - miny +1
                base_w = maxx - minx +1
                res = []
                # try all expansion of base rect to area k that include original sign rect
                # We try to enlarge rectangle from miny..maxy horizontally and vertically within field
                for ry1 in range(miny+1):
                    if ry1 > miny:
                        break
                    for ry2 in range(maxy, Y):
                        if ry2 < maxy:
                            continue
                        height = ry2 - ry1 +1
                        if height < base_h:
                            continue
                        for rx1 in range(minx+1):
                            if rx1 > minx:
                                break
                            for rx2 in range(maxx,X):
                                if rx2 < maxx:
                                    continue
                                width = rx2 - rx1 +1
                                if width < base_w:
                                    continue
                                area = height * width
                                if area != k:
                                    continue
                                if not all_in_rect(b, ry1, rx1, ry2, rx2):
                                    continue
                                # check no conflict with others' known signs inside
                                conflict = False
                                for y in range(ry1, ry2+1):
                                    for x in range(rx1, rx2+1):
                                        sb = s[y][x]
                                        if sb != 0 and sb != b:
                                            conflict = True
                                            break
                                    if conflict:
                                        break
                                if not conflict:
                                    res.append((ry1, ry2, rx1, rx2))
                candidates[b] = res

        # If any candidate empty => no solution
        if any(len(candidates[b])==0 for b in range(1,n+1)):
            print("NA")
            continue

        # Backtracking to assign one rectangle per buyer without overlap on other buyers' rects
        # Area sum must be exact total area
        # No overlap between buyers
        # Signs must be inside rect chosen
        # Check all candidates
        res = None

        buyers_list = list(range(1,n+1))

        grid = [[0]*X for _ in range(Y)]
        used_area = [[0]*X for _ in range(Y)]

        def can_place(ry1, ry2, rx1, rx2):
            for y in range(ry1, ry2+1):
                for x in range(rx1, rx2+1):
                    if used_area[y][x]:
                        return False
            return True

        def place(b, ry1, ry2, rx1, rx2, val):
            for y in range(ry1, ry2+1):
                for x in range(rx1, rx2+1):
                    used_area[y][x] = val
                    grid[y][x] = b if val else 0

        uniques = []

        def dfs(idx):
            nonlocal res
            if res is not None and len(uniques)>1:
                return
            if idx == n:
                # all assigned
                # check if all non-zero s matches buyer in grid
                for y in range(Y):
                    for x in range(X):
                        if s[y][x]!=0 and grid[y][x]!=s[y][x]:
                            return
                uniques.append([row[:] for row in grid])
                if len(uniques) >1:
                    res = None
                else:
                    res = uniques[0]
                return
            b = buyers_list[idx]
            for (ry1, ry2, rx1, rx2) in candidates[b]:
                if can_place(ry1, ry2, rx1, rx2):
                    place(b, ry1, ry2, rx1, rx2, 1)
                    dfs(idx+1)
                    place(b, ry1, ry2, rx1, rx2, 0)
                    if res is None and len(uniques)>1:
                        return

        dfs(0)
        if res is None:
            print("NA")
        else:
            for row in res:
                print(" ".join(map(str,row)))

if __name__ == '__main__':
    solve()