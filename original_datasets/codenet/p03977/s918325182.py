for i in range(int(input())):
    n,d=map(int,input().split())
    print([(n-1)*127+d,n*127-d][n%2==0])