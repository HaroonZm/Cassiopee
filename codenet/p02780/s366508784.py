def main():
    N, K = map(int, input().split())
    dice = [int(p) for p in input().split()]
    S = [ 0 for i in range(N+1)]

    for i in range(1, N+1):
        S[i] = S[i-1] + (dice[i-1]+1)/2.0

    max_E = 0
    for i in range(N-K+1):
       E = S[i+K] - S[i]
       if max_E < E:
           max_E = E

    print(max_E)
    
if __name__ == "__main__":
    main()