from operator import itemgetter

def hole(query, n):
    dir, a, b = query[0], *(int(x) - 1 for x in query[1:])
    match dir:
        case "xy":
            return [b * n + a + z * n**2 for z in range(n)]
        case "xz":
            return [n**2 * b + a + y * n for y in range(n)]
        case _:
            return [n**2 * b + a * n + x for x in range(n)]

while True:
    if (tokens := input().split()) and (n := int(tokens[0])) == 0:
        break
    h = int(tokens[1])
    bad = set()
    for _ in range(h):
        query = input().split()
        bad.update(hole(query, n))
    print(n**3 - len(bad))