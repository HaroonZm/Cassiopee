# Démarre une boucle infinie afin de continuer à traiter les entrées tant qu'il n'y a pas d'erreur ou d'interruption
while 1:
    try:
        # Demander à l'utilisateur une entrée au clavier. raw_input() lit une ligne de texte depuis la console et la retourne comme une chaîne de caractères.
        # float(...) convertit cette chaîne en nombre à virgule flottante (float), ce qui permet de traiter des nombres décimaux.
        a = s = float(raw_input())
        # Ici, nous affectons la valeur convertie à deux variables : 'a' et 's'. Cela signifie que 'a' et 's' contiennent la même valeur initiale.

        # Boucle sur les entiers de 2 à 10 inclus. range(2, 11) génère la séquence : 2, 3, 4, ..., 10
        # 'i' prend donc successivement toutes ces valeurs pendant la boucle
        for i in range(2, 11):
            # Teste si la valeur de 'i' est paire (modulo 2 égal à 0)
            if i % 2 == 0:
                # Si 'i' est pair, multiplier la variable 'a' par 2.0 (nombre décimal pour forcer un float)
                a *= 2.0
                # Ajouter la nouvelle valeur de 'a' au total stocké dans 's'
                s += a
            else:
                # Si 'i' est impair, diviser la variable 'a' par 3.0 pour obtenir un float
                a /= 3.0
                # Ajouter cette nouvelle valeur à 's'
                s += a
        # Affiche le résultat final accumulé dans 's'
        print s
    except:
        # Si une exception survient (par exemple : entrée invalide, fin de fichier, etc.), sortir de la boucle avec 'break'
        break