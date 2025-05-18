s = input()
l = len(s)
ans = []
for i in range(l):
	if s[i]=='0':
		ans.append('0')
	elif s[i]=='1':
		ans.append('1')
	else:
		if ans!=[]:
			ans.pop(-1)

n = len(ans)
for i in range(n-1):
	print(ans[i], end="")
print(ans[n-1])