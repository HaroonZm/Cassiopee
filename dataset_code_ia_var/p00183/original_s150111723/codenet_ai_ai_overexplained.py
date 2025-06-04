# Commence une boucle infinie. Cela signifie que le code qui se trouve à l'intérieur du while True: va être exécuté encore et encore, jusqu'à ce que l'on sorte explicitement de cette boucle avec un break plus loin dans le code.
while True:

    # Affiche un curseur à l'utilisateur pour saisir des données.
    # La fonction built-in input() lit une ligne saisie au clavier (en tant que chaîne de caractères).
    input_data1 = input()

    # Vérifie si la donnée saisie est exactement le caractère "0" (sous forme de chaîne).
    # Cela sert généralement à permettre à l'utilisateur d'arrêter le programme.
    if input_data1 == "0":
        # Si l'utilisateur a entré "0", on sort immédiatement de la boucle, mettant ainsi fin au programme.
        break

    # Attend une 2e entrée de la part de l'utilisateur et stocke cette chaîne dans la variable input_data2.
    input_data2 = input()
    # Attend une 3e entrée de la part de l'utilisateur et stocke cette chaîne dans la variable input_data3.
    input_data3 = input()

    # Définit la variable output avec la valeur par défaut "NA".
    # "NA" signifiera, selon la logique du programme, qu'aucune condition de victoire n'a été trouvée.
    output = "NA"

    # Première série de conditions : vérifie si une ligne contient trois mêmes caractères (ni "+")
    # On vérifie la première ligne (input_data1) :
    # Si le premier caractère n'est pas "+", et que les trois caractères de la ligne sont identiques,
    # alors on stocke dans output ce caractère (c'est probablement le symbole gagnant).
    if input_data1[0] != "+" and input_data1[0] == input_data1[1] == input_data1[2]:
        output = input_data1[0]
    # Cas similaire, mais cette fois pour la deuxième ligne (input_data2) :
    elif input_data2[0] != "+" and input_data2[0] == input_data2[1] == input_data2[2]:
        output = input_data2[0]
    # Cas similaire pour la troisième ligne (input_data3) :
    elif input_data3[0] != "+" and input_data3[0] == input_data3[1] == input_data3[2]:
        output = input_data3[0]

    # Deuxième série de conditions : vérifie si une colonne contient trois mêmes caractères (ni "+")
    # Vérifie première colonne (colonne d'indice 0)
    elif input_data1[0] != "+" and input_data1[0] == input_data2[0] == input_data3[0]:
        output = input_data1[0]
    # Vérifie deuxième colonne (colonne d'indice 1)
    elif input_data1[1] != "+" and input_data1[1] == input_data2[1] == input_data3[1]:
        output = input_data1[1]
    # Vérifie troisième colonne (colonne d'indice 2)
    elif input_data1[2] != "+" and input_data1[2] == input_data2[2] == input_data3[2]:
        output = input_data1[2]

    # Troisième série de conditions : vérifie les diagonales
    # Diagonale de haut-gauche à bas-droite : indices (0,0), (1,1), (2,2)
    elif input_data1[0] != "+" and input_data1[0] == input_data2[1] == input_data3[2]:
        output = input_data1[0]
    # Diagonale de haut-droite à bas-gauche : indices (0,2), (1,1), (2,0)
    elif input_data1[2] != "+" and input_data1[2] == input_data2[1] == input_data3[0]:
        output = input_data1[2]

    # Affiche le résultat calculé dans output.
    # Si aucune des conditions précédentes n'a été remplie, output vaut "NA".
    print(output)