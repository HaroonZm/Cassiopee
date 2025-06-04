def main():
    """
    Programme principal qui lit une séquence de paires d'entiers (x, s) et calcule la valeur maximale atteinte
    par cumulation sur un intervalle variable dépendant du déplacement (différence entre les x consécutifs).
    La logique peut s'appliquer à des problèmes de disjoint set, somme maximale avec décrément, ou simulation de stock/recharge.
    """
    n = int(input())  # Lit le nombre de paires (x, s) à traiter
    ans = 0           # Variable qui stocke la valeur maximale atteinte jusqu'à présent
    tmp = 0           # Valeur temporaire courante servant d'accumulateur/mémoire
    prev = 0          # Dernière position x traitée afin de calculer l'écart dx

    # Itère sur les n entrées fournies, chaque entrée étant composée de deux entiers séparés par un espace
    for x, s in (map(int, input().split()) for _ in range(n)):
        dx = x - prev          # Calcule la différence de position avec la précédente (écart sur x)
        if dx > tmp:
            # Si l'écart est supérieur à la réserve temporaire, on repart de s (comme une "recharge")
            tmp = s
        else:
            # Sinon, on ajoute la contribution s en compensant la perte dx
            tmp += s - dx
        ans = max(ans, tmp)    # Met à jour la valeur maximale atteinte
        prev = x               # Mémorise la position x courante pour le prochain calcul d'écart

    ans = max(ans, tmp)        # S'assure que la dernière valeur temporaire soit prise en compte
    print(ans)                 # Affiche le résultat final

if __name__ == "__main__":
    main()