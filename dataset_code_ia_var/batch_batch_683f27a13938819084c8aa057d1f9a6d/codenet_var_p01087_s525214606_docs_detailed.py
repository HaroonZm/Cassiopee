import sys
input = sys.stdin.readline

def calc(i, level, fs, lim):
    """
    Évalue récursivement une arborescence d'expressions arithmétiques préfixes structurée par indentations.
    
    Args:
        i (int): L'indice courant dans la liste fs représentant la position de l'expression à traiter.
        level (int): Le niveau courant d'indentation dans l'arbre d'expressions.
        fs (list): Une liste de sous-listes, chaque sous-liste contenant [niveau_d'indentation, operateur_ou_valeur].
        lim (int): Limite supérieure (exclusive) de l'index à traiter dans fs (en général sa longueur).
        
    Returns:
        tuple: (dernier_indice_traverse, valeur_entière_calculée)
    """
    # Cas de base : si le token courant n'est pas un opérateur (‘+’ ou ‘*’), c'est une valeur entière terminale
    if fs[i][1] not in "+*":
        return i, int(fs[i][1])
    
    # Cas récursif : opérateur d'addition
    if fs[i][1] == "+":
        tmp = 0  # Accumulateur pour la somme
        j = i + 1  # Débute à l'élément suivant
        # Parcours des enfants directs (d'un niveau d'indentation supérieur)
        while j < lim:
            # Retourne si on rencontre un niveau d'indentation égal ou inférieur au noeud courant
            if fs[j][0] <= level:
                break
            # Si c'est un nouvel opérateur, appeler récursivement
            if fs[j][1] in "*+":
                j, tmp2 = calc(j, level + 1, fs, lim)
                tmp += tmp2
            else:
                # Sinon, additionner la feuille entière
                tmp += int(fs[j][1])
            j += 1
        return j - 1, tmp
    
    # Cas récursif : opérateur de multiplication
    elif fs[i][1] == "*":
        tmp = 1  # Accumulateur pour le produit
        j = i + 1  # Débute à l'élément suivant
        # Parcours des enfants directs (d'un niveau d'indentation supérieur)
        while j < lim:
            # Retourne si on rencontre un niveau d'indentation égal ou inférieur au noeud courant
            if fs[j][0] <= level:
                break
            # Si c'est un nouvel opérateur, appel récursif
            if fs[j][1] in "*+":
                j, tmp2 = calc(j, level + 1, fs, lim)
                tmp *= tmp2
            else:
                # Sinon, multiplier la feuille entière
                tmp *= int(fs[j][1])
            j += 1
        return j - 1, tmp

def main():
    """
    Lit des expressions arithmétiques préfixes structurées par indentation depuis l'entrée standard.
    Parse chaque expression en une structure de liste, puis l'’évalue récursivement et affiche le résultat.
    La boucle principale continue jusqu'à la lecture d’une ligne commençant par 0.
    """
    while True:
        n = int(input())
        if n == 0:
            break  # Arrête le programme si 0 est lu

        # Initialisation de la structure contenant l'expression formattée
        fs = [[0, 0] for _ in range(n)]

        # Lecture et prétraitement de chaque ligne de l'expression
        for i in range(n):
            tmp = input().strip()
            # Compte le nombre de points pour déterminer le niveau d'indentation
            fs[i][0] = tmp.count(".")
            # Extrait l'opérateur ou la valeur entière (en retirant les points)
            fs[i][1] = tmp.replace(".", "")

        # Calcule la valeur de l'expression à partir de la racine (indice 0, niveau 0)
        _, ans = calc(0, 0, fs, len(fs))
        print(ans)

if __name__ == "__main__":
    main()