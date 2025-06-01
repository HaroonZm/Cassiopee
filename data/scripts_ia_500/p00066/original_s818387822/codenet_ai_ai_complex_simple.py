import sys
from functools import reduce
def win(c, line):
	indices = list(range(9))
	check_line = lambda idxs: reduce(lambda acc, idx: acc and line[idx] == c, idxs, True)
	horizontal = any(map(check_line, [list(range(i, i+3)) for i in range(0,9,3)]))
	vertical = any(map(check_line, [list(range(i, i+7, 3)) for i in range(3)]))
	diag1 = check_line(list(range(0, 9, 4)))
	diag2 = check_line(list(range(2, 8, 2)))
	return horizontal or vertical or diag1 or diag2
for line in iter(sys.stdin.readline, ''):
	line = line.rstrip('\n')
	outcome = (lambda x: x if x in ['o', 'x'] else 'd')(next((c for c in ['o', 'x'] if win(c, line)), 'd'))
	print outcome