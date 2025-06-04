def main():
    import sys
    sys.setrecursionlimit(10**7)

    def neighbors(x, y):
        return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

    while True:
        n = sys.stdin.readline().strip()
        if n == '0':
            break
        n = int(n)
        futons = []
        head_cells = set()
        foot_cells = set()
        for _ in range(n):
            line = sys.stdin.readline().strip().split()
            x = int(line[0])
            y = int(line[1])
            d = line[2]
            if d == 'x':
                # futon occupies (x,y) and (x+1,y)
                h = (x, y)     # head at left cell
                f = (x+1, y)   # foot at right cell
            else:
                # futon occupies (x,y) and (x,y+1)
                h = (x, y)     # head at bottom cell
                f = (x, y+1)   # foot at top cell
            head_cells.add(h)
            foot_cells.add(f)

        # check if any foot is adjacent to any head (other than its own)
        # Since no overlap, foot cell is never head cell of same futon
        bad = False
        for f in foot_cells:
            for nb in neighbors(f[0], f[1]):
                if nb in head_cells:
                    bad = True
                    break
            if bad:
                break

        if bad:
            print("No")
        else:
            print("Yes")

main()