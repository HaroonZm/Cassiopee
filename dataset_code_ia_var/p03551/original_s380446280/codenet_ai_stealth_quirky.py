from functools import reduce
A,B=[int(x) for x in input().split()]
calc=lambda a,b:((a-b)*100+b*1900)*(reduce(lambda x,_:x*2,range(b),1) if b else 1)
print(calc(A,B))