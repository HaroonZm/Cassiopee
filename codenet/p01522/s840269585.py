n,k = map(int,raw_input().split())
boats = [map(int,raw_input().split()) for i in range(k)]
r = input()
hate = [map(int,raw_input().split()) for i in range(r)]
blue = [0]*51
for i,j in hate:
	for boat in boats:
		if i in boat[1:] and j in boat[1:]:
			blue[i] = 1
			blue[j] = 1
print sum(blue)