from sys import exit

def main():
    N, K = map(int, input().split())

    if not N or K == 1:
        print(0)
        exit()

    N %= K
    print(min(N, K - N))

if __name__ == "__main__":
    main()