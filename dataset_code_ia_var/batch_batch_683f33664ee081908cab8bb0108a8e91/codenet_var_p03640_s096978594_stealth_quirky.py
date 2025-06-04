from sys import stdin

def grab():
    return list(map(int, stdin.readline().split()))

# idiosyncratic variable names
HH, WW = grab()
N = int(stdin.readline())
Alist = grab()

Board = [[None]*WW for _ in [0]*HH]

colz = iter(sum([[c+1]*x for c,x in enumerate(Alist)], []))
i = j = 0
flat_count = 0

def zig(x): return x[::-1]

for row in range(HH):
    for col in range(WW):
        try:
            Board[row][col] = next(colz)
        except StopIteration:
            Board[row][col] = 0  # should not occur

for idx, slicez in enumerate(Board):
    print(*zig(slicez) if idx&1 else slicez)