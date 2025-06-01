N=int(raw_input())
for __ in xrange(int(raw_input())):
    a,b=map(int,raw_input().split())
    r=(a-1,N-a,b-1,N-b)
    print(sum(r)%3+1)