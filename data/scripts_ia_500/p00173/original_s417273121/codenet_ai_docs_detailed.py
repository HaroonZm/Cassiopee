def process_inputs():
    """
    Lit neuf fois une ligne d'entrée contenant une chaîne de caractères suivie de deux entiers séparés par des espaces.
    Pour chaque entrée, la fonction effectue les opérations suivantes :
    - Convertit les deux derniers éléments en entiers.
    - Calcule la somme des deux entiers.
    - Calcule une valeur pondérée en multipliant le premier entier par 200 et le second par 300, puis en les additionnant.
    - Affiche la chaîne de caractères initiale, la somme et la valeur pondérée calculée.
    
    Entrée attendue par ligne : <chaîne> <entier_a> <entier_b>
    Exemple d'entrée : A 3 4
    Exemple de sortie pour l'entrée ci-dessus : A 7 1800
    """
    for _ in range(9):
        # Lecture et découpage de la ligne d'entrée en trois variables
        n, a, b = input().split()
        # Conversion des chaînes a et b en entiers
        a = int(a)
        b = int(b)

        # Calcul de la somme de a et b
        somme = a + b
        # Calcul de la valeur pondérée selon les coefficients 200 et 300 respectivement
        valeur_ponderee = 200 * a + 300 * b

        # Affiche les résultats au format demandé
        print(n, somme, valeur_ponderee)

# Appel de la fonction principale
process_inputs()