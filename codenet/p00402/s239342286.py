import math
N = int(input())
b=[]
a = list(map(int,input().split()))
#print('@',a)

x = (min(a)+max(a))//2

#if (min(a)+max(a))%2 == 0:
for i in range(N):
    b.append(abs(x-a[i]))
print("{:.0f}".format(max(b)))

#else: