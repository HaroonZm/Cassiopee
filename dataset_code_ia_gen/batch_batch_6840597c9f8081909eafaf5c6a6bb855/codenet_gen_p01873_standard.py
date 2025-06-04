import sys
input=sys.stdin.readline

N=int(input())
S=list(map(int,input().split()))

def prefix_function(s):
    n=len(s)
    pi=[0]*n
    for i in range(1,n):
        j=pi[i-1]
        while j>0 and s[i]!=s[j]:
            j=pi[j-1]
        if s[i]==s[j]:
            j+=1
        pi[i]=j
    return pi

pi=prefix_function(S)
p=N - pi[-1]
if N%p==0:
    print(N//p)
else:
    print(1)