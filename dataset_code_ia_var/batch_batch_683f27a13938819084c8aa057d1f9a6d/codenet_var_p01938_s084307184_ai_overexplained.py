# Demande à l'utilisateur d'entrer une chaîne de caractères via le clavier.
# La fonction input() affiche un invite (vide ici) et attend que l'utilisateur tape une entrée, terminée par 'Entrée'.
# Le résultat, une chaîne de caractères, est stocké dans la variable S.
S = input()

# Définition d'une chaîne contenant toutes les lettres majuscules de l'alphabet anglais, dans l'ordre.
# Cette chaîne sera utilisée pour déterminer la position (l'indice) d'une lettre spécifiée dans l'alphabet.
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Création et initialisation d'une variable appelée 'Now' avec la valeur 0.
# Cette variable va enregistrer la position (indice) dans l'alphabet de la lettre précédente du mot.
# On commence à 0, ce qui correspond à la première lettre de l'alphabet ('A') selon notre variable alpha.
Now = 0

# Création et initialisation d'une variable appelée 'ans' à 0.
# Cette variable servira à compter ou à accumuler le nombre d'occurrences selon la condition précisée dans la boucle suivante.
ans = 0

# Démarrage d'une boucle for. Elle va parcourir chaque caractère (lettre) de la chaîne S, un par un.
# À chaque itération, la lettre en cours est stockée dans la variable 's'.
for s in S:
    # Pour le caractère courant 's', on cherche son indice (position) dans la chaîne 'alpha'.
    # La méthode find() renvoie l'indice de la première occurrence de 's' dans 'alpha'.
    # Si 's' est 'A', alors Next vaut 0 ; si 's' est 'B', Next vaut 1 ; etc.
    # Le résultat est stocké dans la variable 'Next'.
    Next = alpha.find(s)

    # L'instruction suivante a été commentée, elle aurait affiché ('print') la lettre actuelle, la variable Now et Next.
    # Cela aurait pu servir au débogage pour comprendre l'évolution des variables lors de l'exécution du programme.
    # print(s, Now, Next)

    # Test conditionnel pour savoir si la position précédente (Now) est inférieure à la position actuelle (Next).
    # Si 'Now < Next', cela signifie que l'on avance dans l'ordre alphabétique.
    if(Now < Next):
        # Si l'on avance dans l'ordre alphabétique, selon le programme d'origine, on ne fait rien ici (pass).
        # Le mot-clé pass indique que ce bloc d'instructions est intentionnellement laissé vide et ne fait rien.
        pass
    else:
        # Si l'on n'avance pas, c'est-à-dire que 'Now' est supérieur ou égal à 'Next',
        # cela signifie que la lettre actuelle est la même ou revient en arrière dans l'ordre alphabétique.
        # Dans ce cas, on incrémente la variable 'ans' de 1. Cela compte le nombre de "retours" ou "non-avancées".
        ans += 1
    # À la fin de chaque itération, on met à jour la variable 'Now' pour qu'elle prenne la valeur 'Next'.
    # Ainsi, à la prochaine lettre, 'Now' contiendra la position de la lettre précédente.
    Now = Next

# Après que la boucle a parcouru l'intégralité de la chaîne S, on affiche la valeur de 'ans' à l'écran.
# Cela représente le nombre total de fois où on a "recommencé" ou "retourné en arrière" dans l'ordre alphabétique.
print(ans)