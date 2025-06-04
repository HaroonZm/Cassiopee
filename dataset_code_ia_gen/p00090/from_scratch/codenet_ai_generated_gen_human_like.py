import sys
import math

def main():
    lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(lines):
            break
        n = int(lines[idx])
        idx += 1
        if n == 0:
            break
        centers = []
        for _ in range(n):
            x_str, y_str = lines[idx].split(',')
            idx += 1
            x = float(x_str)
            y = float(y_str)
            centers.append( (x,y) )

        # Points to check for max overlap:
        # 1) Each center
        # 2) Each intersection point of pairs of circles (if any)
        candidates = []
        candidates.extend(centers)

        # For each pair compute intersection points of circles radius=1
        for i in range(n):
            x1, y1 = centers[i]
            for j in range(i+1, n):
                x2, y2 = centers[j]
                dx = x2 - x1
                dy = y2 - y1
                d = math.hypot(dx, dy)
                if d > 2:
                    # no intersection
                    continue
                if d == 0:
                    # same center, no intersection points besides center
                    continue
                # calculate intersection points
                # formula from circle intersection
                a = d/2  # since radius=1, and circles intersect if d<=2
                h = math.sqrt(max(0.0, 1 - (a*a)))
                # midpoint between centers
                xm = x1 + dx/2
                ym = y1 + dy/2
                # offset vector (perpendicular)
                ox = -dy * (h/d)
                oy = dx * (h/d)
                p1 = (xm+ox, ym+oy)
                p2 = (xm-ox, ym-oy)
                candidates.append(p1)
                candidates.append(p2)

        # count max overlap
        max_overlap = 1 if n>0 else 0
        for px, py in candidates:
            count = 0
            for cx, cy in centers:
                dist = math.hypot(px - cx, py - cy)
                if dist <= 1+1e-10:
                    count +=1
            if count > max_overlap:
                max_overlap = count
        print(max_overlap)

if __name__ == '__main__':
    main()