n = int(input())
a = list(map(int,input().split()))

even = []
odd = []
for i in range(0,n):
	if i % 2 == 0:
		odd.append(a[i])
	else:
		even.append(a[i])

res = []
if n % 2 == 0:
	even = reversed(even)
	res.extend(even)
	res.extend(odd)
else:
	odd = reversed(odd)
	res.extend(odd)
	res.extend(even)

print(" ".join(map(str,res)))