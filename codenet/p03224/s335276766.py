N=int(input())
chk = (2*N)**(1/2)
k = chk//1
if N  != k*(k+1)//2:
    print("No")
else:
    print("Yes")
    k = int(k)
    print(k+1)
    ans_list = [[0 for i in range(k)] for j in range(k+1)]
    W1 = 0
    H1 = 0
    W2 = 0
    H2 = 1
    for i in range(N):
        ans_list[H1][W1] = i+1
        ans_list[H2][W2] = i+1
        if H1 == W1 :
            H1 = 0
            W1 =W1+1
            H2 = W1+1
            W2 = 0
        else:
            H1 += 1
            W2 += 1
    for i in range(k+1):
        print(str(k)+" "+" ".join(str(n) for n in ans_list[i]))