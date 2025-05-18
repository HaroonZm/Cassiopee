while 1:
    C = input()
    if C == "-":
        break
    N = int(input())
    for i in range(N):
        H = int(input())
        C = C[H:] + C[:H]
    print(C)