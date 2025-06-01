def main():
    import sys
    while True:
        n = int(sys.stdin.readline())
        if n == 0: break
        maxind = 0
        maxnum = 0
        for i in range(n):
            line = sys.stdin.readline()
            a, b, c = map(int, line.split())
            if maxnum < b + c:
                maxind = a
                maxnum = b + c
        print(maxind, maxnum)
if __name__ == "__main__":
    main()