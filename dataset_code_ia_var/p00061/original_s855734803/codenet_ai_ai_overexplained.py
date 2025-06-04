# Création d'une liste appelée 'List' contenant 101 éléments initialisés à 0.
# L'opérateur * permet de répéter la valeur 0 cent une fois (de l'indice 0 à 100 inclus).
List = [0] * 101

# Démarrage d'une boucle infinie afin de lire en continu les entrées utilisateur.
while True:
    # La fonction input() attend une saisie au clavier.
    # L'utilisateur doit entrer deux nombres séparés par une virgule (par exemple : "5,10").
    # input().split(",") divise la chaîne saisie en deux parties à chaque virgule.
    # map(int, ...) convertit chacune des deux valeurs extraites en entier.
    # Le résultat est affecté à p (premier entier) et s (second entier).
    p, s = map(int, input().split(","))
    
    # Si l'utilisateur entre "0,0", cela signifie que la saisie est terminée.
    # On sort alors de la boucle à l'aide de l'instruction break.
    if p == 0 and s == 0:
        break

    # Mise à jour de la liste 'List'.
    # À l'indice 'p', on place la valeur 's' (cela écrase toute valeur précédente à cet emplacement).
    List[p] = s

# Construction d'une liste appelée 'Sorted_List' :
# 1. set(List) transforme la liste 'List' en un ensemble (type 'set') pour supprimer les doublons.
# 2. list(set(List)) convertit cet ensemble à nouveau en une liste, car set ne permet pas l'indexation.
# 3. sorted(..., reverse = True) trie la liste par ordre décroissant (du plus grand au plus petit).
Sorted_List = sorted(list(set(List)), reverse=True)

# Nouvelle boucle infinie pour accepter des requêtes utilisateurs.
while True:
    try:
        # L'utilisateur doit saisir un entier (la variable 'q').
        # Si l'utilisateur envoie un signal de fin de fichier (EOF), l'appel à input() lèvera une exception EOFError.
        q = int(input())
    except EOFError:
        # Si EOFError est levée, on quitte la boucle grâce à break.
        break

    # On prend la valeur présente dans la liste 'List' à l'indice 'q'.
    # On cherche l'indice de cette valeur (List[q]) dans la liste triée 'Sorted_List' avec la méthode index().
    # Comme Sorted_List est ordonnée par ordre décroissant, l'indice obtenu représente le rang.
    # On ajoute 1 à ce rang car les indices de liste commencent à 0, mais on veut probablement retourner un rang commencé à 1.
    print(Sorted_List.index(List[q]) + 1)