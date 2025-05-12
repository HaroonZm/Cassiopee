n,k = map(int,raw_input().split())
boats = [map(int,raw_input().split())[1:] for i in range(k)]
r = input()
hate = [map(int,raw_input().split()) for i in range(r)]
blue = [0]*51
for i,j in hate:
	for boat in boats:
		if i in boat and j in boat:
			blue[i] = 1
			blue[j] = 1
print sum(blue)