n = int(raw_input())
hanako = 0
taro = 0
for i in range(n):
	t,h = raw_input().split()
	if h == t:
		hanako += 1
		taro += 1
	elif h < t:
		taro += 3
	else:
		hanako += 3
print " ".join(map(str,[taro, hanako]))