# Boucle infinie qui continue à s'exécuter jusqu'à ce qu'on rencontre une instruction 'break'
while True:
    # Initialisation de la variable s_m à 0 pour cumuler un total pour chaque itération de la boucle externe
    s_m = 0

    # Lecture d'une entrée utilisateur, conversion en entier, et stockage dans la variable n
    n = int(input())

    # Si n vaut 0, on sort de la boucle infinie grâce à l'instruction 'break'
    # C'est une condition d'arrêt pour ce programme
    if n == 0:
        break

    # Exécution d'une boucle venant n fois, indiquée ici par 'range(n)'
    # Cette boucle récupère des données à chaque itération
    for i in range(n):
        # On lit une ligne d'entrée, on sépare les valeurs en plusieurs variables x, y, h et w
        # map(int, input().split()) transforme chaque valeur lue en entier
        x, y, h, w = map(int, input().split())

        # Calcul de la somme de x, y, et h, qui semble correspondre à une mesure combinée
        # Ensuite on vérifie si cette somme et la valeur de w respectent certaines conditions
        # Selon ces conditions, un certain nombre est ajouté à s_m

        # Condition 1 : La somme x+y+h est inférieure ou égale à 60 et w est inférieur ou égal à 2
        if x + y + h <= 60 and w <= 2:
            # Ajout de 600 à s_m car les conditions ci-dessus sont vraies pour ce cas
            s_m += 600

        # Condition 2 : La somme x+y+h est inférieure ou égale à 80 et w est inférieur ou égal à 5
        elif x + y + h <= 80 and w <= 5:
            # Ajout de 800 à s_m pour ce cas
            s_m += 800

        # Condition 3 : La somme x+y+h est inférieure ou égale à 100 et w est inférieur ou égal à 10
        elif x + y + h <= 100 and w <= 10:
            # Ajout de 1000 à s_m
            s_m += 1000

        # Condition 4 : La somme x+y+h est inférieure ou égale à 120 et w est inférieur ou égal à 15
        elif x + y + h <= 120 and w <= 15:
            # Ajout de 1200 à s_m
            s_m += 1200

        # Condition 5 : La somme x+y+h est inférieure ou égale à 140 et w est inférieur ou égal à 20
        elif x + y + h <= 140 and w <= 20:
            # Ajout de 1400 à s_m
            s_m += 1400

        # Condition 6 : La somme x+y+h est inférieure ou égale à 160 et w est inférieur ou égal à 25
        elif x + y + h <= 160 and w <= 25:
            # Ajout de 1600 à s_m
            s_m += 1600

    # Après avoir traité toutes les entrées pour cette valeur de n, on affiche la somme totale s_m calculée
    print(s_m)