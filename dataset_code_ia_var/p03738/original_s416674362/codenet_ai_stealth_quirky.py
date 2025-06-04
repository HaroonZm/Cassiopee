from sys import stdin
x, y = map(int, [stdin.readline(), stdin.readline()])
_ = ["LESS", "EQUAL", "GREATER"]
print(_[(x > y) * 2 + (x == y)]) if not x < y else print(_[0])