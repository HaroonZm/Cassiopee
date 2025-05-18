from itertools import chain
explosion = [i for i in range(-3, 4) if i] + [0] * 6

def bomb(x, y):
	field[y][x] = 0
	for dx, dy in zip(explosion, reversed(explosion)):
		nextX = x + dx
		nextY = y + dy
		if nextX in range(0, 8) and nextY in range(0, 8):
			if field[nextY][nextX] == 1:
				bomb(nextX, nextY)
			field[nextY][nextX] = 0

for i in xrange(input()):
	raw_input()
	field = [[int(c) for c in raw_input()] for j in range(8)]
	x = input() - 1
	y = input() - 1
	bomb(x, y)
	print "Data %d:" % (i + 1)
	for f in field:
		print "".join(str(i) for i in f)