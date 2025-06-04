# Demande à l'utilisateur d'entrer une valeur à l'aide de la fonction input().
# input() retourne une chaîne de caractères (str). On utilise donc int() pour convertir la chaîne en un entier (integer).
x = int(input())

# La variable 'ans' représente la réponse finale qui sera calculée.
# On commence par effectuer une division entière (c'est-à-dire sans reste) de x par 11. En Python, l'opérateur '//' réalise la division entière.
# Cette division donne le nombre maximum de groupes entiers de 11 dans x.
# On multiplie ce résultat par 2 car chaque groupe complet de 11 nécessite exactement 2 unités de 'réponse'.
ans = x // 11 * 2

# Maintenant, on met à jour la valeur de x pour qu'elle ne représente plus que le reste (modulo 11) qui n'a pas été pris en compte dans le calcul précédent.
# L'opérateur '%' donne le reste de la division entière de x par 11.
x %= 11

# Maintenant, nous examinons ce qu'il reste dans x après avoir retiré tous les groupes de 11.
# Si ce reste (x) est supérieur à 0 ET inférieur à 7 (donc dans l'intervalle [1, 6]), alors il nous faut exactement 1 unité de réponse supplémentaire pour le traiter.
if x > 0 and x < 7:
    ans += 1  # On ajoute 1 à ans car une unité supplémentaire est nécessaire.

# Si le reste (x) est supérieur à 6 (c'est-à-dire x vaut 7, 8, 9 ou 10), il nous faut alors 2 unités de réponse supplémentaires.
if x > 6:
    ans += 2  # On ajoute 2 à ans car deux unités supplémentaires sont nécessaires.

# Enfin, on affiche la réponse finale en utilisant print().
# print() convertit automatiquement ans (qui est un nombre entier) en chaîne de caractères et l'affiche à l'écran.
print(ans)