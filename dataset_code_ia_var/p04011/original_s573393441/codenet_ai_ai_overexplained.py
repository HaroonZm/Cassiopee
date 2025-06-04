# Demande à l'utilisateur d'entrer une valeur entière et la stocke dans la variable n
# La fonction input() attend que l'utilisateur saisisse une entrée via le clavier
# int() convertit cette entrée, initialement une chaîne de caractères (string), en un entier (integer)
n = int(input())

# Demande à l'utilisateur d'entrer une valeur entière et la stocke dans la variable k
k = int(input())

# Demande à l'utilisateur d'entrer une valeur entière et la stocke dans la variable x
x = int(input())

# Demande à l'utilisateur d'entrer une valeur entière et la stocke dans la variable y
y = int(input())

# Calcule le minimum entre les variables n et k en utilisant la fonction min()
# La fonction min(a, b) retourne la plus petite valeur parmi les arguments a et b
# Multiplie le minimum trouvé par la variable x
min_n_k = min(n, k)  # min(n, k) donne la plus petite valeur entre n et k
first_part = min_n_k * x  # Multiplie ce minimum par x

# Calcule la différence n - k. Si cette différence est négative, max() remplacera par 0 pour éviter d'avoir un nombre négatif
# max(a, b) retourne la plus grande valeur entre a et b, donc si n - k < 0, max(n - k, 0) retourne 0
remaining = max(n - k, 0)  # nombre d'unités restantes après avoir pris min(n, k)
second_part = remaining * y  # Multiplie cette valeur par y

# Additionne les deux parties calculées précédemment: first_part + second_part
total_cost = first_part + second_part  # Somme totale

# Affiche la valeur totale calculée à l'écran
# La fonction print() permet d'afficher des informations à l'utilisateur
print(total_cost)