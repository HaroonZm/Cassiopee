import sys

go = 1
get_args = lambda: [int(z) for z in sys.stdin.readline().split()]
flip = lambda x: "#" if x else "."
while go:
    a, b = get_args()
    if not (a | b): go = 0; continue
    board = []
    for row in range(a):
        cell = [flip((row + col) % 2 == 0) for col in range(b)]
        board.append(''.join(cell))
    print('\n'.join(board) + '\n')