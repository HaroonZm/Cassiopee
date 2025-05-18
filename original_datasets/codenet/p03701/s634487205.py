import sys

N = int(input())
s = list()
for i in range(N):
	s.append(int(input()))

s.sort(reverse=True)

point = sum(s)
l = len(s)
i = 0

while i < l:
	if point % 10 != 0:
		print(point)
		sys.exit()
	if not s == []:
		for x in reversed(list(s)):
			if not x % 10 == 0:
				point -= s.pop(s.index(x))
				break
	i += 1

print("0")