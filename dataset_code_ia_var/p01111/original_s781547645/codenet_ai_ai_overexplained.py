# Initialisation d'une liste vide qui servira à stocker les résultats finaux pour chaque entrée utilisateur.
ans = []

# Démarrage d'une boucle infinie. Le programme en sortira uniquement en rencontrant un 'break'.
while 1:

    # Demande à l'utilisateur de saisir un nombre entier et convertit l'entrée texte en un entier grâce à int().
    b = int(input())
    
    # Si l'utilisateur saisit 0, cela signifie qu'il souhaite arrêter le programme.
    if b == 0:
        # Interruption immédiate de la boucle 'while', ce qui sortira du programme principal de saisie.
        break
    
    # Initialisation de la variable x à 1. x servira à parcourir tous les diviseurs potentiels de b.
    x = 1
    # Initialisation de 'res' à (1, 1). Cette variable va stocker temporairement le meilleur couple (b, a) trouvé.
    res = (1, 1)
    
    # Boucle qui va tester tous les 'x' tels que x * x <= b. De cette manière, on ne teste que jusqu'à la racine carrée de b.
    # Cela optimise le temps d'exécution car les diviseurs de b sont trouvés par paires.
    while x * x <= b:
        
        # On vérifie si 'x' est effectivement un diviseur de 'b' en testant le reste de la division (modulo).
        if b % x == 0:
            
            # Si 'x' est un diviseur, alors il existe un autre diviseur 'y' tel que x * y == b.
            y = b // x
            
            # On vérifie si 'x' est impair en testant le reste de la division par 2. Si x % 2 vaut 1, x est impair.
            if x % 2 == 1:
                
                # Teste si la quantité 'y - x//2' est supérieure ou égale à 1.
                # x//2 correspond à la division entière de x par 2. On utilise '//' pour obtenir un entier sans décimale.
                if y - x // 2 >= 1:
                    # On met à jour 'res' en gardant la valeur maximale (en termes lexicographiques) entre sa valeur actuelle et le couple (x, y - x//2).
                    # 'max' appliqué à des tuples compare d'abord le premier élément, puis le second en cas d'égalité.
                    res = max(res, (x, y - x // 2))
                
                # On vérifie aussi l'autre possibilité : si 'x//2 - y + 1' est >= 1.
                if x // 2 - y + 1 >= 1:
                    # Mise à jour de 'res' avec le couple (2*y, x//2 - y + 1) si c'est plus grand au sens des tuples.
                    res = max(res, (2 * y, x // 2 - y + 1))
            
            # On refait des vérifications similaires, mais avec 'y' au lieu de 'x' pour couvrir tous les cas possibles.
            if y % 2 == 1:
                
                if x - y // 2 >= 1:
                    res = max(res, (y, x - y // 2))
                
                if y // 2 - x + 1 >= 1:
                    res = max(res, (2 * x, y // 2 - x + 1))
        
        # Incrémentation de 'x' de 1 à chaque itération de boucle interne pour tester le diviseur suivant.
        x += 1
    
    # Après la recherche, 'res' contient le meilleur couple (b_value, a_value).
    # On échange l'ordre en extrayant b et a depuis le tuple 'res' (b, a) = res.
    b, a = res
    
    # On formate l'information trouvée sous la forme d'une chaîne de caractères "a b" en utilisant '%d' pour s'assurer que ce sont des entiers.
    # Cette chaîne est ajoutée à la liste 'ans' pour être affichée après toutes les entrées.
    ans.append("%d %d" % (a, b))

# Affichage final de toutes les réponses collectées.
# '*ans' décompose la liste pour afficher chaque élément séparément.
# 'sep='\n'' garantit que chaque élément sera affiché sur une nouvelle ligne.
print(*ans, sep='\n')