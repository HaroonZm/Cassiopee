import sys
 
n = int(sys.stdin.readline())
s = list(sys.stdin.readline())

it = s[0]
w = 0
e = s[1:].count('E')

m = e
j = 0

for i in range(1, len(s)):
	if it == 'W':
		w = w + 1

	it = s[i]

	if it == 'E':
		e = e - 1

	m2 = w + e
	if m2 < m:
		m = m2
		j = i
print(m)