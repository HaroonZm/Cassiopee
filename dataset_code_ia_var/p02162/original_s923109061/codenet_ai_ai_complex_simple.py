from functools import reduce

(*a,), = [tuple(map(int, input().split()))]
dispatch = {
    True: lambda x, y: ["Draw", "Alice", "Bob"][(x > y) - (x < y)],
    False: lambda x, y: ["Draw", "Alice", "Bob"][(x > y) - (x < y)]
}
i, j = map(lambda v: v == -1, a[2:])
which = reduce(lambda acc, x: acc or x, (i, j))
x, y = (a[0], a[1]) if which else (a[2], a[3])
print(dispatch[which](x, y))