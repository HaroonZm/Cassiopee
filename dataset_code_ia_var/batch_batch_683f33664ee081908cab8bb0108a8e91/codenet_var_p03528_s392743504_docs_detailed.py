def generate_sequences(N, K):
    """
    Génère et retourne des séquences d'entiers selon un schéma mathématique particulier.
    
    Args:
        N (int): Le nombre total de séquences générées (doit correspondre au nombre de sous-listes générées).
        K (int): Un paramètre contrôlant la structure et la taille des séquences.
    
    Returns:
        List[List[int]]: Une liste de listes d'entiers générée selon l'algorithme décrit.
    """
    ans = []

    # Première phase : Construction des K premières séquences de taille K
    for i in range(K):
        # La première valeur de chaque séquence est 1, suivie d'une séquence consécutive dépendant de K et de l'itérateur i
        # La formule ((K-1)*i + 2) donne le début de la séquence, et on va jusqu'à ((K-1)*(i+1) + 2) exclus
        tmp = [1] + list(range((K-1)*i + 2, (K-1)*(i+1) + 2))
        ans.append(tmp)

    # Deuxième phase : Construction des séquences restantes
    # On itère sur i à partir de 1 jusqu'à K-1, produisant (K-1)*K séquences supplémentaires
    for i in range(1, K):
        for j in range(K-1):
            tmp = [i + 1]  # La première valeur de la séquence est i + 1
            # Ajout de K-1 éléments supplémentaires calculés selon une formule à base de modulo et de décalages
            for k in range(K-1):
                # La formule suivante calcule un entier unique pour chaque position
                value = K + ((j + (i - 1) * k) % (K - 1)) + k * (K - 1) + 1
                tmp.append(value)
            ans.append(tmp)

    return ans

def main():
    """
    Point d'entrée principal.
    Définit les paramètres N et K, génère les séquences et les affiche de façon formatée.
    """
    N = 1407  # Nombre total de séquences à générer (doit correspondre à la sortie réelle)
    K = 38    # Paramètre de structure des séquences

    # Génération des séquences via la fonction dédiée
    ans = generate_sequences(N, K)

    # Affichage du nombre total de séquences et du paramètre K
    print(N, K)

    # Parcours de toutes les séquences et affichage des éléments de chaque sous-liste, séparés par des espaces
    for sequence in ans:
        print(*sequence)

if __name__ == "__main__":
    main()