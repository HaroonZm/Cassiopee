delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
def ds(here, lb, ub, field):
	if field[here[1]][here[0]] == "#":
		return 0
	result = 1
	field[here[1]][here[0]] = "#"
	for dx, dy in delta:
		next = (here[0]+dx,here[1]+dy)
		if lb[0] <= next[0] < ub[0] and lb[1] <= next[1] < ub[1]:
			result += ds(next, lb, ub, field)
	return result
while 1:
	W, H = map(int,raw_input().split(" "))
	if W == H == 0:
		break
	floor = [list(raw_input()) for i in range(H)]
	start = None
	for i in range(H):
		for j in range(W):
			if floor[i][j] == "@":
				start = (j,i)
				break
		if start is not None:
			break
	print ds(start,(0,0),(W,H),floor)