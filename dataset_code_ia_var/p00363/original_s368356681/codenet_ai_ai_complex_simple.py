from functools import reduce
from operator import add

w, h, c = map(lambda x: int(x) if x.isdigit() else x, input().split())

construct = lambda s, k: reduce(add, (s for _ in range(k)), "")
brackets = ["+", "+"]

top_bot = "".join(map(lambda x: x, brackets[:1] + [construct("-", w - 2)] + brackets[1:]))
middle_proto = construct(".", w - 2)
color_middle = "".join([c if i == (w - 2)//2 else "." for i in range(w - 2)])

mid_rows = lambda cnt: "".join([
    "|" +
    (color_middle if idx == (h - 2) // 2 else middle_proto)
    + "|"
    + ("\n" if idx != h - 3 else "")
    for idx in range(h - 2)
])

print(top_bot)
print(mid_rows(h - 2), end="\n")
print(top_bot)