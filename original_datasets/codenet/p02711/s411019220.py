import sys
import math

n = int(input())
#tmp = input().split()
#n,m,k = list(map(lambda a: int(a), tmp))

if(n%10==7):
	print("Yes")
	sys.exit()
n-=n%10
n/=10
if(n%10==7):
	print("Yes")
	sys.exit()
n-=n%10
n/=10
if(n==7):
	print("Yes")
	sys.exit()
print("No")