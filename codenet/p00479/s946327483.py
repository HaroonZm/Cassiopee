N=input()
for i in range(input()):
    a,b=map(int,raw_input().split())
    print min(a-1,N-a,b-1,N-b)%3+1