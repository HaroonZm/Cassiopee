n,m = list(map(int,input().split()))
print(max(m//n+(m%n != 0),1))