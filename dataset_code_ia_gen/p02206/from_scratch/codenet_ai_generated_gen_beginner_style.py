N, K = map(int, input().split())

# On cherche le montant maximal x que Segtree (personne 1) peut recevoir,
# sous la contrainte que pour chaque i >= 2,
# la récompense du membre i est au moins la moitié entière de celle de i-1.

def is_possible(x):
    total = 0
    current = x
    for _ in range(N):
        total += current
        current = current // 2
        if total > K:
            return False
    return total <= K

left = 0
right = K

while left < right:
    mid = (left + right + 1) // 2
    if is_possible(mid):
        left = mid
    else:
        right = mid - 1

print(left)