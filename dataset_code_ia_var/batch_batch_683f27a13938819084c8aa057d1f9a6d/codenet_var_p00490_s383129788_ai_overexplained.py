# Demande à l'utilisateur d'entrer un entier indiquant le nombre de garnitures disponibles pour la pizza.
n = int(input())  # Stocke la valeur entrée sous forme d'entier dans la variable n

# Demande à l'utilisateur d'entrer deux entiers séparés par un espace :
# 'a' représente le prix de la pâte à pizza de base, 
# 'b' représente le prix supplémentaire pour chaque garniture ajoutée.
a, b = map(int, input().split())  # Transforme les deux éléments de l'entrée en entiers, et les assigne à 'a' et 'b'

# Demande à l'utilisateur d'entrer un entier correspondant au nombre de calories de la pâte à pizza de base sans garniture
c = int(input())  # Stocke la valeur entière dans la variable 'c'

# Initialise 'ans' avec le meilleur ratio de calories/prix trouvé jusque-là :
# calcule initialement le ratio uniquement avec la pâte à pizza de base (c / a).
ans = c / a  # 'ans' va contenir la meilleure valeur de calories par unité de monnaie trouvée.
p = a  # 'p' représente le prix total actuel de la pizza, commence avec le prix de la pâte de base

# Crée une liste contenant les calories de chaque garniture possible :
# pour chaque garniture (il y en a 'n'), on lit une valeur entière depuis l'entrée.
d = [int(input()) for i in range(n)]  # Liste des apports caloriques des différentes garnitures

# Trie la liste des calories des garnitures dans l'ordre décroissant (plus grandi au début),
# pour maximiser l'apport calorique lors de l'ajout de chaque garniture.
d.sort(reverse=True)

# Parcourt toutes les garnitures dans l'ordre (du plus calorique au moins calorique)
for i in range(n):
    # Calcule le nouveau ratio de calories/prix si on rajoute la i-ème garniture à la pizza :
    # On additionne les calories de la garniture à 'c', et le prix de la garniture à 'p'
    t = (c + d[i]) / (p + b)
    
    # Vérifie si ce nouveau ratio (t) est supérieur à la meilleure valeur trouvée jusque-là ('ans').
    if t > ans:
        ans = t  # Met à jour la meilleure valeur trouvée si le ratio s'améliore
        c += d[i]  # Ajoute les calories de cette garniture à la somme totale de calories
        p += b     # Ajoute le prix de cette garniture au prix total
    else:
        # Si ajouter une garniture ne permet plus d'améliorer le ratio,
        # alors arrêter l'ajout de garnitures supplémentaires.
        break

# Convertit la meilleure valeur de ratio calories/prix ('ans') en entier (en ignorant la partie décimale),
# puis affiche ce résultat à l'utilisateur.
print(int(ans))  # Affiche le résultat final (partie entière du meilleur ratio obtenu)