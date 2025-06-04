import copy  # Le module copy permet de faire des copies profondes d'objets, utile pour copier des listes sans liaison avec l'original

while 1:  # Boucle infinie, s'exécutera jusqu'à ce qu'un break soit rencontré explicitement à l'intérieur de la boucle
    n = list(input())  # Demande à l'utilisateur d'entrer une chaîne de caractères, puis convertit la chaîne saisie en une liste de caractères (chaque chiffre devient un élément de liste)
    if n == ["0", "0", "0", "0"]:  # Si la liste obtenue correspond exactement à quatre zéros, on considère que c'est le signal d'arrêt
        break  # On quitte la boucle infinie grâce à l'instruction break

    # Conversion de la liste de caractères représentant un nombre de 4 chiffres en sa valeur entière numérique
    # int(n[0]) extrait le chiffre des milliers (ex: '3' devient 3) puis multiplie par 1000 pour retrouver sa valeur pondérée
    # int(n[1]) extrait le chiffre des centaines puis multiplie par 100
    # int(n[2]) extrait le chiffre des dizaines puis multiplie par 10
    # int(n[3]) extrait le chiffre des unités
    # L'addition de ces quatre quantités produit la valeur entière correspondante
    tmp = int(n[0])*1000 + int(n[1])*100 + int(n[2])*10 + int(n[3])
    if tmp % 1111 == 0:  # Si le nombre formé a quatre chiffres identiques (il est divisible par 1111, comme 2222, 3333...), alors:
        print("NA")  # Affichage de 'NA' qui signifie que ce nombre n'est pas admissible pour la suite de l'algorithme, car il n'est pas transformable selon la suite désirée
        continue  # Passe à l'itération suivante de la boucle principale sans exécuter le reste des instructions

    cnt = 0  # Initialisation d'un compteur à zéro; ce compteur va servir à compter le nombre d'itérations de l'opération principale

    # Tant que la liste des chiffres n'est pas égale à ["6", "1", "7", "4"] (c'est-à-dire tant que l'on n'a pas atteint le nombre 6174, la "constante de Kaprekar")
    while n != ["6", "1", "7", "4"]:
        n.sort(reverse=True)  # Tri de la liste des chiffres dans l'ordre décroissant (du chiffre le plus grand au plus petit)
        l = copy.deepcopy(n)  # Création d'une copie profonde de la liste triée, appelée 'l', pour représenter la version décroissante
        n.sort()  # Tri de la liste d'origine dans l'ordre croissant cette fois-ci (du chiffre le plus petit au plus grand)
        s = copy.deepcopy(n)  # Création d'une copie profonde de la liste triée dans l'ordre croissant, appelée 's'

        # Conversion de la liste des chiffres triée (ordre décroissant) en un nombre entier
        # - l[0] est le chiffre des milliers, l[1] celui des centaines, l[2] des dizaines, l[3] des unités
        # Les multiplications par 1000, 100, 10, et 1 servent à replacer chaque chiffre à sa bonne position dans le nombre final
        l = int(l[0])*1000 + int(l[1])*100 + int(l[2])*10 + int(l[3])

        # Même principe pour la version croissante
        s = int(s[0])*1000 + int(s[1])*100 + int(s[2])*10 + int(s[3])

        # Calcul de la différence entre la version décroissante et la version croissante obtenues
        # str(l-s) convertit la différence obtenue en chaîne de caractères
        # .zfill(4) ajoute des zéros en début de chaîne si besoin pour garantir que la chaîne ait exactement 4 caractères
        # list(...) convertit la chaîne de 4 caractères obtenue en une liste de caractères
        n = list(str(l-s).zfill(4))

        cnt += 1  # Incrémentation du compteur d'itérations, car une transformation supplémentaire vient d'être effectuée

    print(cnt)  # Affiche le nombre d'étapes nécessaires pour obtenir 6174 à partir du nombre initial saisi (hors cas spéciaux)