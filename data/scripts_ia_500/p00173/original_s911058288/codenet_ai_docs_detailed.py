def process_input():
    """
    Lit neuf lignes depuis l'entrée standard. Chaque ligne doit contenir trois valeurs séparées par des espaces :
    - ni : une chaîne représentant un identifiant ou un nom
    - ai : un entier
    - bi : un autre entier

    Pour chaque ligne, la fonction effectue les calculs suivants :
    - somme = ai + bi
    - valeur = ai * 200 + bi * 300

    Elle affiche ensuite les résultats sous la forme : ni somme valeur

    Cette fonction ne prend aucun argument et n'a pas de valeur de retour.
    """
    # Parcours de neuf itérations car nous devons traiter neuf lignes d'entrée
    for _ in range(9):
        # Lecture d'une ligne et séparation en trois variables : ni (string), ai (string), bi (string)
        ni, ai, bi = input().split()
        
        # Conversion des chaînes de caractères ai et bi en entiers pour pouvoir faire des calculs
        ai = int(ai)
        bi = int(bi)
        
        # Calcul de la somme de ai et bi
        somme = ai + bi
        
        # Calcul d'une valeur pondérée basée sur ai et bi
        valeur = ai * 200 + bi * 300
        
        # Affichage du résultat : ni, la somme calculée, et la valeur calculée
        print(ni, somme, valeur)

# Appel de la fonction pour lancer le traitement
process_input()