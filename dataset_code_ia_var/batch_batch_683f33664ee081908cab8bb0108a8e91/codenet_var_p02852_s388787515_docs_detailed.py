import sys

def read_input():
    """
    Lit les valeurs de N et M, puis lit la chaîne S et l'inverse.

    Returns:
        N (int): Longueur totale de la chaîne.
        M (int): Longueur maximale de saut autorisé.
        S (str): Chaîne inversée représentant les positions libres et bloquées.
    """
    N, M = map(int, input().split())
    S = input()[::-1]    # On inverse l'entrée pour faciliter le traitement depuis le début réel.
    return N, M, S

def calculate_steps(N, M, S):
    """
    Calcule la séquence minimale de sauts pour atteindre la fin de la chaîne S en respectant les contraintes.

    Args:
        N (int): Longueur totale de la chaîne.
        M (int): Longueur maximale de saut autorisé.
        S (str): Chaîne inversée contenant '0' (libre) ou '1' (bloquée).

    Returns:
        str: Une chaîne d'entiers représentant les sauts, séparés par des espaces, ou '-1' si impossible.
    """
    ans = ''   # Chaîne qui va accumuler les sauts effectués
    i = 0      # Position actuelle dans la chaîne
    while i < N - M:
        found = False    # Indique si un saut valide a été trouvé depuis la position courante
        # On cherche le saut maximal possible allant de M à 1
        for j in range(M, 0, -1):
            if S[i + j] == '0':   # Vérifie si la destination est libre
                ans += str(j) + ' '   # Ajoute ce saut à la séquence de réponses
                i += j                # Avance à la prochaine position atteinte
                found = True
                break
        if not found:
            return '-1'      # Si aucun saut n'est possible, on retourne -1 immédiatement
    # Dernier saut pour couvrir les cases restantes jusqu'à la fin
    ans += str(N - i)
    # On inverse la séquence pour retrouver l'ordre "naturel" (puisqu'on a traité la chaîne inversée)
    return ' '.join(ans.split()[::-1])

def main():
    """
    Point d'entrée du programme.
    Lit les entrées, calcule les sauts, et affiche la solution.
    """
    N, M, S = read_input()
    result = calculate_steps(N, M, S)
    print(result)

if __name__ == "__main__":
    main()