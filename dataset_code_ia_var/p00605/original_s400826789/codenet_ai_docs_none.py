while True:
    N, K = map(int, input().split())
    if N == 0:
        break
    S = [0] + list(map(int, input().split()))
    flag = True
    for _ in range(N):
        B = list(map(int, input().split()))
        for i, b in enumerate(B):
            S[i+1] -= b
            if S[i+1] < 0:
                flag = False
                break
    print("Yes" if flag else "No")