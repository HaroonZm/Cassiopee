def main():
    import sys
    input = sys.stdin.readline

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        diffs = []
        for i in range(n):
            diff = (b[i] - a[i]) % m
            diffs.append(diff)

        ops = 0
        i = 0
        while i < n:
            if diffs[i] == 0:
                i += 1
                continue
            current = diffs[i]
            j = i
            while j < n and diffs[j] == current:
                diffs[j] = 0
                j += 1
            ops += current
            i = j

        print(ops)

if __name__ == "__main__":
    main()