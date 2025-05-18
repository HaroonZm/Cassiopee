n,m = map(int,input().split())
x = 1900*m + 100*(n-m)  #１提出分の時間
print(x*(2**m)) #一番最後にACする時間