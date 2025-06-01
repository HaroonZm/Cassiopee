import sys
def main():
    while True:
        try:
            n = int(sys.stdin.readline())
            if n == 0:
                break
            d = []
            for _ in range(n):
                line = sys.stdin.readline()
                values = list(map(int, line.strip().split()))
                d.append(values)
            w = 0
            for d1 in d:
                s = sum([d2[0] for d2 in d if d2[1] <= d1[1] < d2[2]])
                if s > w:
                    w = s
            if w < 151:
                print("OK")
            else:
                print("NG")
        except:
            break
if __name__ == "__main__":
    main()