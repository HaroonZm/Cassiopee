INF = 10 ** 10  # Définition d'une grande constante, potentiellement utilisable comme "infinie"
MOD = 10 ** 9 + 7  # Constante pour le module, une valeur populaire utilisée pour éviter les grands nombres en informatique, elle est un grand nombre premier

def solve(A, B, C):
    # Inversion des chaînes de caractères pour faciliter la gestion des retenues lors de l’addition
    # Par exemple, si A = '123', alors A[::-1] devient '321'
    A = A[::-1]
    B = B[::-1]
    C = C[::-1]

    # Liste représentant l'état initial de la dynamique
    # before[x] = nombre de moyens d’atteindre la position courante avec x comme "retenue"
    before = [1, 0, 0]  # On commence avec une seule façon (aucune retenue)

    N = len(A)  # Longueur des chaînes (on suppose qu’elles sont de même longueur)

    for i in range(N):  # Parcours de chaque position (chiffre) à partir du chiffre le moins significatif
        dp = [0] * 3  # dp[x] est le nombre de façons d'arriver ici avec une retenue de x
        s = 0  # "s" est le chiffre de départ pour cette colonne
        if i == N - 1:
            # Pour le chiffre le plus significatif (dernière position après inversion),
            # on ne doit pas commencer par 0, donc on met s=1
            s += 1

        # Parcours de toutes les valeurs possibles de la retenue entrante
        for j in range(3):  # Il n'y a que trois états possibles de retenue : 0, 1, 2
            # Parcours de toutes les valeurs possibles pour A[i]
            for a in range(s, 10):
                # Si A[i] n’est pas un joker (pas '?'), on ne garde que la valeur correcte
                if A[i] != '?' and int(A[i]) != a:
                    continue
                # Parcours de toutes les valeurs possibles pour B[i]
                for b in range(s, 10):
                    # Même logique pour B[i]
                    if B[i] != '?' and int(B[i]) != b:
                        continue
                    # Parcours de toutes les valeurs possibles pour C[i]
                    for c in range(s, 10):
                        # Même logique pour C[i]
                        if C[i] != '?' and int(C[i]) != c:
                            continue
                        # Vérifie que la somme des chiffres A[i], B[i] et de la retenue j
                        # (modulo 10) correspond au chiffre C[i] (c)
                        # Cela garantit que les chiffres concordent à cette position
                        if (j + a + b) % 10 != c:
                            continue
                        # Retenue sortante : (j + a + b)//10, soit 0, 1 ou 2
                        # Ajoute toutes les manières existantes d'y arriver (from before[j])
                        dp[(j + a + b) // 10] += before[j]
                        # Réduction modulo MOD pour éviter le débordement
                        dp[(j + a + b) // 10] %= MOD
        # Mise à jour "before" pour l’itération suivante (prochaine colonne)
        before = dp

    # À la fin, on est à la position la plus significative sans retenue
    ans = before[0]
    # Affiche le résultat
    print(ans)

def main():
    while True:  # Boucle infinie, s'arrête quand la condition d'arrêt est atteinte
        A = input()  # Lecture première chaîne d’entrées (A)
        if A == '0':  # Condition d'arrêt : si A est exactement '0', exit
            return
        B = input()  # Lecture deuxième chaîne d’entrées (B)
        C = input()  # Lecture troisième chaîne d’entrées (C)
        # Appel de la fonction principale pour résoudre le cas actuel avec A, B, C
        solve(A, B, C)

# Point d'entrée du script
if __name__ == '__main__':  # Vérifie que ce script est exécuté (pas importé)
    main()  # Appelle la fonction principale pour démarrer le programme