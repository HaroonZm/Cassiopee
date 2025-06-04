def find_missing_x(signal):
    """
    Analyse une séquence de signaux, identifiant les valeurs possibles pour les places occupées par 'x'.
    Les valeurs numériques doivent respecter certaines contraintes d'ordre alterné selon leur position.

    Args:
        signal (list of str): Liste représentant la séquence de signaux ("x" ou nombres en tant que chaînes).

    Returns:
        str or int: "none" si impossible, "ambiguous" si plusieurs solutions, ou la valeur trouvée pour 'x'.
    """
    MAX = 10**9 * 2  # Définition d'une valeur maximale pour limiter l'espace de recherche
    N = len(signal)  # Nombre d'éléments dans la séquence
    xst = MAX + 1    # Borne supérieure pour le candidat 'x', initialisée au maximum
    xlt = - xst      # Borne inférieure, initialisée au minimum

    for i in range(N):
        if signal[i] == "x":
            # Si deux 'x' se suivent directement, problème insoluble
            if i < N-1 and signal[i+1] == "x":
                return "none"
            if (i + 1) % 2 != 0: # Cas où l'index (1-based) est impair
                # On prend la valeur de gauche et de droite pour contraindre 'x' par le minimum
                left = MAX + 1 if i <= 0 else int(signal[i-1])
                right = MAX + 1 if i >= N-1 else int(signal[i+1])
                xst = min(xst, left, right)
            else:
                # Index pair (1-based), contrainte sur la borne inférieure
                left = - (MAX + 1) if i <= 0 else int(signal[i-1])
                right = - (MAX + 1) if i >= N-1 else int(signal[i+1])
                xlt = max(xlt, left, right)
        elif i < N-1 and signal[i+1] != "x":
            # On vérifie la cohérence de l'alternance de valeurs connues
            if ((i + 1) % 2 != 0 and int(signal[i]) >= int(signal[i+1]) or
                (i + 1) % 2 == 0 and int(signal[i]) <= int(signal[i+1])):
                return "none"

    # Après analyse, on cherche s'il existe une ou plusieurs valeurs de 'x' valides
    x = "none"
    tmpx = xlt + 1
    while tmpx < xst:
        if x != "none":
            return "ambiguous"  # Plus d'une valeur possible
        x = tmpx
        tmpx += 1
    else:
        return x

def main():
    """
    Exécute la boucle principale : lit les entrées utilisateur, applique find_missing_x,
    puis affiche le résultat pour chaque cas, jusqu'à ce que l'entrée soit 0.
    """
    MAX = 10**9 * 2
    while True:
        N = int(raw_input())
        if N == 0:
            break
        # Lecture de la séquence de signaux (chaîne), séparation sur les espaces
        signal = raw_input().split(" ")
        result = find_missing_x(signal)
        print result

# Point d'entrée du script
if __name__ == "__main__":
    main()