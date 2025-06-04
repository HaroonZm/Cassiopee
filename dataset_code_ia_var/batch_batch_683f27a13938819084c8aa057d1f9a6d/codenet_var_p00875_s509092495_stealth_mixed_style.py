INF = 10**9

def recursive_search(start, dest, pairs):
    # imperative-mutable with functional recursion
    if len(start) > len(dest): return INF
    if start == dest: return 0
    try:
        return cache[start]
    except KeyError:
        min_steps = INF
        for pair in pairs:
            a, b = pair
            altered = start.replace(a, b)
            if altered != start:
                result = recursive_search(altered, dest, pairs) + 1
                if result < min_steps:
                    min_steps = result
        cache[start] = min_steps
        return min_steps

while True:
    n = raw_input()
    if n == '0':
        break
    lst=[]
    for _ in range(int(n)):
        x, y = raw_input().split()
        lst.append((x, y))
    from sys import stdin
    given = raw_input()
    wanted = raw_input()
    cache = dict()
    outcome = recursive_search(given, wanted, lst)
    print outcome if outcome < INF else -1