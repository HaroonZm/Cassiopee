while True:
    N,I,J = map(int,input().split())
    if N == 0:
        break
    L = [I]*N
    for i in range(N-2,-1,-1):
        if L[i+1]<=2**(i+1):
            L[i] = 2**(i+1) - L[i+1] + 1
        else:
            L[i] = L[i+1] - 2**(i+1)
    ans = ""
    for i in range(N):
        if L[i] > 2**i:
            if J <= 2**(N-i-1):
                ans = ans+"R"
            else:
                ans = ans+"L"
                J -= 2**(N-i-1)
        else:
            if J <= 2**(N-i-1):
                J = 2**(N-1-i)-J+1
                ans = ans + "L"
            else:
                J -= 2**(N-i-1)
                J = 2**(N-1-i)-J+1
                ans = ans + "R"
    print(ans)