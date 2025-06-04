def grundy(w, b):
    # Based on analysis, the grundy number for each pile depends only on the parity of (b - w)
    return (b - w) % 2

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    xor_sum = 0
    for _ in range(n):
        w, b = map(int, input().split())
        xor_sum ^= grundy(w, b)
    print(0 if xor_sum != 0 else 1)

if __name__ == "__main__":
    main()