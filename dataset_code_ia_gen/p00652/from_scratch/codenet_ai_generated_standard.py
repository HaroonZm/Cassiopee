import sys
import bisect

def main():
    input = sys.stdin.readline
    while True:
        n,m,w,h,S = map(int,input().split())
        if n==0 and m==0 and w==0 and h==0 and S==0:
            break
        l = [0]*m
        r = [0]*m
        for i in range(m):
            li,ri = map(int,input().split())
            l[i],r[i] = li,ri
        almonds = []
        for _ in range(n):
            x,y = map(float,input().split())
            almonds.append((x,y))

        # Precompute areas of pieces 0..m-1
        # Each piece i between line i and line i+1; line m is top edge at h
        # Since l and r are lists of length m, piece i uses lines i and i+1:
        # For i in [0,m-1), piece i is between lines i and i+1
        # The problem states lines connect points (0,l[i]) to (w,r[i]) for i in [0,m)
        # But we have m lines, from 0..m-1, with l[m-1], r[m-1] = h.
        # The pieces are 0..m-1; top piece is between lines m-1 and the top edge?

        # Actually, indexing pieces as i=0..m-1, piece i is bounded below by line i, above by line i+1,
        # with line m is the top edge (0,h) to (w,h)
        # But input only gives m lines, last line l[m-1], r[m-1]=h, so piece i is between line i and i+1 for i in 0..m-2,
        # piece m-1 is between line m-1 and top, which is same as line m-1..top? The last line is at h, so top edge is at h.

        # So to handle all pieces including the top piece, append the top edge
        l.append(h)
        r.append(h)
        m += 1

        # area[i] is area of piece i between line i and line i+1
        area = [0]*(m-1)
        for i in range(m-1):
            area[i] = ((l[i+1]+l[i])+(r[i+1]+r[i]))*w/2/2  # trapezoid area: average height * width
            # Average height = (left side avg + right side avg)/2
            # left height avg: (l[i+1]+l[i])/2
            # right height avg: (r[i+1]+r[i])/2
            # area = w * ( (l[i+1]+l[i])/2 + (r[i+1]+r[i])/2 )/2
            # Simplified above

        # prefix sums of area for fast range area calculation
        # pre_area[i]: sum of areas of pieces [0..i-1]
        pre_area = [0]*(m)
        for i in range(m-1):
            pre_area[i+1] = pre_area[i]+area[i]

        # Count almonds in each piece
        # For each almond (x,y), find piece i so that y in [lines i and i+1]
        # y coordinate between max of l[i], r[i] and min of l[i+1], r[i+1]? 
        # Actually, the lines form a polygonal chain on left and right sides;
        # The pieces are bounded left by vertical line x=0 going from y=l[i] to y=l[i+1],
        # right side x=w going from y=r[i] to y=r[i+1]
        # For almond at (x,y), find i such that almond is between lines i and i+1 vertically:
        # i where y >= max(l[i],r[i]) and y <= min(l[i+1],r[i+1])

        # Actually: line i: from (0,l[i]) to (w,r[i]) line
        # line i+1: (0,l[i+1]) to (w,r[i+1])
        # We want almond y to be between lines i and i+1, meaning the almond is in piece i.

        # Since lines do not cross in x in (0,w) and are monotonic in y, 
        # the almond y is between "line i" and "line i+1" if
        # y >= max(l[i], r[i]) and y < max(l[i+1], r[i+1]) or so
        # We need a method.

        # But the problem is that the left and right walls are defined by l[i] and r[i].
        # The line i is segment between (0,l[i]) and (w,r[i])
        # The line i+1 is between (0,l[i+1]) and (w,r[i+1])

        # For almond (x,y), we compute y coordinates of line i and i+1 at almond.x
        # line i at almond x:
        # y_i = l[i] + (r[i] - l[i]) * (x / w)
        # similarly for line i+1

        # almond is in piece i if y_i <= y < y_{i+1} or vice versa (depending which line is upper)
        # Need to check order of lines to find which is upper or lower.

        # We'll binary search i in [0..m-2] so that almond y is between lines i and i+1 at almond x

        # Precompute functions to get line_y(i,x)
        def line_y(i,x):
            return l[i] + (r[i]-l[i]) * (x/w)

        almonds_count = [0]*(m-1)

        for x,y in almonds:
            low,high = 0,m-2
            while low<=high:
                mid = (low+high)//2
                y1 = line_y(mid,x)
                y2 = line_y(mid+1,x)
                lowy = min(y1,y2)
                highy = max(y1,y2)
                if y < lowy - 1e-12:
                    high = mid -1
                elif y > highy + 1e-12:
                    low = mid +1
                else:
                    almonds_count[mid] +=1
                    break

        # Sliding window to find min almonds in consecutive pieces with area >= S
        ans = float('inf')
        j = 0
        total_almonds = 0
        for i in range(m-1):
            # move j forward while area < S
            while j < m-1 and pre_area[j+1] - pre_area[i] < S:
                total_almonds += almonds_count[j]
                j +=1
            # Now [i..j) area < S or j == m-1
            if j == m-1 and pre_area[j] - pre_area[i] < S:
                # no solution extending this left border
                total_almonds -= almonds_count[i]
                continue
            # expand j one more to reach area >= S
            if j < m-1:
                total_almonds += almonds_count[j]
                j +=1
            # now area in [i,j) >= S
            # try to minimize almonds
            ans = min(ans,total_almonds)
            # slide left border
            total_almonds -= almonds_count[i]

        print(ans if ans != float('inf') else 0)

if __name__ == "__main__":
    main()