# Demander à l'utilisateur de saisir des valeurs. La fonction input() lit une ligne de texte saisie.
# split() divise cette ligne en une liste de sous-chaînes en utilisant l'espace comme séparateur, par défaut.
# La fonction map() applique la fonction int à chaque élément de cette liste pour les convertir en entiers.
# Ces trois entiers sont ensuite assignés respectivement aux variables a, b et c grâce à l'affectation multiple.
a, b, c = map(int, input().split())

# Initialisation d'une variable x à 0.
# Cette variable va servir de compteur pour compter combien d'entiers i dans l'intervalle [a, b] divisent c sans reste.
x = 0

# Boucle for qui va permettre d'itérer sur les entiers de a jusqu'à b inclus.
# range(a, b+1) génère une séquence d'entiers commençant à a et se terminant à b inclus (car le 2ème argument de range est exclusif donc on met b+1).
for i in range(a, b+1):
    # À chaque itération, on vérifie si c est divisible par i sans reste.
    # L'opérateur modulo % donne le reste de la division entière de c par i.
    # Si le reste est égal à 0, cela signifie que i divise exactement c.
    if c % i == 0:
        # Si la condition est vraie, on incrémente le compteur x de 1.
        x += 1

# Après la sortie de la boucle, toutes les vérifications sont terminées.
# On affiche la valeur finale de x avec la fonction print(), qui envoie la variable x sur la sortie standard.
print(x)