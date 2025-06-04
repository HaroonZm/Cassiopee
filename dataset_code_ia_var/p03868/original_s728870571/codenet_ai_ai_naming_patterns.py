N, *edges = map(int, open(0))
result, balance = 1, 0
edge_events = [(edge_value, 2 * (index < N) - 1) for index, edge_value in enumerate(edges)]
for event_value, delta in sorted(edge_events):
    if balance * delta < 0:
        result = abs(result * balance) % (10**9 + 7)
    balance += delta
print(result)