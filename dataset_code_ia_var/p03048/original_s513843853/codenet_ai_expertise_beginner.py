import sys

def solve(R, G, B, N):
    count = 0
    i = 0
    while i <= N:
        j = 0
        while j <= N:
            x = N - i - j
            if x >= 0 and x % B == 0:
                count += 1
            j += G
        i += R
    print(count)

def main():
    inputs = sys.stdin.read().split()
    R = int(inputs[0])
    G = int(inputs[1])
    B = int(inputs[2])
    N = int(inputs[3])
    solve(R, G, B, N)

if __name__ == "__main__":
    main()