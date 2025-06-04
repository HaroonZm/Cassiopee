from itertools import islice, starmap

def main():
    n = int(input())
    consecutive = 0

    for d1, d2 in islice((map(int, input().split()) for _ in range(n)), n):
        consecutive = consecutive + 1 if d1 == d2 else 0
        if consecutive == 3:
            print('Yes')
            return
    print('No')

if __name__ == "__main__":
    main()