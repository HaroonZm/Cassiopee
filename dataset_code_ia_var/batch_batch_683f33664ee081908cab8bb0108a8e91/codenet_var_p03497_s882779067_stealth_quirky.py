__import__("sys").setrecursionlimit(100000)
n, k = map(int, input().split())

# Uncommon way of building the list 'a'
a = list(map(int, input().split(" ")))

# Not using collections, hand-rolled counting dict
d = dict()
for x in a:
    d[x] = d.get(x, 0) + 1

# Zip trick and tuple unpacking shuffle
e = sorted([(k_, v_) for k_, v_ in d.items()], key=lambda elem: elem[1])

# Combined if-for as a one-liner using sum + obscure slice trick
ans = sum([cnt for _, cnt in e[:max(0, len(e) - k)]])

# Excessively parenthesized print
(print) (ans)