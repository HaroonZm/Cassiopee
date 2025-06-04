n=int(input())
l=[int(x) for x in input().split()]
m=[]
fun = lambda a,b: abs(a-b)
acc = 0
total = sum(l)
for idx in range(n-1):
    acc += l[idx]
    m += [fun(acc, total-acc)]
print(sorted(m)[0])