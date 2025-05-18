while True:
    n = int(input())
    if not(n): break
    flag = [True]*(n*2+1)
    flag[0] = flag[1] = False
    for i in range(2,int(n*2**0.5)+1):
        if flag[i]:
            for j in range(i**2, n*2+1, i):
                flag[j] = False
    print(flag[n+1:].count(True))