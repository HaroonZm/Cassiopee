n,k = map(int,raw_input().split())
boats = [map(int,raw_input().split()) for i in range(k)]
r = input()
hate = [map(int,raw_input().split()) for i in range(r)]
blue = []
for i,j in hate:
	for boat in boats:
		if i in boat[1:] and j in boat[1:]:
			if i not in blue: blue.append(i)
			if j not in blue: blue.append(j)
print len(blue)