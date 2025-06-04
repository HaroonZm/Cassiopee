def dfs(l):
    """
    Effectue une traversée récursive d'une structure en forme d'arbre représentée
    par une liste de chaînes, chacune symbolisant un noeud à un certain niveau.
    Les noeuds sont soit un opérateur ('+' ou '*'), soit une valeur numérique.
    
    Args:
        l (list of str): La sous-liste représentant l'arbre ou le sous-arbre à évaluer.
    
    Returns:
        int: Résultat de l'évaluation de la sous-arborescence donnée.
    """
    x = len(l[0])  # Longueur de l'indentation du noeud racine courant (détermine le niveau)
    
    if l[0][-1] == "+":  # Si le noeud courant est une addition
        b = 0  # Flag de résultant d'addition
        i = 1  # Index de parcours des enfants
        while i < len(l):
            # Si l'élément est un chiffre, descendant d'un niveau (un enfant direct)
            if len(l[i]) == x + 1 and "0" <= l[i][-1] <= "9":
                b += int(l[i][-1])  # Ajoute la valeur au résultat
                i += 1
            # Si l'élément est un opérateur imbriqué ('+' ou '*')
            elif len(l[i]) == x + 1 and (l[i][-1] == "+" or l[i][-1] == "*"):
                f = i  # Garde la position de début du sous-arbre
                i += 1
                # Trouve la fin du sous-arbre imbriqué
                while i < len(l):
                    if len(l[i]) == x + 1:
                        break
                    i += 1
                # Appel récursif pour évaluer le sous-arbre
                b += dfs(l[f:i])
    elif l[0][-1] == "*":  # Si le noeud courant est une multiplication
        b = 1  # Flag résultant de multiplication
        i = 1
        while i < len(l):
            if len(l[i]) == x + 1 and "0" <= l[i][-1] <= "9":
                b *= int(l[i][-1])  # Multiplie la valeur
                i += 1
            elif len(l[i]) == x + 1 and (l[i][-1] == "+" or l[i][-1] == "*"):
                f = i
                i += 1
                # Trouve la fin du sous-arbre imbriqué
                while i < len(l):
                    if len(l[i]) == x + 1:
                        break
                    i += 1
                b *= dfs(l[f:i])  # Multiplie le résultat récursif du sous-arbre
    else:
        # Cas terminal : feuille contenant un nombre
        b = int(l[0][-1])
    return b

def main(n):
    """
    Gère l'entrée pour une expression arborescente.
    Lit n lignes depuis l'entrée standard, puis affiche le résultat de l'évaluation.
    
    Args:
        n (int): Le nombre de lignes à lire (nombre de noeuds/arêtes dans l'arbre).
    """
    l = [input() for i in range(n)]  # Lecture des lignes représentant l'arbre
    print(dfs(l))  # Affiche le résultat de l'évaluation

while True:
    # Boucle principale d'interaction utilisateur.
    n = int(input())  # Lecture du nombre de lignes pour une expression
    if n == 0:
        break  # Arrête le programme si l'utilisateur entre 0
    main(n)  # Lance le traitement de l'expression