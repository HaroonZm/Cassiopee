# Demande à l'utilisateur combien de cas de test il souhaite exécuter.
nombre_de_tests = int(input())

# Boucle qui s'exécutera pour chaque cas de test.
for i in range(nombre_de_tests):
    # Prend une ligne d'entrée de l'utilisateur, divise la chaîne en parts en utilisant l'espace comme séparateur,
    # puis convertit chaque part en entier. Les valeurs obtenues sont stockées dans les variables m et n.
    m, n = map(int, input().split())

    # Initialise le compteur à zéro. Ce compteur va servir à compter le nombre de solutions validées selon le critère plus bas.
    count = 0

    # Boucle externe : la variable 'p' va de 0 inclus jusqu'à 141 inclus (car range(142) s'arrête juste avant 142).
    for p in range(142):

        # Boucle interne, imbriquée dans la précédente : la variable 'q' varie aussi de 0 à 141 inclus.
        for q in range(142):

            # Vérifie si à la fois p et q sont égaux à zéro.
            # Si c'est le cas, on utilise 'continue' pour passer immédiatement à la prochaine itération de la boucle 'q',
            # car (p, q) = (0, 0) n'est pas un cas valide pour ce problème (probablement car cela causerait une division par zéro dans les calculs suivants).
            if p == 0 and q == 0:
                continue

            # Calcule la somme du carré de p et du carré de q. Stocke cette somme dans la variable pq.
            # Cette valeur est utilisée plus bas à la fois comme seuil et comme dénominateur.
            pq = p * p + q * q

            # Si la valeur de pq est strictement supérieure à 20000, on quitte la boucle interne actuelle (sur 'q') prématurément en utilisant 'break'.
            # Cela signifie que, parce que q ne peut qu'augmenter dans cette boucle, aucune valeur future de q ne donnera un pq plus petit, donc on passe à l'itération suivante de 'p'.
            if pq > 20000:
                break

            # Teste deux conditions simultanément :
            # 1) (m * p + n * q) modulo pq est égal à zéro. Cela veut dire que m * p + n * q est divisible par pq.
            # 2) (n * p - m * q) modulo pq est aussi zéro, donc n * p - m * q est aussi divisible par pq.
            # Si ces deux conditions sont remplies, alors nous considérons avoir trouvé une solution valide.
            if (m * p + n * q) % pq == 0 and (n * p - m * q) % pq == 0:
                # Si la condition précédente est vraie, on incrémente le compteur de un.
                count += 1

    # Après avoir testé toutes les p et q possibles pour ce cas de test, 
    # on vérifie la valeur finale du compteur.
    # Si le nombre de solutions trouvées est strictement inférieur à 5, alors on affiche "P".
    if count < 5:
        print("P")
    # Sinon, si le nombre de solutions est supérieur ou égal à 5, on affiche "C".
    else:
        print("C")