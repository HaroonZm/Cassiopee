from itertools import islice, accumulate

n, k = map(int, input().split())
p = list(map(int, input().split()))

# Calcul des sommes glissantes optimisé à l'aide de itertools.accumulate et compréhension de liste
prefix_sums = list(accumulate(p, initial=0))
window_sums = [prefix_sums[i + k] - prefix_sums[i] for i in range(n - k + 1)]

# Affichage avec calcul final, sans variable temporaire inutile
print((max(window_sums) + k) / 2.0)