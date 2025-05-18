n = int(input())
response_list = [ int(v) for v in input().split() ]

ans = 0

mod = 10**9+7

if n % 2 == 0:
	right_list = [ 2*(i//2+1)-1 for i in range(n) ]
else:
	right_list = [ 2*((i+1)//2) for i in range(n) ]

if sorted(response_list) == right_list:

	if n % 2 == 0:
		ans = pow(2,n//2,mod)
	else:
		ans = pow(2,(n-1)//2,mod)

print(ans)