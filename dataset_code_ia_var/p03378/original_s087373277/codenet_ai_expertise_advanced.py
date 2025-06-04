from bisect import bisect_right

def main():
    *_, X = map(int, input().split())
    A = list(map(int, input().split()))

    idx = bisect_right(A, X)
    print(min(idx, len(A) - idx))

if __name__ == "__main__":
    main()