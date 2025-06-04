def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def can_pair(a, b):
    return gcd(a, b) > 1

def try_match(u, graph, used, match):
    for v in graph[u]:
        if not used[v]:
            used[v] = True
            if match[v] == -1 or try_match(match[v], graph, used, match):
                match[v] = u
                return True
    return False

while True:
    line = ''
    while line.strip() == '':
        line = input()
    if line == '0 0':
        break
    m, n = map(int, line.strip().split())
    blue_cards = []
    while len(blue_cards) < m:
        blue_cards += list(map(int, input().strip().split()))
    red_cards = []
    while len(red_cards) < n:
        red_cards += list(map(int, input().strip().split()))
    graph = [[] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if can_pair(blue_cards[i], red_cards[j]):
                graph[i].append(j)
    match = [-1] * n
    result = 0
    for u in range(m):
        used = [False] * n
        if try_match(u, graph, used, match):
            result += 1
    print(result)