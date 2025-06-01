def main():
    while 1:
        try:
            v = int(input())
        except ValueError:
            continue
        if not v:
            return
        c = 0
        f = None
        i = 1
        while i <= 12:
            line = input().split()
            if len(line) != 2:
                continue
            m, n = map(int, line)
            c = c + (m - n)
            if f is None:
                if c >= v:
                    f = i
            i += 1
        print(f if f is not None else "NA")

if __name__ == "__main__":
    main()