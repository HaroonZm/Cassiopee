N=int(input())
A=set(map(int,input().split()[1:]))
B=set(map(int,input().split()[1:]))
C=set(map(int,input().split()[1:]))

result=(C - A) | (B & C)
print(len(result))