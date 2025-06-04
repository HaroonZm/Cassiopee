def read_input():
    """
    Lit la valeur de N (nombre de chaînes) ainsi que les N chaînes de caractères depuis l'entrée standard.

    Returns:
        tuple: Un entier N et une liste de chaînes S.
    """
    N = int(input())
    S = [input() for _ in range(N)]
    return N, S

def count_alphabet_occurrences(S, alphabet):
    """
    Compte les occurrences des lettres de l'alphabet dans chaque chaîne de la liste S.

    Args:
        S (list of str): Liste des chaînes à analyser.
        alphabet (str): Chaîne représentant l'alphabet à considérer.

    Returns:
        list of list of int: Matrice des décomptes par mot, de taille (len(S), len(alphabet)).
    """
    counts = [[0 for _ in range(len(alphabet))] for _ in range(len(S))]
    for i in range(len(S)):
        for char in S[i]:
            if char in alphabet:  # Pour s'assurer que seuls les caractères de l'alphabet sont pris.
                index = alphabet.index(char)
                counts[i][index] += 1
    return counts

def get_common_chars(counts, alphabet):
    """
    Détermine, pour chaque lettre de l'alphabet, le nombre minimum d'occurrences trouvées
    dans toutes les chaînes afin de former la liste des caractères communs à repléter.

    Args:
        counts (list of list of int): Matrice des occurrences par chaîne (dimensions: chaînes x lettres).
        alphabet (str): Alphabet utilisé pour l'analyse statistique.

    Returns:
        str: Chaîne représentant la concaténation des caractères communs à toutes les chaînes,
             chacun répété selon le nombre minimal d'occurrences.
    """
    # Transpose la matrice pour travailler lettre par lettre (plutôt que par mot)
    transposed_counts = list(zip(*counts))
    result = []
    for i in range(len(alphabet)):
        min_count = min(transposed_counts[i])
        # Ajoute la lettre répétée min_count fois
        result.append(alphabet[i] * min_count)
    return ''.join(result)

def main():
    """
    Fonction principale :
    - Lit les entrées,
    - Calcule les occurrences de chaque lettre dans chaque chaîne,
    - Trouve quels caractères sont communs à toutes les chaînes (au minimum),
    - Affiche la chaîne finale.
    """
    # On définit l'alphabet à utiliser
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Lecture des données
    N, S = read_input()
    # Calcul des occurrences de chaque lettre pour chaque mot
    counts = count_alphabet_occurrences(S, alphabet)
    # Construction de la réponse selon les lettres communes à toutes les chaînes
    answer = get_common_chars(counts, alphabet)
    print(answer)

# Exécute le programme principal uniquement si ce module est lancé directement
if __name__ == '__main__':
    main()