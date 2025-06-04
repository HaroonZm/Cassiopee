# Lecture des 5 entiers séparés par des espaces depuis l'entrée standard
# On utilise la fonction input() pour lire une ligne de texte de l'utilisateur
# Ensuite, on découpe cette ligne en morceaux grâce à split(), qui par défaut coupe sur les espaces
# La fonction map(int, ...) applique la fonction int à chaque élément résultant du découpage pour tout convertir en entiers
A, B, C, X, Y = map(int, input().split())

# Initialisation d'une variable pour stocker la valeur minimale trouvée
# float('INF') crée un objet flottant représentant l’infini, utilisé comme valeur initiale
ans = float('INF')

# La variable k va représenter le nombre de "couples" d'éléments spéciaux impactant le coût
# On doit tester tous les k pairs de 0 jusqu'à 2*max(X, Y), inclus, avec un pas de 2
# Le choix de 2*max(X, Y) permet de couvrir tous les cas possibles où on achète assez de couples pour couvrir soit X soit Y, dans le pire des cas
for k in range(0, 2*max(X, Y)+1, 2):

    # Calcul du nombre d'éléments de type A qu'il reste à acheter sans passer par des couples
    # k/2 est le nombre de couples achetés (car chaque couple contribue à 1 unité de chaque type)
    # int(k/2) convertit la division en entier et garantit que le résultat est bien un nombre entier
    # X - int(k/2) donne combien il reste à acheter "en plus" pour satisfaire X après avoir couvert une partie par les couples
    # max(0, ...) empêche que cette quantité ne soit négative (on ne peut pas acheter un nombre négatif d'objets)
    i = max(0, X - int(k/2))
    
    # Même calcul pour le nombre d'éléments de type B à acheter en plus
    j = max(0, Y - int(k/2))
    
    # Calcul du coût total pour ce choix particulier de k
    # A * i : coût des éléments de type A restants
    # B * j : coût des éléments de type B restants
    # C * k : coût de tous les couples achetés
    total_cost = A * i + B * j + C * k
    
    # Mise à jour du minimum global
    # min(ans, total_cost) prend la plus petite valeur entre la précédente et la nouvelle trouvée
    ans = min(ans, total_cost)

# Affichage du coût minimal trouvé
# print() permet d’afficher une valeur à l’écran (ici, la réponse finale)
print(ans)