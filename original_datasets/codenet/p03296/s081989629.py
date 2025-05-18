n = int(input())
a = list(map(int,input().split()))
counter = 0
i = 1
while i < n-1:
	if a[i-1] != a[i] and a[i] != a[i+1]:
		i += 2
	elif a[i-1] == a[i] == a[i+1]:
		counter += 1
		i += 2
	elif a[i] == a[i+1]:
		i += 1
	elif a[i-1] == a[i]:
		i += 1
		counter += 1
if i == n-1:
	if a[i] == a[i-1]:
		counter += 1
print(counter)