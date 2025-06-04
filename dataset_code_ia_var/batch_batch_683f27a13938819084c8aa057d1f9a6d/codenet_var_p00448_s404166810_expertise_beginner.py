def main():
    while True:
        line = input()
        if line == '0 0':
            break
        parts = line.split()
        r = int(parts[0])
        col_input = []
        for i in range(r):
            col_input.append(input().split())
        # Transpose to get columns
        columns = list(zip(*col_input))
        d = []
        for x in columns:
            s = ''.join(x)
            d.append(int(s, 2))
        max_a = 0
        for m in range(1 << (r-1)):
            t = 0
            for s in d:
                c = bin(m ^ s).count('1')
                if c > r // 2:
                    t += c
                else:
                    t += r - c
            if t > max_a:
                max_a = t
        print(max_a)

if __name__ == '__main__':
    main()