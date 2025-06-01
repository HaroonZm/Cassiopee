def hole(query, n):
    direction = query[0]
    a, b = [int(x)-1 for x in query[1:]]
    if direction == "xy":
        result = []
        for z in range(n):
            result.append(b * n + a + z * n * n)
    elif direction == "xz":
        result = [n*n*b + a + y*n for y in range(n)]
    else:
        # assuming direction == "yz"
        result = []
        for x in range(n):
            result.append(n*n*b + a*n + x)
    return result

while True:
    line = raw_input()
    n, h = [int(x) for x in line.split()]
    if n == 0:
        break
    bad = []
    for _ in range(h):
        query = raw_input().split()
        bad.extend(hole(query, n))
    bad_set = set(bad)  # unique bad cubes
    print n**3 - len(bad_set)  # remaining cubes not in holes