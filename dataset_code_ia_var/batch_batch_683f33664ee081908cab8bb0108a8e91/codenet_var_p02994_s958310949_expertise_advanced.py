from operator import itemgetter

def main():
    N, L = map(int, input().split())
    total_sum = N * (2 * L + N - 1) // 2

    first = L
    last = L + N - 1

    if first > 0:
        result = total_sum - first
    elif last < 0:
        result = total_sum - last
    else:
        result = total_sum

    print(result)

if __name__ == "__main__":
    main()