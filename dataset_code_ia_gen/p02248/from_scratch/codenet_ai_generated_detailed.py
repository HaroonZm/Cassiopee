# Solution complète en Python pour la recherche de toutes les occurrences d'une chaîne P dans un texte T.
# Cette solution utilise l'algorithme de recherche de pattern KMP (Knuth-Morris-Pratt) pour une efficacité optimale.
# KMP permet de rechercher P dans T en temps linéaire O(n + m), où n est la longueur de T et m la longueur de P.

def kmp_search(text, pattern):
    """
    Recherche toutes les positions où 'pattern' apparaît dans 'text' grâce à l'algorithme KMP.
    
    Args:
    text (str): Le texte dans lequel on cherche.
    pattern (str): La chaîne recherchée.
    
    Returns:
    List[int]: Liste des indices où 'pattern' commence dans 'text'.
    """
    n = len(text)
    m = len(pattern)
    
    # Fonction pour construire le tableau des préfixes (longueurs des suffixes propres préfixes maximaux)
    def build_lps(pattern):
        lps = [0] * m  # lps[i] = plus longue longueur de préfixe suffixe propre jusqu'à i
        length = 0  # longueur du prefixe suffixe propre le plus long pour le préfixe précédent
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    lps = build_lps(pattern)
    indices = []
    
    i = 0  # index pour text
    j = 0  # index pour pattern
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                # On a trouvé une occurrence
                indices.append(i - j)
                j = lps[j - 1]  # continuer la recherche pour les occurrences suivantes
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return indices


# Lecture des entrées
T = input().rstrip()
P = input().rstrip()

# Recherche des indices
positions = kmp_search(T, P)

# Affichage des indices dans l'ordre croissant
for pos in positions:
    print(pos)