def main():
    while True:
        line = input()
        if not line:
            break
        parts = line.split()
        if len(parts) < 3:
            break
        n, w, d = map(int, parts)
        if n == 0 and w == 0 and d == 0:
            break
        cuts = []
        for _ in range(n):
            p_i, s_i = map(int, input().split())
            cuts.append((p_i, s_i))
        # Each piece is represented by (x, y, w, d)
        # x,y is the north-west corner coordinate
        pieces = [(0, 0, w, d)]
        for i in range(n):
            p_i, s_i = cuts[i]
            piece = pieces[p_i - 1]
            x, y, pw, pd = piece
            perimeter = 2*(pw + pd)
            s = s_i
            # locate the start point side
            # NW corner is at (x,y), sides ordered clockwise:
            # north side: length pw, from (x,y) moving east
            # east side: length pd, from (x+pw, y) moving south
            # south side: length pw, from (x+pw, y+pd) moving west
            # west side: length pd, from (x, y+pd) moving north
            if s < pw:
                # north side
                sx = x + s
                sy = y
                # cut is vertical (parallel to north-south), so cut divides width
                # cut along line x = sx
                # split into left and right pieces
                left = (x, y, sx - x, pd)
                right = (sx, y, x+pw - sx, pd)
                new_pieces = [left, right]
            elif s < pw + pd:
                # east side
                s_ = s - pw
                sx = x + pw
                sy = y + s_
                # cut is horizontal (parallel to east-west), so cut divides depth
                # cut along line y = sy
                up = (x, y, pw, sy - y)
                down = (x, sy, pw, y+pd - sy)
                new_pieces = [up, down]
            elif s < pw + pd + pw:
                # south side
                s_ = s - (pw + pd)
                sx = x + pw - s_
                sy = y + pd
                # cut vertical
                left = (x, y, sx - x, pd)
                right = (sx, y, x+pw - sx, pd)
                new_pieces = [left, right]
            else:
                # west side
                s_ = s - (pw + pd + pw)
                sx = x
                sy = y + pd - s_
                # cut horizontal
                up = (x, y, pw, sy - y)
                down = (x, sy, pw, y + pd - sy)
                new_pieces = [up, down]
            # Remove the piece to cut, add the two new ones
            del pieces[p_i - 1]
            # compute area of new pieces
            areas = [p[2]*p[3] for p in new_pieces]
            # sort new pieces so that smaller area has smaller id
            combined = list(zip(areas, new_pieces))
            combined.sort(key=lambda x: x[0])
            pieces.extend([p[1] for p in combined])
        areas = [p[2]*p[3] for p in pieces]
        areas.sort()
        print(" ".join(str(a) for a in areas))
if __name__ == "__main__":
    main()