a=int(input())
a_li=list(map(int, input().split()))
b=int(input())
b_li=list(map(int, input().split()))
answer=sorted(set(a_li+b_li))
ans=[print(i) for i in answer]