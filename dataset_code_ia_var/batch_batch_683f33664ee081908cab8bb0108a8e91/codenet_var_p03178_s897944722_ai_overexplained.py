MOD = 10**9 + 7  # On définit une constante MOD qui sera utilisée pour appliquer le modulo aux résultats et éviter les débordements d'entiers

def main():
    # Lecture de l'entrée sous forme de liste de caractères, chaque caractère représentant un chiffre du nombre
    S = [s for s in input()]  # Par exemple, pour "123", S sera ['1', '2', '3']
    N = len(S)  # Calcul du nombre de chiffres du nombre donné en entrée
    D = int(input())  # Lecture de l'entier D, le reste sur lequel on veut travailler

    # Initialisation d'un tableau 3D pour la programmation dynamique (DP)
    # dp[i][smaller][dsum] signifie :
    # i : on a considéré les i premiers chiffres du nombre
    # smaller : booléen converti en entier (0 = False, 1 = True), indique si on a déjà rencontré un chiffre inférieur à celui du nombre original -> permet d'autoriser tous les choix ensuite
    # dsum : la somme des chiffres du nombre mod D en cours de construction
    # Tous les éléments du tableau sont initialisés à 0
    dp = [[[0]*D for _ in range(2)] for _ in range(N+1)]
    # On initialise la condition de base : il y a exactement 1 manière de commencer (nombre vide, aucune liberté prise, somme 0)
    dp[0][0][0] = 1

    from itertools import product  # On importe product pour former les boucles imbriquées de façon compacte
    # On parcourt chaque position du nombre, chaque état "smaller" possible, et chaque somme de chiffres mod D possible
    for i, smaller, dsum in product(range(N), [True, False], range(D)):
        # Pour le chiffre actuel à l'indice i :
        # Si le drapeau 'smaller' est True, alors on peut placer n'importe quel chiffre de 0 à 9 (lim = 9)
        # Si le drapeau est False, pour rester "limité", on ne peut aller que jusqu'au chiffre de S[i]
        lim = 9 if smaller else int(S[i])
        # On considère tous les chiffres possibles qu'on peut mettre à cette position (selon la limite lim déterminée)
        for d in range(lim+1):
            # Calcul du nouvel état "smaller or d < lim" :
            #  - Si on était déjà plus petit, on continue de l'être
            #  - Ou bien, si d est plus petit que lim (donc qu'on a pris une valeur plus petite que S[i]), on passe à smaller=True
            # Calcul du nouveau dsum : ajoute d à l'ancienne somme, puis on prend le modulo D
            new_smaller = smaller or d < lim
            new_dsum = (dsum + d) % D
            # On met à jour le nombre de façons d'arriver à cet état dans dp
            dp[i+1][new_smaller][new_dsum] += dp[i][smaller][dsum]
            # Pour empêcher le débordement, on applique le modulo MOD à chaque ajout
            dp[i+1][new_smaller][new_dsum] %= MOD

    # On a terminé de remplir la table DP.
    # Pour calculer la réponse finale :
    # Les nombres valides sont ceux de longueur N, ayant sum % D == 0, et pouvant être soit 'exactement égal à S' (smaller=0), soit 'strictement plus petit' (smaller=1)
    # On additionne ces deux possibilités.
    # On retire 1 pour exclure le nombre 0 (la solution DP le compte), puisqu'il n'est pas un nombre valide "inférieur ou égal à S" à moins que S ne soit "0" lui-même
    result = (dp[N][0][0] + dp[N][1][0] - 1) % MOD  # calcul du résultat final avec le modulo pour rester dans les bornes

    # On affiche la réponse finale
    print(result)

# Point d'entrée standard du script Python
if __name__ == '__main__':
    main()