#!/usr/bin/python

def is_abc_string(S):
    """
    Vérifie si la chaîne S peut être réduite exactement à 'ABC' en supprimant toutes les occurrences du motif 'ABC'
    de manière itérative.

    Paramètres:
        S (str): La chaîne à vérifier.

    Retourne:
        bool: True si S == 'ABC' après les suppressions, False sinon.
    """
    c = ['A', 'B', 'C']  # Liste des caractères attendus pour la reconstruction

    while True:
        # Si la taille de la chaîne est inférieure ou égale à 3, vérifie si elle correspond à 'ABC'
        if len(S) <= 3:
            return S == "ABC"

        # Découpe la chaîne courante sur chaque occurrence du motif 'ABC'
        T = S.strip().split("ABC")
        # Recombine les segments restants après la suppression du motif 'ABC'
        P = ''.join(T)

        cnt = 0  # Compte le nombre de caractères parmi 'A','B','C' présents dans P

        for x in c:
            if x in P:
                cnt += 1
            else:
                # Si un caractère est manquant, le réinsère entre les segments de T pour S
                S = x.join(T)
        
        # Si la découpe n'a pas retiré d'occurrences ou s'il manque plus d'un caractère
        if len(T) == 1 or cnt != 2:
            return False

if __name__ == "__main__":
    # Demande à l'utilisateur de saisir une chaîne
    # Pour Python 2, on utilise raw_input; en Python 3, remplacer par input
    S = raw_input()
    
    # Vérifie si la chaîne S peut être réduite à 'ABC' selon la logique de is_abc_string
    if is_abc_string(S):
        print "Yes"
    else:
        print "No"