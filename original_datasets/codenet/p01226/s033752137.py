for _ in range(input()):
	if _ > 0: print
	H,W = map(int,raw_input().split())
	A = [list(raw_input()) for i in range(H)]
	for h in range(H):
		for w in range(W):
			if A[h][w] in "^<v>":
				x,y = w,h
				d = A[h][w]
				A[h][w] = "."
	input()
	cmd = raw_input()
	for c in cmd:
		if   c == "S":
			if d == "^":
				for h in range(y-1,-1,-1):
					if A[h][x] == "*":
						A[h][x] = "."
						break
					if A[h][x] == "#":
						break
			if d == "<":
				for w in range(x-1,-1,-1):
					if A[y][w] == "*":
						A[y][w] = "."
						break
					if A[y][w] == "#":
						break
			if d == "v":
				for h in range(y+1,H):
					if A[h][x] == "*":
						A[h][x] = "."
						break
					if A[h][x] == "#":
						break
			if d == ">":
				for w in range(x+1,W):
					if A[y][w] == "*":
						A[y][w] = "."
						break
					if A[y][w] == "#":
						break
		elif c == "U":
			d = "^"
			if y-1 >= 0 and A[y-1][x] == ".":
				y = y-1
		elif c == "L":
			d = "<"
			if x-1 >= 0 and A[y][x-1] == ".":
				x = x-1
		elif c == "D":
			d = "v"
			if y+1 <  H and A[y+1][x] == ".":
				y = y+1
		elif c == "R":
			d = ">"
			if x+1 <  W and A[y][x+1] == ".":
				x = x+1
	A[y][x] = d
	for h in range(H):
		print "".join(A[h])