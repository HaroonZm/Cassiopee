from functools import reduce  # Importation de la fonction 'reduce' depuis le module 'functools'. 'reduce' permet d'appliquer une fonction cumulativement à une séquence d'éléments.
while True:  # Début d'une boucle infinie. La boucle continuera à s'exécuter jusqu'à ce qu'on rencontre une instruction 'break' qui la stoppe.
    n = input()  # Lecture d'une chaîne de caractères entrée par l'utilisateur via la console. La fonction 'input()' attend que l'utilisateur saisisse quelque chose et appuie sur Entrée.
    if n == '0000': break  # Si la chaîne saisie est exactement '0000', alors on arrête la boucle avec 'break'. Cela sert de condition d'arrêt pour le programme.
    if len(n) < 4: n = n.zfill(4)  # Vérifie si la longueur de la chaîne 'n' est inférieure à 4. Si oui, on complète la chaîne avec des '0' au début jusqu'à une longueur de 4 caractères. La méthode 'zfill' ajoute des zéros à gauche.
    # On vérifie maintenant si tous les caractères dans la chaîne sont identiques.
    # Pour cela, on crée une liste de valeurs booléennes où chaque élément indique si le caractère en position 0 est égal au caractère courant.
    # Par exemple, pour '1111', la liste sera [True, True, True, True]. Pour '1234', ce sera [True, False, False, False].
    all_equal = reduce(lambda x, y: x and y, [n[0] == s for s in n])  
    # 'reduce' applique la fonction 'lambda' cumulativement sur la liste: ici, elle réalise un "ET" logique entre tous les éléments.
    # Cela signifie que si tous les éléments de la liste sont True, alors 'all_equal' sera True.
    if all_equal:
        print('NA')  # Si tous les chiffres sont identiques, on affiche 'NA' (non applicable probablement car l'algorithme ne marche pas dans ce cas).
    else:
        cnt = 0  # Initialisation du compteur à zéro. Ce compteur va compter le nombre d'itérations nécessaires pour atteindre la valeur 6174.
        while n != '6174':  # Tant que la chaîne 'n' n'est pas égale à '6174', on poursuit le processus.
            # L'algorithme en question est lié à la constante de Kaprekar (6174).
            l = ''.join(sorted(n, reverse=True))  # Tri des chiffres de la chaîne 'n' en ordre décroissant, puis jointure en une nouvelle chaîne.
            s = ''.join(sorted(n))  # Tri des chiffres de la chaîne 'n' en ordre croissant, puis jointure en une nouvelle chaîne.
            # Conversion de ces chaînes de caractères en entiers, puis soustraction.
            n = str(int(l) - int(s))  # Calcul de la différence entre le nombre avec chiffres triés décroissante et celui avec chiffres triés croissante.
            if len(n) < 4: n = n.zfill(4)  # On complète avec des zéros à gauche si la longueur est inférieure à 4 caractères.
            cnt += 1  # Incrémente le compteur à chaque itération, comptabilisant le nombre d'étapes effectuées.
        print(cnt)  # Affiche le nombre d'itérations nécessaires pour que 'n' atteigne 6174.