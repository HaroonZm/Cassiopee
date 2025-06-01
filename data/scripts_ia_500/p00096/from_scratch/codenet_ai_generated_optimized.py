from sys import stdin

# Pré-calculer toutes les sommes possibles de a + b (avec 0 <= a,b <= 1000)
max_val = 1000
ab_counts = [0] * (2 * max_val + 1)
for a in range(max_val + 1):
    for b in range(max_val + 1):
        ab_counts[a + b] += 1

for line in stdin:
    n = line.strip()
    if not n.isdigit():
        continue
    n = int(n)
    count = 0
    # pour chaque somme possible de c + d, on regarde combien de (a+b) peuvent compléter à n
    for cd_sum in range(max(0, n - 2*max_val), min(n, 2*max_val) + 1):
        count += ab_counts[cd_sum] * ab_counts[n - cd_sum]
    print(count)