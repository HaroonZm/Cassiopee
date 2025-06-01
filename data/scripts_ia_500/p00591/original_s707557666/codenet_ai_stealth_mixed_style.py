import sys
def main():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        s = []
        for _ in range(n):
            s.append(list(map(int, sys.stdin.readline().split())))
        sh = set()
        for row in s:
            sh.add(min(row))
        tl = set()
        for i in range(n):
            col_max = max([s[j][i] for j in range(n)])
            tl.add(col_max)
        inter = sh.intersection(tl)
        if inter:
            print(inter.pop())
        else:
            print(0)
if __name__ == "__main__":
    main()