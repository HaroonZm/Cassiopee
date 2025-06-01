from collections import defaultdict

# Définition d'une constante nommée MOD à la valeur 1 000 000 007.
# Cette constante est souvent utilisée dans les problèmes d'informatique
# compétitive pour effectuer des opérations modulo afin d'éviter 
# des débordements d'entiers et pour garder les nombres dans une plage gérable.
MOD = 1000000007

# Lecture d'une entrée utilisateur qui sera convertie en entier.
# Cette entrée correspond à un nombre n, qui sera utilisé pour déterminer
# la taille des chaînes qui vont suivre ainsi que la plage à parcourir.
n = int(input())

# Lecture d'une chaîne de caractères depuis l'entrée standard.
# Cette chaîne est stockée dans la variable s.
s = input()

# Lecture d'une deuxième chaîne de caractères depuis l'entrée standard.
# Cette chaîne est stockée dans la variable t.
t = input()

# Création d'un dictionnaire spécial nommé dic où chaque clé aura une valeur entière par défaut 0.
# defaultdict est un type de dictionnaire fourni par la bibliothèque collections de Python.
# Si une clé n'existe pas dans ce dictionnaire, sa valeur par défaut sera automatiquement 0 (int()).
dic = defaultdict(int)

# Initialisation de la valeur associée à la clé correspondant au premier caractère de la chaîne s.
# Cette valeur est mise à 1, ce qui signifie que l'on commence à compter à partir de ce caractère.
dic[s[0]] = 1

# Boucle for qui parcourt simultanément les caractères des deux chaînes s et t.
# zip(s[1:n-1], t[1:n-1]) crée un itérateur qui va produire des paires de caractères
# où la première provient de s et la deuxième de t.
# Les indices vont de 1 inclus à n-1 exclus, ce qui signifie que le dernier caractère n'est pas inclus dans la boucle.
for cs, ct in zip(s[1:n-1], t[1:n-1]):
    # Pour chaque paire de caractères (cs venant de s, ct venant de t),
    # on ajoute la valeur associée à la clé ct dans le dictionnaire dic à la valeur associée à la clé cs.
    dic[cs] += dic[ct]

    # Puis on applique l'opération modulo MOD sur la nouvelle valeur de dic[cs].
    # Cela garantit que la valeur reste dans la plage [0, MOD-1], évitant les débordements.
    dic[cs] %= MOD

# Enfin, on affiche la valeur associée dans le dictionnaire à la clé correspondant
# au dernier caractère de la chaîne t.
# Cette valeur a été mise à jour dans la boucle précédente et représente le résultat final calculé.
print(dic[t[-1]])