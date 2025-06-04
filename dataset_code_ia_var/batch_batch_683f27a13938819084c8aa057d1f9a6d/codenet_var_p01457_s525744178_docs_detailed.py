def check_parentheses_balance():
    """
    Lit un entier N depuis l'entrée standard, puis lit N lignes suivantes contenant chacune
    trois valeurs : un identifiant (non utilisé), un caractère de parenthèse '(' ou ')', 
    et un nombre indiquant combien de fois ce caractère apparaît.
    À chaque ligne, la fonction compare les totaux cumulés des parenthèses ouvrantes 
    et fermantes, et affiche 'Yes' si les deux totaux sont égaux, 'No' sinon.
    """
    # Lire le nombre de lignes à traiter
    N = int(input())

    # Initialiser les compteurs pour les parenthèses ouvrantes et fermantes
    lp = 0  # compteur de '('
    rp = 0  # compteur de ')'

    # Parcourir toutes les lignes d'entrée
    for i in range(N):
        # Lire la ligne et séparer en trois parties : identifiant (non utilisé), caractère, quantité
        p, c, n = input().split()
        count = int(n)  # convertir la quantité en entier

        # Vérifier quel caractère a été lu et incrémenter le compteur correspondant
        if c == '(':
            lp += count
        else:
            rp += count

        # Afficher 'Yes' si les compteurs sont égaux, sinon 'No'
        if lp == rp:
            print('Yes')
        else:
            print('No')

# Appeler la fonction principale pour exécuter le programme
check_parentheses_balance()