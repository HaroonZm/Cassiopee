# AOJ 0254: Scone
# Python3 2018.6.25 bal4u

def main():
    """
    Résout le problème AOJ 0254 "Scone". 
    Pour chaque cas de test, on lit deux entiers n et m, suivis d'une liste de n entiers.
    Le programme calcule la plus grande somme mod m possible à partir d'une sous-séquence contiguë des éléments,
    puis affiche ce résultat. Le traitement s'arrête lorsque n est égal à 0.
    """
    # Tableau pré-alloué utilisé pour le calcul des préfixes modulaires
    s = [0 for _ in range(30001)]

    while True:
        # Lecture de n (taille de la séquence) et m (modulo)
        n, m = map(int, input().split())
        # Condition d'arrêt du programme
        if n == 0:
            break

        # f stockera pour chaque valeur mod m, l'indice de dernière apparition dans s
        # Initialisé à -1 signifiant "non trouvée"
        f = [-1 for _ in range(m)]

        # Initialisations :
        # sum : somme totale des éléments
        # nmax : valeur maximale modulo m rencontrée dans a
        # ans : la réponse finale (somme modulo maximale)
        sum_val = 0
        nmax = 0
        ans = 0

        # Lecture de la séquence a
        a = list(map(int, input().split()))

        for i in range(n):
            sum_val += a[i]          # cumul de la somme totale brute
            a[i] %= m               # on remplace a[i] par sa valeur modulo m
            if a[i] > nmax:
                nmax = a[i]         # mise à jour du nmax
            if a[i] == m - 1:
                ans = a[i]          # si un élément égale m-1, c'est la valeur maximale possible
            # Calcul du préfixe modulaire : s[i+1] est la somme modulo m des a[0..i]
            s[i + 1] = s[i] + a[i]
            if s[i + 1] >= m:
                s[i + 1] -= m       # ajustement modulo m
            # Enregistre l'indice i+1 comme dernière apparition du préfixe modulo s[i+1]
            f[s[i + 1]] = i + 1

        if ans == 0:
            # Si aucune sous-somme mod m ne vaut m-1
            if nmax == 0:
                # Si tous les éléments sont nuls modulo m, la réponse est 0
                ans = 0
            elif sum_val < m:
                # Si la somme brute est inférieure à m, la réponse est la somme brute
                ans = sum_val
            else:
                # Dans le cas général, on recherche la plus grande valeur possible
                # entre nmax et m-1 vérifiant une condition sur les préfixes s
                done = False
                # On essaie toutes les valeurs d'ans possibles à partir de m-1 descendant vers nmax
                for ans_candidate in range(m - 1, nmax - 1, -1):
                    for i in range(n + 1):
                        # On calcule la valeur x = s[i] + ans_candidate modulo m
                        x = s[i] + ans_candidate
                        if x >= m:
                            x -= m
                        # Si la valeur x apparaît plus loin ou à la même position dans f,
                        # cela signifie qu'une sous-séquence existe avec cette somme modulo ans_candidate
                        if f[x] >= i:
                            ans = ans_candidate
                            done = True
                            break
                    if done:
                        break

        # Affichage de la réponse pour le cas de test courant
        print(ans)

if __name__ == "__main__":
    main()