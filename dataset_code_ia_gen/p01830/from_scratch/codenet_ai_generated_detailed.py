# Solution Python pour le problème "Delete Files"
# L'objectif est de déterminer le nombre minimum d'opérations de suppression nécessaires
# pour supprimer tous les fichiers marqués 'y' (à supprimer), en utilisant les règles données.

# Approche :
# Les fichiers sont affichés verticalement les uns sous les autres.
# La suppression se fait en sélectionnant une région rectangulaire : cela peut donc supprimer un
# intervalle continue de fichiers en une opération, à condition que tous soient à supprimer.
# Cependant, la sélection rectangulaire correspond à la sélection par coordonnées :
# - verticalement, on choisit un intervalle d'indices
# - horizontalement, on choisit une coordonnée de longueur sur la largeur (les fichiers ont des largeurs différentes)
#   Le rectangle sélectionné part de la gauche (x=0) et s'étend jusqu'à une certaine largeur W.
# Un fichier est sélectionné si son largeur est au moins partiellement dans la sélection horizontale,
# c'est-à-dire si sa largeur est > 0 et que la largeur du rectangle couvre au moins une partie du fichier (de 0 à W).
# Au niveau vertical, les fichiers correspondent à des indices de lignes consécutives.

# Pour supprimer un groupe de fichiers contigus, il faut que la largeur du rectangle de sélection horizontale
# couvre tous les fichiers du groupe, donc la largeur minimale à prendre est la largeur minimale parmi les fichiers
# du groupe car si on ne sélectionne pas au moins la largeur minimale parmi eux, on ne sélectionnera pas tous.
# Comme la sélection commence toujours à X=0, la largeur W doit être au moins égale à la largeur maximale 
# de tous les fichiers dans le groupe.

# Ainsi, pour une séquence continue de fichiers 'y', on peut supprimer cette séquence en une seule opération
# si tous les fichiers dans la séquence ont la même largeur minimale possible ? Non, le rectangle doit couvrir
# la plus petite largeur qui couvre tous. La largeur minimale suffisante pour supprimer un groupe est la max des 
# longueurs des fichiers dans ce groupe ? Oui, il faut au moins couvrir la plus large.

# Cependant, la contrainte supplémentaire vient du fait que la sélection horizontale doit sélectionner tous les fichiers
# voulus, mais ne doit pas sélectionner des fichiers non supprimables ('n'). Donc on ne peut pas supprimer un intervalle
# si un fichier 'n' est dans la sélection (car il serait automatiquement supprimé, ce qui est interdit).
# Par conséquent, on doit séparer les groupes d'opérations par les fichiers 'n'.

# Donc, l'algorithme est :
# 1. Séparer la liste de fichiers en segments divisés par les fichiers 'n'.
# 2. Pour chaque segment, les fichiers à supprimer sont les fichiers 'y' dans ce segment.
# 3. Comme on peut sélectionner un rectangle horizontal qui couvre la largeur maximale des fichiers à supprimer
#    et verticalement le segment de fichiers à supprimer, on peut supprimer tous ces fichiers en une seule opération
#    par segment, sauf que dans un segment, on peut avoir des fichiers à ne pas supprimer ('n'), donc on ne peut 
#    pas supprimer un intervalle contenant un fichier 'n'.
# 4. Ainsi, dans chaque segment entre deux fichiers 'n' ou entre un bord et un fichier 'n', on doit compter le nombre
#    de sous-intervalles continus de fichiers 'y', car chaque sous-intervalle continue de 'y' peut être supprimée en
#    une seule sélection.
# 5. Le total est la somme, sur tous les segments délimités par 'n', du nombre de sous-intervalles contigus de 'y'.

# Implémentation : On parcours la liste. Chaque fois qu'on rencontre un 'n', on considère que c'est une frontière.
# On compte ensuite, dans chaque segment, le nombre de plages continues de 'y'.
# La somme de tous ces comptes donnera le nombre minimum d'opérations.

# Exemples donnés confirment cette approche.

def main():
    import sys

    input = sys.stdin.readline

    N = int(input())
    files = []
    for _ in range(N):
        D, L = input().split()
        files.append( (D, int(L)) )

    # Initialisation du compteur d'opérations
    operations = 0

    # On va parcourir les fichiers et diviser en segments limités par les fichiers 'n'
    # Dans chaque segment, on compte les plages continues de 'y'.
    i = 0
    while i < N:
        if files[i][0] == 'n':
            # Fichier non supprimable, on passe au suivant
            i += 1
            continue
        # Sinon fichier à supprimer -> on démarre un segment
        # On parcourt tant qu'on a pas de 'n' ni fin du tableau
        segment_start = i
        while i < N and files[i][0] != 'n':
            i += 1
        segment_end = i  # segment fichiers entre segment_start (inclus) et segment_end (exclu)

        # Compter dans ce segment le nombre de plages continues de 'y'
        segment_ops = 0
        in_delete_run = False
        for j in range(segment_start, segment_end):
            if files[j][0] == 'y':
                if not in_delete_run:
                    # début d'une nouvelle plage de suppression
                    segment_ops += 1
                    in_delete_run = True
            else:
                # fichier 'n' dans segment - impossible selon la segmentation car on a coupé au premier 'n'
                # mais on garde la forme pour solidité
                in_delete_run = False
        operations += segment_ops

    print(operations)

if __name__ == "__main__":
    main()