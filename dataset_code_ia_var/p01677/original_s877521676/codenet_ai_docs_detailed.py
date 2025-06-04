def process_sequence(N, sequence):
    """
    Analyse une séquence d'entiers et de caractères 'x', détermine si un seul entier
    peut remplacer les 'x' pour respecter les contraintes d'ordre, ou détecte l'ambiguïté/impossibilité.

    Paramètres
    ----------
    N : int
        La taille de la séquence.
    sequence : list of str
        Liste de chaînes représentant la séquence, chaque élément étant soit 'x' soit un entier.

    Retourne
    -------
    str or int
        Renvoie 'none' si aucune solution n'est possible, 'ambiguous' si plusieurs sont possibles,
        ou l'unique entier solution si elle existe.
    """
    mn = -10 ** 10  # Borne inférieure possible pour 'x'
    mx = 10 ** 10   # Borne supérieure possible pour 'x'

    for i in range(1, N):
        prev_elem = sequence[i - 1]
        curr_elem = sequence[i]
        
        # Vérifie les cas où deux 'x' se suivent, ce qui est interdit
        if prev_elem == curr_elem == 'x':
            return "none"

        # Cas où l'élément courant ou précédent est 'x', on ajuste les bornes mn/mx selon la position
        elif prev_elem == 'x':
            if (i + 1) % 2 == 0:
                # Pour une position paire (commençant à 1), 'x' doit être strictement inférieur à curr_elem
                mx = min(mx, int(curr_elem) - 1)
            else:
                # Pour une position impaire, 'x' doit être strictement supérieur à curr_elem
                mn = max(mn, int(curr_elem) + 1)
        elif curr_elem == 'x':
            if (i + 1) % 2 == 0:
                # Pour une position paire, 'x' doit être strictement supérieur à prev_elem
                mn = max(mn, int(prev_elem) + 1)
            else:
                # Pour une position impaire, 'x' doit être strictement inférieur à prev_elem
                mx = min(mx, int(prev_elem) - 1)
        else:
            # Cas où les deux sont des entiers, on vérifie le respect des contraintes d'ordre strict
            if (i + 1) % 2 == 0 and int(curr_elem) <= int(prev_elem):
                return "none"
            elif (i + 1) % 2 == 1 and int(curr_elem) >= int(prev_elem):
                return "none"
    else:
        # S'il n'y a pas de 'x', il n'y a pas d'information à déduire, donc ambiguïté
        if 'x' not in sequence:
            return "ambiguous"
        else:
            # Si une seule valeur satisfait les contraintes, c'est la solution
            if mn == mx:
                return mx
            # S'il y a plusieurs valeurs possibles, c'est ambigu
            elif mn < mx:
                return "ambiguous"
            # Si mn > mx, aucune valeur possible ne satisfait les contraintes
            else:
                return "none"


def main():
    """
    Fonction principale qui lit les entrées standard, traite chaque séquence,
    et affiche le résultat correspondant à la sortie standard.
    S'arrête si l'utilisateur saisit 0 comme valeur de N.
    """
    while True:
        N = int(raw_input())  # Lecture de la taille de séquence
        if N == 0:
            break  # Fin du programme si N vaut 0
        a = raw_input().split()  # Lecture de la séquence sous forme de liste de chaînes
        
        result = process_sequence(N, a)  # Traitement de la séquence
        print(result)

# Exécution du programme principal        
if __name__ == '__main__':
    main()