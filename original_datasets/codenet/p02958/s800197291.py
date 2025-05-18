n = int(input())
s = list(map(int, input().split()))

r = "YES"
cnt = 0
for i in range(n - 1):
	if(s[i + 1] - s[i] < 1):
		cnt += 1
		if(cnt == 1):
			a_value = s[i]
			a_index = i
		elif(cnt == 2):
			b_value = s[i + 1]
			b_index = i + 1
		elif(cnt > 2):
			r = "NO"
			break

if(cnt == 1):
	r = "NO"
elif(cnt == 2):
	s[a_index] = b_value
	s[b_index] = a_value
	if(s[a_index + 1] - s[a_index] < 1) or (s[b_index] - s[b_index - 1] < 1):
		r = "NO"

print (r)