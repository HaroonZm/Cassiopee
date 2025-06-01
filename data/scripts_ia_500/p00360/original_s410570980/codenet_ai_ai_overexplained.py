import sys

# Définition de la fonction principale qui encapsule toute la logique du programme
def main():
    # NI est une fonction lambda (fonction anonyme) qui lit une ligne depuis l'entrée standard,
    # puis convertit cette chaîne de caractères en un entier. 
    # Cela permet de récupérer un entier depuis l'entrée utilisateur.
    NI = lambda : int(sys.stdin.readline())
    # SI est une fonction lambda qui lit une ligne depuis l'entrée standard,
    # puis supprime les espaces blancs (comme le retour à la ligne) à la fin de la chaîne.
    # Elle retourne ainsi une chaîne propre sans caractères de fin qui pourraient perturber.
    SI = lambda : sys.stdin.readline().rstrip()

    # Lecture de la chaîne de caractères s depuis l'entrée utilisateur
    s = SI()
    # n est la longueur de la chaîne s, ie le nombre de caractères qu'elle contient.
    n = len(s)
    # Lecture d'un entier k depuis l'entrée utilisateur
    k = NI()

    # Fonction conv qui prend un caractère x (une lettre) et retourne sa position dans l'alphabet (0 pour 'a', 1 pour 'b', etc.)
    # ord() donne le code ASCII du caractère. En soustrayant le code ASCII de 'a', on normalise les lettres sur 0..25.
    def conv(x):
        return ord(x) - ord('a')

    # Création d'un tableau 'bit' (Fenwick Tree ou arbre binaire indexé) de taille n+1, initialisé à zéro.
    # Cet arbre va servir à faire des mises à jour et requêtes efficientes en temps logarithmique.
    bit = [0] * (n+1)

    # Fonction bit_add qui met à jour le BIT en ajoutant 1 à la position i.
    # La boucle while permet de propager cet ajout dans toutes les positions du BIT qui couvrent l'index i.
    # L'expression i & (-i) calcule la plus petite puissance de deux qui divise i (le "bit le plus bas à 1").
    # Cela permet de naviguer dans les "nœuds" du BIT de façon efficace.
    def bit_add(i):
        # temps O(log n)
        while i <= n:
            bit[i] += 1
            i += i & (-i)

    # Fonction bit_sum qui calcule la somme des éléments dans le BIT de l'indice 1 à l'indice i inclus.
    # Cela permet d'obtenir une somme partielle efficace malgré les modifications.
    def bit_sum(i):
        ret = 0
        # On remonte dans le BIT en soustrayant la plus petite puissance de deux qui divise i
        while i > 0:
            ret += bit[i]
            i -= i & (-i)
        # ret contient la somme partielle demandée
        return ret

    # Initialisation de plusieurs listes : z, top, nxt, bef
    # z est un tableau de 0/1 de taille n, marquant si un caractère de s est choisi (1) ou non (0)
    z = [0] * n
    # top est un tableau de taille 26 initialisé à -1, il contiendra pour chaque lettre la position dans s de la prochaine occurrence non utilisée
    top = [-1] * 26
    # nxt aidera à relier la position d'une lettre à la suivante dans la chaîne s
    nxt = [-1] * n
    # bef contient pour chaque lettre la position la plus récente vue dans s pour cette lettre
    bef = [-1] * 26

    # Remplissage des tableaux nxt, top et bef en parcourant la chaîne s de gauche à droite
    for i in range(n):
        # cv est la position alphabétique de s[i] (ex: 'a'->0, 'b'->1, ...)
        cv = conv(s[i])
        # Si on a déjà vu cette lettre auparavant, on relie la dernière occurrence (bef[cv]) à la position actuelle i
        if bef[cv] >= 0:
            nxt[bef[cv]] = i
        # On met à jour la dernière occurrence vue de cette lettre à la position i
        bef[cv] = i
        # Si c'est la première occurrence de cette lettre, on initialise top[cv] avec i (position de la première apparition)
        # top sert à pointer vers la prochaine occurrence disponible pour chaque lettre
        if top[cv] < 0:
            top[cv] = i

    # ans sera la liste finale des caractères choisis (construction finale de la sortie)
    ans = []
    # Tant que k > 0 (ressource disponible pour supprimer ou réarranger)
    while k > 0:
        # On essaie dans l'ordre alphabétique de 0 à 25 (a à z)
        for i in range(26):
            # Si top[i] est négatif, cela signifie qu'il n'y a plus de caractères disponibles pour cette lettre
            if top[i] < 0:
                continue
            # p est l'indice dans s de la prochaine occurrence non utilisée de la lettre i
            p = top[i]
            # cost calcule combien de lettres doivent être "déplacées" pour prendre cette lettre, ajusté par les suppressions via bit_sum
            # bit_sum(p+1) donne le nombre de caractères déjà choisis parmi les indices ≤ p
            cost = p - bit_sum(p+1)
            # Si ce coût ne dépasse pas k, on peut choisir cette lettre
            if cost <= k:
                # On ajoute cette lettre (convertie à la lettre correspondante) à la réponse
                ans.append(chr(ord('a')+i))
                # Marque la position p comme utilisée
                z[top[i]] = 1
                # On consomme le budget k du coût nécessaire pour 'attraper' cette lettre
                k -= cost
                # On avance top[i] vers la prochaine occurrence disponible de cette lettre
                top[i] = nxt[top[i]]
                # Mise à jour du BIT pour signaler que la position p+1 est maintenant prise
                bit_add(p+1)
                # Sortir de la boucle des lettres pour recommencer depuis 'a'
                break
        else:
            # Si aucune lettre n'a pu être choisie (toutes coûtent trop cher ou épuisées), sortie de la boucle while
            break

    # Ajout des lettres restantes non utilisées dans l'ordre initial
    for i in range(n):
        if z[i] == 0:
            ans.append(s[i])

    # Affichage de la chaîne finale construite sans espaces (séparateur vide)
    print(*ans,sep='')

# Vérification que ce script est bien exécuté en tant que programme principal (et non importé)
if __name__ == '__main__':
    main()