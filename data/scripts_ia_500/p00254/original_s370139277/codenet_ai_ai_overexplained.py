import copy  # Importation du module copy qui permet de faire des copies profondes d'objets complexes

# Boucle infinie qui permet de traiter plusieurs entrées utilisateur successives
while 1:
    # Demande une chaîne de caractères à l'utilisateur, convertit cette chaîne en liste de caractères
    # Par exemple, si l'utilisateur entre "1234", n sera ['1', '2', '3', '4']
    n = list(input())

    # Vérification si la liste entrée par l'utilisateur est exactement ["0", "0", "0", "0"]
    # Cela sert de condition d'arrêt pour la boucle while infinie
    if n == ["0", "0", "0", "0"]:
        break  # Sortie immédiate de la boucle while

    # Conversion des caractères individuels (qui sont des chiffres sous forme de chaînes)
    # en un entier à 4 chiffres. On multiplie chaque chiffre par sa puissance de 10 correspondante
    # pour reconstruire le nombre entier.
    tmp = int(n[0]) * 1000 + int(n[1]) * 100 + int(n[2]) * 10 + int(n[3])

    # Vérifie si le nombre est divisible par 1111, ce qui signifie que les 4 chiffres sont identiques
    # Par exemple 1111, 2222, 3333, etc. Tous divisibles par 1111.
    if tmp % 1111 == 0:
        print("NA")  # Affiche "NA" pour indiquer une situation non applicable ou non valide
        continue  # Passe à la prochaine itération de la boucle while, ignore le reste du code

    cnt = 0  # Initialisation d'un compteur à zéro pour compter le nombre d'itérations suivantes

    # Boucle exécutée tant que la liste n ne correspond pas à ['6', '1', '7', '4']
    # Chaque élément de la liste représente un chiffre sous forme de caractère.
    while n != ["6", "1", "7", "4"]:
        n.sort(reverse=True)  # Trie les chiffres de la liste n dans l'ordre décroissant
        l = copy.deepcopy(n)  # Fait une copie profonde de la liste triée pour ne pas affecter n

        n.sort()  # Trie maintenant les chiffres de la liste n dans l'ordre croissant
        s = copy.deepcopy(n)  # Fait une autre copie profonde de cette liste triée dans l'ordre croissant

        # Conversion des listes l et s en entiers correspondants,
        # en multipliant chaque chiffre converti en int par sa place décimale respective
        l = int(l[0]) * 1000 + int(l[1]) * 100 + int(l[2]) * 10 + int(l[3])
        s = int(s[0]) * 1000 + int(s[1]) * 100 + int(s[2]) * 10 + int(s[3])

        # Calcul de la différence entre les deux nombres obtenus
        # Conversion du résultat en chaîne de caractères, remplissage avec des zéros à gauche 
        # pour s'assurer qu'il comporte exactement 4 caractères, puis transformation en liste de caractères
        n = list(str(l - s).zfill(4))

        cnt += 1  # Incrémente le compteur à chaque boucle, mesurant le nombre d'itérations effectuées

    # Une fois la boucle terminée (quand n == ["6", "1", "7", "4"]), on affiche le nombre d'itérations
    print(cnt)