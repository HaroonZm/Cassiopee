import sys
input = sys.stdin.readline

def main():
    while True:
        n, w, d = map(int, input().split())
        if w == 0:
            break
        cuts = [list(map(int, input().split())) for i in range(n)]
        cakes = [(w,d,w*d)]
        for cut in cuts:
            p, s = cut
            w, d, wd = cakes.pop(p-1)
            s = s % (w*2+d*2)
            if s > w+d:
                s -= w+d
            if 0 < s and s < w:
                w1 = min(s, w-s)
                w2 = w - w1
                cakes.append((w1, d, w1*d))
                cakes.append((w2, d, w2*d))
            else:
                d1 = min(w+d-s, s-w)
                d2 = d - d1
                cakes.append((w, d1, w*d1))
                cakes.append((w, d2, w*d2))
        cakes = sorted(cakes, key=lambda x:x[2])
        len_ = len(cakes)
        for i in range(len_):
            _,__,area = cakes[i]
            print(area, end="")
            if i != len_ - 1:
                print(" ",end="")
            else:
                print()

if __name__ == "__main__":
    main()