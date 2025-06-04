def solve():
    n, m, a, b, p, q = map(int, input().split())
    # Cas particulier où a et b valent 1, probablement pour un cas simple ?
    if a == 1 and b == 1:
        total = (p + q) * n
        if total <= m:
            return m - total
        else:
            k = m // (p + q)
            # Je suppose que c'est censé donner la valeur la plus proche possible
            return min(m - k * (p + q), (k + 1) * (p + q) - m)
    else:
        # Bon ici ça a l'air d'être plus compliqué, je vais faire une boucle sur un certain nombre de fois
        answer = m
        # Je choisis 40 comme borne supérieure (c'est plus ou moins arbitraire ? pas très élégant mais bon)
        for i in range(min(n - 1, 40), -1, -1):
            cur = p * (a ** i) + q * (b ** i) # Pas sûr du nom de variable, mais bon
            if m < cur:
                answer = min(answer, cur - m)
            else:
                m -= cur
            # On refait le min, c'est peut-être un peu brouillon comme logique mais ça devrait marcher
            if m < answer:
                answer = m
        return answer

def main():
    # Affichage naïf du résultat...
    print(solve())

if __name__ == "__main__":
    main()