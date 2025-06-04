from itertools import count, islice

L = range(1, 100000)
TRI_NUM = set(i * (i + 1) // 2 for i in range(1, 100000))

def process_case(b):
    if sum(b) not in TRI_NUM:
        print(-1)
        return

    b = b[:]
    ans = 0
    ideal = tuple(islice(L, len(b)))

    for ans in range(10001):
        if tuple(b) == ideal:
            print(ans)
            return
        b = [v - 1 for v in b] + [len(b)]
        b = [v for v in b if v != 0]

    print(-1)

def main():
    import sys
    input_iter = iter(sys.stdin.readline, '')
    for line in input_iter:
        N_str = line.strip()
        if not N_str:
            continue
        N = int(N_str)
        if N == 0:
            break
        b = list(map(int, next(input_iter).split()))
        process_case(b)

if __name__ == "__main__":
    main()