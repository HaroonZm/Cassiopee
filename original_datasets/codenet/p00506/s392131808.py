from fractions import gcd
n=input()
L=map(int,raw_input().split())
g=reduce(gcd,L)
print "\n".join(map(str,filter(lambda x:g%x==0,range(1,g+1))))