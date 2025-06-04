def min_common_char_multiset(n, S):
    """
    Calcule le multiensemble de caractères communs minimums parmi une liste de chaînes.

    Pour chaque caractère de 'a' à 'a'+26, compte la quantité minimale trouvée dans chaque chaîne.
    Utilisé principalement pour déterminer le multiensemble d'intersection de plusieurs chaînes.

    Args:
        n (int): Le nombre de chaînes de la liste.
        S (list of str): La liste des chaînes à examiner.

    Returns:
        str: Une chaîne composée des caractères communs, chaque caractère répété selon son minimum de présence.
    """
    # Initialise un tableau pour compter la fréquence minimale de chaque lettre ('a' à 'a'+26)
    cnt = [10**9] * 28  # On prend 28 pour couvrir 'a' à 'a'+27 (bien que normalement 26 suffisent)

    # Parcourt chaque chaîne dans la liste
    for s in S:
        # Pour chaque lettre de l'alphabet de 'a' à 'a'+26
        for i in range(27):
            # Comptabilise le minimum de présence du caractère courant dans toutes les chaînes
            cnt[i] = min(cnt[i], s.count(chr(ord("a") + i)))

    # Après avoir parcouru toutes les chaînes, met à zéro les lettres jamais vues
    for i in range(27):
        if cnt[i] == 10**9:
            cnt[i] = 0

    # Construit le résultat en ajoutant chaque caractère le nombre minimum de fois trouvé
    ans = ""
    for i in range(27):
        ans += chr(ord("a") + i) * cnt[i]

    return ans

def main():
    """
    Point d'entrée du script.
    Lit l'entrée utilisateur, puis affiche la chaîne correspondant au multiensemble commun minimal.
    """
    # Lit le nombre de chaînes
    n = int(raw_input())
    # Lit chacune des chaînes dans une liste
    S = [raw_input() for _ in xrange(n)]
    # Calcule et affiche le résultat
    print min_common_char_multiset(n, S)

if __name__ == "__main__":
    main()