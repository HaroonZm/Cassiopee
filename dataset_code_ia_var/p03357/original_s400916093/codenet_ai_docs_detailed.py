from itertools import accumulate

def solve(n, rev):
    """
    Calcule le coût minimum pour réordonner les billes blanches et noires dans une ligne
    selon une règle spécifique basée sur leurs positions initiales.

    Args:
        n (int): Nombre de billes blanches (et également de billes noires, donc 2n billes au total).
        rev (list): Liste composée de deux sous-listes :
            - rev[0] : positions actuelles des billes blanches dans la ligne (ordre donné par les indices).
            - rev[1] : positions actuelles des billes noires dans la ligne.

    Returns:
        int: Le coût minimum selon l'algorithme employé.
    """
    def existence_right(rev_c):
        """
        Pour chaque bille de la couleur concernée, construit une table qui indique
        combien de billes de cette couleur se trouvent plus à droite de chaque position.

        Args:
            rev_c (list): Liste des positions pour une couleur donnée.

        Returns:
            list: Liste d'états accumulés représentant, pour chaque progression,
                le nombre cumulatif de billes à droite de chaque indice.
        """
        n2 = n * 2  # Longueur totale de la ligne (2n positions).
        acc = [[0] * n2]  # Initialise l'accumulateur pour chaque étape.
        row = [0] * n2    # Représente la présence des billes sur chaque case.
        for x in rev_c:
            # On place une bille à la position correspondante (côté "droit", d'où le n2-x-1)
            row[n2 - x - 1] += 1
            # On accumule le total depuis la droite vers la gauche (côté le plus à droite == début de l'accumulateur)
            acc.append(list(reversed(list(accumulate(row)))))
        return acc

    # Chaque élément de cost correspond à une couleur (cost[0] pour blanc, cost[1] pour noir).
    # Chacun est une table donnant combien de billes de cette couleur sont à droite de chaque index,
    # pour chaque nombre de billes déjà prises.
    cost = list(map(existence_right, rev))

    # Initialisation du premier vecteur dp : coût minimum pour sélectionner les billes noires dans un certain ordre.
    # dp[b] sera le coût minimum pour avoir traité les b premières billes noires.
    dp = [0] + list(accumulate(c[y] for y, c in zip(rev[1], cost[1])))

    # On traite ensuite les billes blanches une à une.
    for x, cw0, cw1 in zip(rev[0], cost[0], cost[0][1:]):
        # ndp sera le nouveau tableau des coûts minimums, pour chaque nombre de billes noires déjà sélectionnées.
        ndp = [0] * (n + 1)
        # Coût pour placer une bille blanche à la position x, sachant la config précédente.
        cw0x = cw0[x]
        # Cas où aucune bille noire n'est encore traitée.
        ndp[0] = prev = dp[0] + cw0x
        # Parcours du nombre de billes noires déjà sélectionnées (de 1 à n).
        for b, (y, cb0, cb1) in enumerate(zip(rev[1], cost[1], cost[1][1:])):
            # Choix du coût en ajoutant la prochaine bille noire ou la prochaine bille blanche.
            # Comparaison entre deux scénarios et prise du minimum.
            ndp[b + 1] = prev = min(
                dp[b + 1] + cw0x + cb1[x],  # Cas où l'on ajoute une bille blanche puis une noire
                prev + cw1[y] + cb0[y]      # Cas où l'on ajoute une bille noire puis une blanche
            )
        # On prépare pour la prochaine itération.
        dp = ndp
    # À la fin, le résultat optimal est dp[n], i.e., toutes les billes traitées (blanches et noires)
    return dp[n]

if __name__ == "__main__":
    # Lecture du nombre de billes de chaque couleur
    n = int(input())
    # Initialisation des tableaux pour les positions de chaque bille blanche et noire.
    # rev[0] contiendra les positions des billes blanches
    # rev[1] celles des noires
    rev = [[0] * n, [0] * n]
    for i in range(n * 2):
        c, a = input().split()  # c = couleur ("W" ou "B"), a = numéro de la bille (1-based)
        a = int(a) - 1          # Conversion en indice basé zéro
        rev[int(c == 'B')][a] = i  # Mise à jour de la position pour la couleur et le numéro donnés
    print(solve(n, rev))  # Calcul et affichage du coût minimum