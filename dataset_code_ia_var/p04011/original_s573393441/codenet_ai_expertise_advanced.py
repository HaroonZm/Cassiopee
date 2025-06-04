from functools import partial

def compute_cost(n: int, k: int, x: int, y: int) -> int:
    return (common := min(n, k)) * x + (rest := max(n - k, 0)) * y

map_input = partial(map, int, map(str.strip, [input(), input(), input(), input()]))
print(compute_cost(*map_input()))