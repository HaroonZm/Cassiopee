from functools import reduce

n=int(input())
a=[int(x) for x in input().split()]
def prefix_gen(l):
    s=0
    res=[s]
    for x in l:
        s+=x
        res+=[s]
    return res
sum_a=prefix_gen(a)[1:-1]

total=reduce(lambda x,y:x+y,a)
for i in range(len(sum_a)):
    sum_a[i]=abs(total/2-sum_a[i])
minval=min(*sum_a)
print(int(minval*2))