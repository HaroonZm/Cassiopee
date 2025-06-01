def process_input_and_compute():
    """
    Lit une ligne d'entrée contenant deux entiers séparés par un espace, puis effectue un calcul conditionnel :
    
    - Si le premier entier est strictement inférieur au second, affiche le premier entier.
    - Sinon, affiche la somme de la partie entière de la division du premier entier par le second
      et du reste de cette division.
    
    Exemple d'entrée : "7 3"
    Exemple de sortie : 4
    (car 7 // 3 = 2, 7 % 3 = 1, 2 + 1 = 3)
    """
    # Lecture d'une ligne d'entrée, découpage avec split(), conversion en liste d'entiers
    ins = [int(x) for x in input().split()]

    # Comparaison entre le premier et le deuxième élément
    if ins[0] < ins[1]:
        # Si le premier entier est plus petit, on l'affiche directement
        print(ins[0])
    else:
        # Sinon, on calcule la division entière et le reste,
        # on les additionne et on affiche le résultat
        division_entier = ins[0] // ins[1]
        reste = ins[0] % ins[1]
        print(division_entier + reste)


# Appel de la fonction principale pour exécuter le programme
process_input_and_compute()