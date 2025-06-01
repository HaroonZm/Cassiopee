ans = []  # Initialisation d'une liste vide qui contiendra toutes les chaînes de résultats à afficher à la fin.

while True:
    # Boucle infinie qui ne sera interrompue que par l'instruction 'break'.
    n = input()  # Lecture de l'entrée utilisateur sous forme de chaîne de caractères.
    
    # La condition qui suit semble attendre une valeur nulle pour sortir, mais input renvoie une chaîne, donc la comparaison avec 0 est incorrecte.
    # Il faudrait convertir la valeur en entier pour comparaison correcte.
    n = int(n)  # Convertir la chaîne lue en entier pour pouvoir effectuer des comparaisons numériques.
    if n == 0:
        # Si l'utilisateur entre 0, on arrête la boucle infinie.
        break
    
    c = 1  # Initialiser le compteur à 1. Ce compteur sera utilisé pour positionner les valeurs dans le cercle.
    N = n * n  # Calculer N qui est le carré de n. Cela représente la taille totale de la structure circulaire à remplir.
    circle = [0] * N  # Créer une liste de taille N remplie de 0. Cela servira de structure pour stocker les valeurs placées.
    
    # Définir la position initiale p. Le calcul est (N+1)/2 -1, qui trouve un index à peu près au centre (on note que l'indice commence à 0).
    p = (N + 1) // 2 - 1  # Utilisation de l'opérateur // pour division entière afin d'éviter un float.
    
    while c <= N:
        # Boucle qui se répète tant que le compteur c n'a pas dépassé N.
        
        # Conditions pour ajuster la position p selon certains indices et contraintes.
        if p == N:
            p = 1  # Si on atteint la fin de la liste (indice N, hors limite 0-based), on revient à l'indice 1 (2ème position).
        elif p % n == 0:
            p += 1  # Si p est un multiple de n, on l'incrémente de 1 pour éviter cette position.
        elif p + n > N:
            p -= (N - n - 1)  # Si p + n dépasse N, on recule selon ce calcul.
        else:
            p += n + 1  # Sinon, on incrémente p de n+1.
        
        # Si la position dans 'circle' est déjà occupée, on ajuste p avec une nouvelle boucle.
        if circle[p - 1] != 0:
            while circle[p - 1] != 0:
                # Condition pour gérer aussi les bords et repositionner p.
                if p == N - n + 1:
                    p = n
                elif (p - 1) % n == 0:
                    p += (n * 2 - 1)
                elif p + n > N:
                    p -= N - n + 1
                else:
                    p += n - 1
        
        # Après ajustement, on place la valeur c à la position p-1 de la liste 'circle'.
        circle[p - 1] = c
        c += 1  # Incrémenter le compteur pour la prochaine valeur.
    
    # Préparer une chaîne temporaire 'temp' qui va contenir la représentation formatée de 'circle' en lignes de n éléments.
    p = 0  # Réinitialiser p pour la boucle de formatage.
    temp = ''  # Chaîne vide pour accumuler la sortie formatée.
    
    while p * n != N:
        # Pour chaque ligne, on extrait une tranche de n éléments dans 'circle'.
        # map applique la fonction lambda sur chaque élément de la tranche, qui convertit l'élément en chaîne droite justifiée sur 4 caractères.
        # join concatène toutes ces chaînes ensemble en une seule ligne.
        temp += ''.join(map(lambda x: str(x).rjust(4), circle[n * p:n * (p + 1)]))
        temp += '\n'  # Ajouter un saut de ligne après chaque ligne.
        p += 1  # Passer à la ligne suivante.
    
    # On ajoute cette chaîne formatée sans les espaces qui pourraient traîner en fin ou saut de lignes inutiles à la liste 'ans'.
    ans.append(temp.rstrip())

# Après avoir collecté tous les résultats pour toutes les entrées, on les affiche chacun sur une ligne.
for i in ans:
    print i  # Affichage de chaque chaîne enregistrée dans 'ans'. En Python 3, il faudrait print(i).