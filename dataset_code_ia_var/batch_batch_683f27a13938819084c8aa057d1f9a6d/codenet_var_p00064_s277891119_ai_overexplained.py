import re  # Importe le module 're' qui permet de travailler avec les expressions régulières en Python

S = 0  # Initialise une variable 'S' à 0 ; elle servira à accumuler la somme totale

while True:  # Démarre une boucle infinie, qui continuera jusqu'à ce qu'une condition d'arrêt explicite soit rencontrée
    try:  # Utilise un bloc 'try' pour capturer et gérer les exceptions éventuelles qui pourraient se produire dans le bloc associé
        x = input()  # Attend que l'utilisateur saisisse une ligne de texte puis affecte cette valeur à la variable 'x'
        
        # Compile une expression régulière qui correspond à une ou plusieurs chiffres consécutifs ('\d+' signifie une séquence de chiffres, 1 ou plusieurs)
        R = re.compile("\d+")
        
        # Applique l'expression régulière compilée sur la chaîne 'x' pour en extraire toutes les correspondances de séquences de chiffres
        # La méthode findall retourne une liste de toutes ces correspondances sous forme de chaînes
        m = R.findall(x)
        
        # Utilise une compréhension de liste pour convertir chaque élément de la liste 'm' (qui sont des chaînes représentant des nombres) en un entier
        # Parcourt chaque élément 's' dans 'm' et applique int(s) pour obtenir la version entière correspondante
        M = [int(s) for s in m]
        
        # Calcule la somme de tous les entiers extraits de la ligne courante (la liste 'M')
        # Ajoute cette somme à la variable d'accumulation 'S'
        S += sum(M)
    
    # Ce bloc 'except' capte spécifiquement une exception de type EOFError, qui se produit lorsque la fonction input() est privée de données à lire (fin de fichier)
    except EOFError:
        break  # Si une EOFError est levée, la boucle infinie est interrompue grâce au mot-clé 'break'

# À la sortie de la boucle (lorsque l'utilisateur a terminé la saisie), affiche la somme totale accumulée dans la variable 'S'
print(S)