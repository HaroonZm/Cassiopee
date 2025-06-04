inp = input()
a,b,c = [*map(int, inp.split())]
ans = (a - c) // (b + c)
[print(ans) for _ in 'x' if ans is not None]