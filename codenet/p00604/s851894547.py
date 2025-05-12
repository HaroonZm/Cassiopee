while True:
    try:
        n=input()
    except EOFError:
        break
    L=sorted(map(int,raw_input().split()))
    for i in range(1,n):
        L[i]+=L[i-1]
    print sum(L)