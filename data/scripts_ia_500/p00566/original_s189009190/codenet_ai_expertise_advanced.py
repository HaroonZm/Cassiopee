h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

# Pré-calcul des positions pondérées pour optimiser les calculs
positions = [(m, n, x) for m, row in enumerate(a) for n, x in enumerate(row) if x]

ans = min(
    sum(min(abs(i - m), abs(j - n)) * x for m, n, x in positions)
    for i in range(h) for j in range(w)
)
print(ans)