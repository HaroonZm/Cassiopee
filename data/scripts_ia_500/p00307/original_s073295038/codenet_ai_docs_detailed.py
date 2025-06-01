from bisect import bisect_right as br
from itertools import accumulate

def main():
    """
    Point d'entrée principal du programme.
    - Lit les entrées standard pour obtenir le nombre de livres et d'étagères.
    - Calcule les préfixes cumulés des poids et des épaisseurs des livres.
    - Lit les contraintes de chaque étagère.
    - Effectue une recherche dynamique pour déterminer la position maximale possible de placement des livres
      selon les contraintes des étagères.
    - Affiche le résultat final.
    """
    # Lire le nombre de livres (m) et le nombre d'étagères (n)
    m, n = map(int, input().split())

    # Lire les caractéristiques des livres : chaque livre a un poids et une épaisseur
    # books est une liste de listes, où chaque sous-liste contient [poids, épaisseur]
    books = [list(map(int, input().split())) for _ in range(m)]

    # Calculer les préfixes cumulés du poids (ws) et de l'épaisseur (ts)
    # Ces accumulations commencent à 0 pour faciliter les calculs d'intervalles
    ws = list(accumulate([0] + [book[0] for book in books]))
    ts = list(accumulate([0] + [book[1] for book in books]))

    # Lire les contraintes de chaque étagère sous forme de paires [limite poids, limite épaisseur]
    shelf = [list(map(int, input().split())) for _ in range(n)]

    # Dictionnaire pour mémoriser les résultats intermédiaires dans la programmation dynamique
    dic = {}

    # Bitmask complet correspondant à toutes les étagères sélectionnées.
    # 2^n - 1 car chaque étagère est représentée par un bit.
    rest = 2 ** n - 1

    def search(index, num):
        """
        Fonction de recherche binaire pour déterminer la position maximale possible
        à partir de l'indice `index` avec la contrainte de l'étagère `num`.

        Args:
            index (int): indice de départ dans la liste des livres.
            num (int): indice de l'étagère dont on applique les contraintes.

        Returns:
            int: l'indice maximal des livres que l'on peut placer sans dépasser les contraintes
                 en poids et épaisseur de l'étagère `num`.
        """
        # Extraire les limites de poids et d'épaisseur pour l'étagère num
        wlim, tlim = shelf[num]

        # Trouver la limite supérieure par poids via recherche binaire dans les préfixes cumulés
        wind = br(ws, ws[index] + wlim)

        # Trouver la limite supérieure par épaisseur via recherche binaire dans les préfixes cumulés
        tind = br(ts, ts[index] + tlim)

        # Retourner l'indice maximum possible, on retire 1 pour obtenir un indice valide
        # car bisect_right retourne la position d'insertion
        return min(wind, tind) - 1

    def dp(rest, dic):
        """
        Fonction récursive de programmation dynamique utilisant la technique de mémoïsation.

        Args:
            rest (int): un bitmask indiquant quelles étagères restent à traiter.
            dic (dict): dictionnaire pour mémorisation des résultats déjà calculés.

        Returns:
            int: la position maximale des livres pouvant être placés avec les étagères indiquées dans `rest`.
        """
        # Si le résultat est déjà calculé pour ce masque, on le retourne directement
        if rest in dic:
            return dic[rest]

        # Cas de base : si aucun étagère à traiter, on ne peut avancer (position 0)
        if rest == 0:
            return 0

        mask = 1  # masque servant à vérifier la présence d'une étagère dans rest
        ret = 0  # valeur max à retourner

        # Itérer sur chaque étagère (n étagères)
        for i in range(n):
            if rest & mask:  # vérifie si l'étagère i est dans rest
                # On enlève l'étagère i de rest pour traiter le sous-problème correspondant
                pre_rest = rest & ~mask

                # On calcule la position max possible sans l'étagère i
                temp = dp(pre_rest, dic)

                # On cherche la position max en incluant l'étagère i, à partir de la position temp
                temp = search(temp, i)

                # On garde la meilleure position possible parmi toutes les étagères
                ret = max(ret, temp)

            mask <<= 1  # passer au bit suivant pour la prochaine étagère

        # Mémoriser le résultat calculé pour ce masque
        dic[rest] = ret
        return ret

    # Lancer la programmation dynamique pour l'ensemble des étagères disponibles
    print(dp(rest, dic))

# Exécuter la fonction principale
main()