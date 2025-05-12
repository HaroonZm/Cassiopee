def string_to_float(s):
    return list(map(float, s.split()))

def solve():
    from sys import stdin
    lines = stdin.readlines()
    from itertools import combinations
    from math import acos, pi
    from cmath import phase
    from bisect import insort
    
    while True:
        n = int(lines[0])
        if n == 0:
            break
        
        circles = enumerate(map(string_to_float, lines[1:1+n]))
        cross_data = [[] for i in range(n)]
        included = [False] * n
        r_sum = sum(map(lambda x: float(x.split()[2]), lines[1:1+n]))
        ans = 2 * pi * r_sum
        
        for c1, c2 in combinations(circles, 2):
            n1, xyr1 = c1
            n2, xyr2 = c2
            if included[n1] or included[n2]:
                continue
            
            x1, y1, r1 = xyr1
            x2, y2, r2 = xyr2
            cn1 = x1 + y1 * 1j
            cn2 = x2 + y2 * 1j
            
            v12 = cn2 - cn1
            d = abs(v12)
            if d >= r1 + r2:
                continue
            elif  d <= abs(r1 - r2):
                if r1 < r2:
                    ans -= 2 * pi * r1
                    included[n1] = True
                else:
                    ans -= 2 * pi * r2
                    included[n2] = True
                continue
            
            a = acos((r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d))
            t = phase(v12)
            s = t - a
            e = t + a
            cd = cross_data[n1]
            if s >= -pi and e <= pi:
                insort(cd, (s, -1))
                insort(cd, (e, 1))
            elif s < -pi:
                insort(cd, (s + 2 * pi, -1))
                insort(cd, (pi, 1))
                insort(cd, (-pi, -1))
                insort(cd, (e, 1))
            else:
                insort(cd, (s, -1))
                insort(cd, (pi, 1))
                insort(cd, (-pi, -1))
                insort(cd, (e - 2 * pi, 1))
            
            a = acos((r2 ** 2 + d ** 2 - r1 ** 2) / (2 * r2 * d))
            t = phase(-v12)
            s = t - a
            e = t + a
            cd = cross_data[n2]
            if s >= -pi and e <= pi:
                insort(cd, (s, -1))
                insort(cd, (e, 1))
            elif s < -pi:
                insort(cd, (s + 2 * pi, -1))
                insort(cd, (pi, 1))
                insort(cd, (-pi, -1))
                insort(cd, (e, 1))
            else:
                insort(cd, (s, -1))
                insort(cd, (pi, 1))
                insort(cd, (-pi, -1))
                insort(cd, (e - 2 * pi, 1))
        
        radius = map(lambda x: float(x.split()[2]), lines[1:1+n])
        flag = 0
        for cd, r in zip(cross_data, radius):
            for ang, f in cd:
                if flag == 0:
                    s = ang
                flag += f
                if flag == 0:
                    ans -= r * (ang - s)
                    
        print(ans)
        
        del lines[:1+n]

solve()