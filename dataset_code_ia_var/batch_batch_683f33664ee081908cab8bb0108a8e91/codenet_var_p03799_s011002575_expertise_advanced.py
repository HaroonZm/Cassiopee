from sys import exit

def main():
    N, M = map(int, input().split())
    if 2 * N >= M:
        print(M // 2)
        exit()
    print(N + (M - 2 * N) // 4)

if __name__ == "__main__":
    main()