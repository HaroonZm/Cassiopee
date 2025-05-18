n,m = map(int, input().split())
ink = list(map(int, input().split()))
ink.sort()
array = [0 for i in range(n+1)]

array[1] = 1
for i in range(2, n+1):
	if i in ink:
		array[i] = 1
	else:
		mini = i
		for j in ink[::-1]:
			if j < i:
				if mini > 1 + array[i-j]:
					mini = 1 + array[i-j]
		array[i] = mini
print(array[n])