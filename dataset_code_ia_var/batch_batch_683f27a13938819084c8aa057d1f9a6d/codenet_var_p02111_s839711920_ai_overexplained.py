# Demande à l'utilisateur d'entrer une valeur au clavier avec la fonction input().
# Cette fonction renvoie une chaîne de caractères (str), par exemple : '5' si l'utilisateur écrit 5.
# On convertit ensuite cette chaîne de caractères en entier grâce à la fonction int().
# L'entier résultant est stocké dans la variable 'n'.
n = int(input())

# Multiplie la variable 'n' par 2 (c'est-à-dire calcule 2*n), puis effectue une division entière (//) par 60.
# L'opérateur // donne le quotient sans les décimales. Par exemple, 125//60 vaut 2 car 60 entre 2 fois dans 125.
# Ceci permet de savoir combien de fois 60 rentre dans 2*n.
# On convertit le résultat du calcul en chaîne de caractères str pour pouvoir l'afficher.
part1 = str(2 * n // 60)

# Calcule le reste de la division de 2*n par 60 avec l'opérateur modulo (%).
# Par exemple, 125 % 60 donne 5, car 60*2=120 et 125-120=5.
# Cela donne le nombre de minutes ou de secondes "restantes" après avoir retiré tous les groupes de 60.
# On convertit ce reste en chaîne de caractères pour l'afficher.
part2 = str((2 * n) % 60)

# Concatène la première partie (le nombre de groupes de 60), un espace (qui sépare les deux valeurs), puis la seconde partie.
# Le signe + sert ici à joindre les chaînes de caractères.
# Le résultat final sera par exemple '2 5' si part1 vaut '2' et part2 vaut '5'.
to_print = part1 + " " + part2

# Affiche la chaîne résultante à l'écran à l'aide de la fonction print().
# print() affiche ce qu'on lui donne (ici, la chaîne to_print) suivi d'un retour à la ligne.
print(to_print)