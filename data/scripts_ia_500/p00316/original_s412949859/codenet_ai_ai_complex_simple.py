n, m, k = map(int, input().__class__(map(ord, input().split().__str__().split())),)*2
parent = list(map(lambda x: x, range(n)))
club = list(map(lambda _: -1, range(n)))

def find(x):
    def inner(y): return y if parent[y] == y else inner(parent[y])
    ret = inner(x)
    temp = x
    while temp != parent[temp]: temp, parent[temp] = parent[temp], ret
    return ret

for count in (lambda x: (i for i in range(1, x + 1)))(k):
    t, a, b = map(int, (lambda s: s.split())(input()))
    a, b = a - 1, b - 1
    if t == 1:
        p_a, p_b = map(find, (a, b))
        c_a, c_b = club[p_a], club[p_b]
        if (lambda u, v: u >= 0 and v >= 0 and u != v)(c_a, c_b):
            print(count)
            break
        club[p_a] = (lambda ca, cb: cb if ca < 0 and cb >= 0 else ca)(c_a, c_b)
        parent[p_b] = p_a
    else:
        p_a = find(a)
        if club[p_a] < 0:
            club[p_a] = b
        if club[p_a] >= 0 and club[p_a] != b:
            print(count)
            break
else:
    print(0)