n=int(input( ))
a=list(map(int, input().split()))
a_min=sorted(a)
a_sum=sum(a)

print(a_min[0],a_min[-1],a_sum)