# Initialisation d'une liste vide nommée 'lst'
# Une liste en Python est une collection ordonnée et modifiable d'éléments.
lst = []

# Utilisation d'une boucle for pour répéter une action 5 fois
# 'range(5)' génère une séquence de nombres de 0 à 4 inclus, donc 5 répétitions
for i in range(5):
    # Demande à l'utilisateur d'entrer une valeur via le clavier
    # input() renvoie une chaîne de caractères, donc on la convertit en entier avec int()
    a = int(input())
    
    # Condition pour vérifier si la valeur entrée est inférieure à 40
    # Si c'est le cas, on remplace la valeur par 40
    # L'opérateur '<' compare deux nombres pour vérifier si le premier est strictement plus petit que le second
    if a < 40:
        a = 40
        
    # Ajoute la valeur déterminée (entrée ou ajustée) à la fin de la liste lst
    # append() est une méthode qui ajoute un élément à une liste existante
    lst.append(a)
    
# Calcul de la moyenne des valeurs stockées dans la liste lst
# sum(lst) calcule la somme de tous les éléments de la liste
# len(lst) retourne le nombre total d'éléments dans la liste
# La division entière '//' est utilisée pour obtenir un résultat entier sans partie décimale
moyenne = sum(lst) // len(lst)

# Affiche le résultat calculé à l'écran
print(moyenne)