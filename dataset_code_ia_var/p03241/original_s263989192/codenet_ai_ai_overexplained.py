# Cette fonction correspond à la résolution du problème D de l'ABC112 sur AtCoder.
# Le but est, étant donnés deux entiers N et M, de trouver le plus grand entier d 
# tel que d soit un diviseur de M et que M // d >= N.

def abc112_d():
    # On commence par lire l'entrée standard.
    # La fonction input() lit une ligne entière tapée par l'utilisateur au clavier,
    # qui est ensuite découpée en une liste de chaînes de caractères par split(),
    # puis chaque élément de cette liste est converti en entier par map(int, ...)
    # Le résultat final est stocké par décomposition dans N et M.
    N, M = map(int, input().split())

    # On procède à la définition d'une fonction imbriquée appelée divisor qui prend en argument un entier n.
    # Cette fonction renverra la liste de tous les diviseurs positifs de n.
    def divisor(n):
        # Début de la fonction divisor
        # Initialisation d'une liste vide qui va contenir les diviseurs trouvés.
        arr = []
        # On va parcourir tous les entiers i de 1 jusqu'à racine carrée de n (borne supérieure incluse)
        # Le but est d'optimiser le nombre d'itérations. Pour chaque i, si i divise n,
        # alors (n // i) est aussi un diviseur de n.
        for i in range(1, int(n**0.5) + 1):
            # On vérifie si i est un diviseur de n, c'est-à-dire si le reste de la division de n par i est nul.
            if n % i == 0:
                # Si oui, on ajoute i à la liste des diviseurs.
                arr.append(i)
                # On ajoute aussi le "diviseur miroir", à savoir n // i
                arr.append(n // i)
        # On retourne la liste arr contenant potentiellement des doublons si n est un carré parfait
        # et pas forcément triée.
        return arr

    # On commence par définir la variable de résultat ans, initialisée à 1.
    ans = 1
    # Pour chaque diviseur d de M (la fonction divisor renvoie tous les diviseurs de M)
    for d in divisor(M):
        # On s'assure que si on divise M par d, le résultat (qui est forcément un entier, car d divise M),
        # est supérieur ou égal à N.
        if M // d >= N:
            # On met à jour la valeur de ans pour retenir le maximum entre la valeur actuelle de ans et d.
            ans = max(d, ans)
    # Après avoir passé tous les diviseurs en revue, on affiche la valeur finale de ans.
    print(ans)

# Appel de la fonction principale pour lancer le programme.
abc112_d()