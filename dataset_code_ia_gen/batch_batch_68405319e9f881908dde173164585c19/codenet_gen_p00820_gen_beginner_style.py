import sys

def count_representations(n):
    count = 0
    max_a = int(n**0.5)
    for a in range(1, max_a+1):
        a_sq = a*a
        if a_sq == n:
            count += 1
        elif a_sq < n:
            max_b = int((n - a_sq)**0.5)
            for b in range(a, max_b+1):
                b_sq = b*b
                s = a_sq + b_sq
                if s == n:
                    count += 1
                elif s < n:
                    max_c = int((n - s)**0.5)
                    for c in range(b, max_c+1):
                        c_sq = c*c
                        t = s + c_sq
                        if t == n:
                            count += 1
                        elif t < n:
                            max_d = int((n - t)**0.5)
                            for d in range(c, max_d+1):
                                d_sq = d*d
                                u = t + d_sq
                                if u == n:
                                    count += 1
    return count

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    print(count_representations(n))