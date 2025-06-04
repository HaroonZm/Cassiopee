# Définition d'une fonction appelée iroha
def iroha():
    # Demande à l'utilisateur de saisir une chaîne de caractères via le clavier.
    # La fonction input() affiche une invite (ici rien n'est affiché) et attend que l'utilisateur entre des données suivies d'une pression sur 'Entrée'.
    # Les données saisies sont récupérées sous forme de chaîne de caractères unique (str).
    # La méthode split() sans argument découpe la chaîne en une liste de sous-chaînes séparées par des espaces.
    # Ici, on suppose que l'utilisateur saisit trois mots séparés par des espaces.
    # Les trois éléments résultants de la découpe sont affectés respectivement aux variables a, b et c.
    a, b, c = input().split()

    # Prend le premier caractère (index 0) de la chaîne de caractères a.
    # Cela se fait grâce à l'opérateur d'indice : a[0].
    # Ensuite, ce caractère (qui peut être minuscule ou majuscule) est converti en majuscule grâce à la méthode upper().
    # Le résultat est assigné à la variable shead.
    shead = a[0].upper()
    # De la même manière, on prend le premier caractère de la chaîne b, puis on le transforme en majuscule et on assigne le résultat à sshead.
    sshead = b[0].upper()
    # Idem pour la chaîne c : on récupère la première lettre, on la met en majuscule, et on stocke le résultat dans ssshead.
    ssshead = c[0].upper()

    # On concatène (colle bout à bout) les trois chaînes de caractères résultantes : shead, sshead, et ssshead.
    # L'opérateur + permet la concaténation de chaînes en Python.
    # On affiche ensuite cette nouvelle chaîne à l'écran grâce à print().
    print(shead + sshead + ssshead)

# Ceci est un point d’entrée standard en Python.
# La variable spéciale __name__ contient '__main__' uniquement si ce fichier est exécuté directement comme script principal, et non importé comme un module dans un autre script.
# Cela permet de ne lancer la fonction iroha que si ce fichier est le programme principal, et pas lors d'importations.
if __name__ == "__main__":
    # Appelle (exécute) la fonction iroha définie ci-dessus.
    iroha()