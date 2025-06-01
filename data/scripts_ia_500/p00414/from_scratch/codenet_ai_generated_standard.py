L,N=map(int,input().split())
s=input()
count_o=s.count('o')
for _ in range(N):
    count_o = 2*count_o -1 if count_o>1 else count_o
print(L + 3*(count_o -1) if count_o>1 else L)