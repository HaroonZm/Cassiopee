# Demande à l'utilisateur d'entrer un nombre entier, qui sera stocké dans la variable N.
# La fonction int() convertit la chaîne de caractères saisie par l'utilisateur en un nombre entier.
N = int(input())

# Demande à l'utilisateur une ligne d'entiers séparés par des espaces.
# input() lit la saisie utilisateur (une chaîne).
# split() découpe la chaîne sur les espaces pour en faire une liste de chaînes représentant des nombres.
# map(int, ...) convertit chaque élément de cette liste en entier.
# list(...) convertit l'objet map en une liste d'entiers, assignée à la variable a.
a = list(map(int, input().split()))

# Initialise une variable ans à 0.
# Cette variable servira à comptabiliser la réponse finale (somme totale).
ans = 0

# Utilise une boucle while infinie qui ne s'arrêtera qu'avec un break explicite.
while True:
    # Crée une nouvelle liste appelée sub, initialisée à des zéros, de taille N.
    # sub[i] sera utilisé plus tard pour stocker un certain calcul basé sur a[i].
    sub = [0] * N
    
    # Parcourt chaque élément de a, à l'aide d'une boucle for basée sur les indices de 0 à N-1.
    for i in range(N):
        # Calcule une certaine valeur basée sur a[i], N, et l'index.
        # (N-1) est soustrait de a[i], puis encore 1.
        # On effectue une division entière "//" sur N.
        # +1 sert à ajuster le résultat, surtout utile pour gérer les cas où a[i] < N-1.
        # La formule :
        #   (a[i] - (N - 1) - 1) // N + 1
        # revient à calculer combien de fois on peut retirer N de a[i] 
        # après avoir 'décalé' de N-1+1 unités.
        # Cette écriture garantit que sub[i] est 0 si a[i] < N, et positif sinon.
        sub[i] = (a[i] - (N - 1) - 1) // N + 1
    
    # Calcule la somme de tous les éléments de la liste sub, stockée dans sum_sub.
    # sum() additionne tous les éléments de la liste sub.
    sum_sub = sum(sub)
    
    # Si la somme sum_sub est 0, cela signifie que pour tous les éléments de sub, la valeur est 0.
    # Autrement dit, aucune modification supplémentaire ne doit être effectuée (condition d'arrêt),
    # donc on quitte la boucle avec break.
    if sum_sub == 0:
        break
    
    # Ajoute la valeur de sum_sub à la variable ans.
    # Cela accumule le nombre total de modifications apportées jusque-là.
    ans += sum_sub
    
    # Met à jour chaque élément de a en fonction de la logique du problème.
    # Pour chaque index i de 0 à N-1 :
    for i in range(N):
        # On modifie a[i] en retirant N*sub[i] (le nombre total retiré pour cet élément),
        # mais on ajoute (sum_sub - sub[i]).
        # Cela semble compenser ou redistribuer le 'surplus' pour s'assurer que la totalité 
        # du lot retiré (sum_sub*N) est justement répartie, sauf pour la propre part déjà retirée (sub[i]).
        a[i] -= N * sub[i] - (sum_sub - sub[i])

# À la sortie de la boucle, on affiche la valeur finale calculée dans ans.
# print() permet d'afficher la réponse à l'écran.
print(ans)