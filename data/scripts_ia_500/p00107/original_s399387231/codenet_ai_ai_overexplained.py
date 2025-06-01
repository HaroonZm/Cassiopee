def min_diam(A,B,C): 
  # Cette fonction calcule une "diamètre" spécifique à partir de trois longueurs A, B, C.
  # Entrées :
  #  - A, B, C : trois nombres réels représentant des longueurs quelconques.
  # Sortie :
  #  - Un nombre réel représentant la racine carrée de la somme des carrés des deux plus petits côtés.
  
  segments=[A,B,C] 
  # On crée une liste contenant les trois longueurs A, B et C.
  
  segments.sort() 
  # On trie cette liste par ordre croissant. Après ce tri,
  # segments[0] est la plus petite longueur,
  # segments[1] la deuxième plus petite,
  # segments[2] la plus grande.
  
  return (segments[0]**2+segments[1]**2)**(1/2) 
  # On calcule ici la racine carrée (c'est-à-dire l'exposant 1/2) de la somme des carrés
  # des deux plus petits segments. Cela correspond à la longueur de l'hypoténuse
  # dans un triangle rectangle formé par ces deux segments (théorème de Pythagore).
  # Cette valeur est retournée par la fonction.

while True:
  # Boucle infinie qui va itérer tant qu’on ne rencontre pas une condition d'arrêt explicite.
  
  A,B,C = tuple(map(float,input().split()))
  # On lit une ligne d'entrée standard (input), qui doit contenir trois nombres séparés par des espaces.
  # La fonction input() lit la ligne en chaîne de caractères.
  # La fonction split() découpe cette chaîne en une liste de sous-chaînes (ici trois), selon les espaces.
  # La fonction map(float, ...) convertit chaque élément de cette liste en nombre réel (float).
  # Enfin, on convertit le résultat en tuple et on assigne aux variables A, B, C.
  
  if (A,B,C) == (0,0,0):
    # Teste si les trois valeurs sont toutes égales à zéro.
    # Ceci est la condition d'arrêt de la boucle.
    break
    # Si c'est vrai, on sort immédiatement de la boucle while.

  n = int(input())
  # On lit une nouvelle ligne d'entrée, censée être un entier naturel.
  # On convertit cette chaîne en entier avec int(), puis on stocke dans n.
  # Cet entier représente le nombre de valeurs suivantes à lire pour les rayons R.

  R = [None]*n
  # On crée une liste R de longueur n, initialisée avec des None (valeur vide).
  # Cette liste va contenir les valeurs de rayons à lire dans la suite.

  for i in range(n):
    R[i] = float(input())
    # Pour chaque index i de 0 jusqu'à n-1,
    # on lit une ligne depuis l'entrée standard,
    # on convertit la chaîne en float et on stocke dans R[i].

  diam = min_diam(A,B,C)
  # On appelle la fonction définie plus haut
  # pour calculer le "diamètre" correspondant aux valeurs A, B, C.
  # On stocke ce résultat dans la variable diam.

  for r in R:
    # Pour chaque rayon r dans la liste des rayons R,
    
    if diam < 2*r:
      # On compare la valeur diam au double du rayon r.
      # La condition représente probablement si le diamètre est plus petit que le diamètre du cercle de rayon r.
      
      print("OK")
      # Si diam est strictement inférieur à 2*r,
      # on affiche la chaîne de caractères "OK" sur la sortie standard.

    else:
      # Sinon (si diam >= 2*r),
      
      print("NA")
      # On affiche la chaîne "NA" (non acceptable ?).
      # Ceci constitue la sortie conditionnelle pour chaque rayon donné.