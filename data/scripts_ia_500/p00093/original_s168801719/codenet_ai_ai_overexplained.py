import sys

# Initialisation d'un compteur à zéro. Ce compteur sera utilisé pour gérer l'affichage d'une ligne vide entre les différents jeux de résultats.
c = 0

# Boucle qui itère sur chaque ligne d'entrée reçue via sys.stdin.
# sys.stdin permet de lire les données fournies en entrée standard, ligne par ligne.
for s in sys.stdin:
  
    # Chaque ligne d'entrée est supposée contenir deux nombres entiers séparés par un espace.
    # La méthode split() découpe la chaîne 's' en une liste de sous-chaînes en se basant sur l'espace par défaut.
    # La fonction map applique la conversion int à chaque élément de la liste résultante, retournant un itérable d'entiers.
    a, b = map(int, s.split())
    
    # Condition de sortie de la boucle.
    # Si les deux entiers lus sont égaux et valent zéro, on interrompt la lecture.
    # Ceci signifie que la séquence de données est terminée.
    if a == b == 0:
        break
    
    # Création d'une liste vide pour stocker les années qui satisfont une certaine condition définie plus loin.
    x = []
    
    # Parcours de toutes les années depuis 'a' jusqu'à 'b' inclus.
    # La fonction range(a, b+1) génère une séquence d'entiers depuis a jusqu'à b.
    for i in range(a, b + 1):
        
        # Pour chaque année i, on applique des tests pour déterminer si elle est bissextile.
        # Première condition : l'année doit être divisible par 4 (multiple de 4).
        if i % 4 == 0:
            
            # Si l'année est divisible par 400, elle est considérée bissextile sans exception.
            if i % 400 == 0:
                x.append(i)  # Ajout de l'année à la liste des années bissextiles.
            
            # Sinon, si elle est divisible par 100 mais pas par 400, elle n'est pas bissextile, on ignore.
            # En revanche, si elle n'est pas divisible par 100 (donc multiples de 4 mais non multiples de 100),
            # elle est aussi considérée comme bissextile.
            elif i % 100 != 0:
                x.append(i)
    
    # Si ce n'est pas la première fois que l'on affiche un résultat (c != 0),
    # on imprime une ligne vide pour séparer visuellement les groupes de résultats.
    if c:
        print()
    
    # Si la liste x est vide, cela signifie qu'aucune année bissextile n'a été trouvée dans l'intervalle donné.
    # On affiche alors la chaîne "NA" pour indiquer l'absence de résultats.
    if x == []:
        print("NA")
    else:
        # Sinon, on parcourt chaque élément de la liste x et on l'affiche sur une ligne séparée.
        for e in x:
            print(e)
    
    # Mise à jour du compteur pour indiquer qu'un groupe de résultats a été affiché,
    # Cela permettra d'insérer une ligne vide avant le prochain groupe si nécessaire.
    c = 1