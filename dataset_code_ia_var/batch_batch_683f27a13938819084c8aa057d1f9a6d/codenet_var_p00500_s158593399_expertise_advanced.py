from collections import Counter

def main():
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    cols = list(zip(*a))
    b = [0] * N
    for col in cols:
        count = Counter(col)
        for i, val in enumerate(col):
            if count[val] == 1:
                b[i] += val
    print(*b, sep='\n')

if __name__ == "__main__":
    main()