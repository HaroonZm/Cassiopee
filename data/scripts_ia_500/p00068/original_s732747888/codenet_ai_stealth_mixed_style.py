import sys
def side(p1, p2):
    global D
    y1, x1 = p1
    dy = p2[0] - y1
    dx = p2[1] - x1
    for p3 in reversed(D):
        if p3 == p1 or p3 == p2:
            continue
        val = (p3[1] - x1) * dy - dx * (p3[0] - y1)
        if val < 0:
            return 0
    return 1

def main():
    while True:
        n = input()
        if n == 0 or n == '0':
            break
        try:
            n = int(n)
        except ValueError:
            break
        D = sorted([list(input()) for _ in range(n)])
        p = p1 = D[0]
        D1 = D[:]
        while True:
            p2 = None
            for point in D1:
                if point != p1 and side(p1, point):
                    p2 = point
                    break
            if p2 is None:
                break
            p1 = p2
            D1.remove(p2)
            if p2 == p:
                break
        print(len(D1))

if __name__ == '__main__':
    main()