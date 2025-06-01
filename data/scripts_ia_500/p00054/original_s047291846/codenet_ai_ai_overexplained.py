import sys  # Import de la bibliothèque standard 'sys' qui permet d'interagir avec des fonctionnalités spécifiques du système, ici pour lire l'entrée standard

# Lecture de chaque ligne de l'entrée standard (les lignes sont fournies sous forme de texte brut)
for a, b, n in (map(int, l.split()) for l in sys.stdin.readlines()):
    # La ligne 'sys.stdin.readlines()' renvoie une liste de toutes les lignes lues depuis l'entrée standard
    # Pour chaque ligne l dans cette liste :
    #    - On découpe la chaîne de caractères l en sous-chaînes à chaque espace avec 'l.split()', ce qui donne une liste de chaînes
    #    - On convertit chaque élément de cette liste en entier avec la fonction 'map(int, ...)', ce qui produit un itérable d'entiers
    #    - On affecte successivement ces entiers aux variables a, b, et n

    # Condition : si le premier entier 'a' est plus grand ou égal à 'b'
    if a >= b:
        # On remplace 'a' par son reste modulo 'b', c'est-à-dire ce qu'il reste après la division entière de 'a' par 'b'
        # Cela revient à faire 'a = a % b'
        a %= b
        
    # On multiplie 'a' par 10 pour déplacer la "virgule" décimale d'un chiffre vers la droite
    a *= 10
    
    # Initialisation de la variable 'ans' à 0, qui servira à accumuler la somme des chiffres extraits
    ans = 0
    
    # On effectue une boucle qui répète 'n' fois, ici écrite de manière pythonique en utilisant une liste temporaire [0]*n
    # Cette liste est une manière de générer n occurrences de la valeur 0, et on itère dessus simplement pour faire n tours
    for _ in [0]*n:
        # La fonction divmod retourne un tuple contenant le quotient et le reste de la division entière de 'a' par 'b'
        d, m = divmod(a, b)
        
        # On ajoute à la variable 'ans' la valeur du quotient 'd' de la division
        ans += d
        
        # On prépare 'a' pour le prochain tour, en multipliant le reste 'm' par 10 pour "déplacer la virgule"
        a = m * 10
        
    # À la fin de la boucle, on affiche la valeur de 'ans' calculée, c'est-à-dire la somme des 'n' premiers chiffres de la représentation décimale de a/b
    print(ans)