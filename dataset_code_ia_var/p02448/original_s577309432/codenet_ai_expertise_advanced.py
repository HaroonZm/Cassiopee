import sys

def main():
    from operator import itemgetter
    n = int(sys.stdin.readline())
    data = [(*map(int, (a, b, d)), c, e)
            for a, b, c, d, e in (line.split() for line in (sys.stdin.readline() for _ in range(n)))]
    for t in sorted(data, key=itemgetter(0, 1, 3, 2, 4)):
        print(t[0], t[1], t[2], t[3], t[4])

if __name__ == '__main__':
    main()