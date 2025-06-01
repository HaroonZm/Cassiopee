n, m = map(int, input().split())
intr = list(map(int, (input() for _ in range(n))))
crit = list(map(int, (input() for _ in range(m))))
vote = [next((1 for c in crit if intr_i <= c), 0) for intr_i in intr]
print(vote.index(max(vote)) + 1)