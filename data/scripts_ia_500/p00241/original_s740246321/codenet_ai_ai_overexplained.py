# Démarrage d'une boucle infinie qui continuera à s'exécuter indéfiniment
# jusqu'à ce qu'une condition spécifique mette fin à son exécution.
while True:
  # Lecture de l'entrée utilisateur sous forme de chaîne de caractères,
  # puis conversion de cette chaîne en un entier, qui est stocké dans la variable n.
  n = int(input())
  
  # Vérification de la valeur de n. Si n est égal à 0,
  # cela signifie que l'on doit sortir de la boucle infinie,
  # donc utilisation de "break" pour arrêter la boucle while.
  if n == 0:
    break
  
  # Boucle for qui s'exécute précisément n fois. L'underscore (_) est utilisé
  # comme variable de boucle quand cette variable n'est pas utilisée dans le bloc.
  for _ in range(n):
    # Lecture d'une ligne d'entrée utilisateur, contenant huit valeurs séparées par des espaces.
    # La méthode input() lit cette ligne sous forme de chaîne, la méthode split() sépare
    # cette chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur.
    # La fonction map applique la fonction int à chaque élément de la liste pour les convertir en entiers.
    # Enfin, ces huit entiers sont décompressés et assignés aux variables x1, y1, z1, w1, x2, y2, z2, w2.
    x1, y1, z1, w1, x2, y2, z2, w2 = map(int, input().split())
    
    # Calcul de la composante x du produit de deux quaternions.
    # Multiplication et soustraction selon la formule spécifique aux quaternions.
    x3 = x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2
    
    # Calcul de la composante y du produit de deux quaternions,
    # suivant la formule de multiplication quaternionique.
    y3 = x1 * y2 + y1 * x2 + z1 * w2 - w1 * z2
    
    # Calcul de la composante z du produit de deux quaternions,
    # en respectant toujours la multiplication quaternionique.
    z3 = x1 * z2 - y1 * w2 + z1 * x2 + w1 * y2
    
    # Calcul de la composante w du produit de deux quaternions,
    # selon la formule standard.
    w3 = x1 * w2 + y1 * z2 - z1 * y2 + w1 * x2
    
    # Affichage des quatre composantes calculées à l'écran,
    # séparées par des espaces. Cela correspond au résultat du produit quaternionique.
    print(x3, y3, z3, w3)