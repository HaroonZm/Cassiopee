def main():
    n = int(input())
    while True:
        if n == 0:
            break
        dmax = -1
        id = None
        i = 0
        while i < n:
            line = input().strip()
            if line:
                parts = line.split()
                p, d1, d2 = int(parts[0]), int(parts[1]), int(parts[2])
                if (d1 + d2) > dmax:
                    id, dmax = p, d1 + d2
                i += 1
        print(f"{id} {dmax}")
        n = int(input())
main()