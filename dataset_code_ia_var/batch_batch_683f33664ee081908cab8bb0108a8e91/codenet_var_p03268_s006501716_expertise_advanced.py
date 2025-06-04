from sys import stdin

def main():
    N, K = map(int, stdin.readline().split())
    q, r = divmod(K, 2)
    if r:
        print(pow(N // K, 3))
    else:
        n_k = N // K
        n_hk = N // (K // 2)
        print(pow(n_k, 3) + pow(n_hk - n_k, 3))

if __name__ == "__main__":
    main()