from itertools import count
for _ in count():
 try:n=int(input())
 except:exit()
 print(sum((n-i)*x for i,x in enumerate(sorted(int(x)for x in input().split()))))