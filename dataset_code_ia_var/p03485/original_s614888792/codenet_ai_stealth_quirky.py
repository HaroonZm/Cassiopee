from sys import stdin
get_val = lambda : map(int, stdin.readline().split())
stuff = list(get_val())
a = stuff.pop(0)
b = stuff[0]
mid = (a + b) / 2
ans = int(mid + 0.5) if (a + b) % 2 else int(mid)
print(ans)