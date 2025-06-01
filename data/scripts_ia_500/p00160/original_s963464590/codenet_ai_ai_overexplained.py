def process(x, y, h, w):
    # Définition d'une fonction nommée 'process' qui prend quatre paramètres entiers : x, y, h et w.
    # Cette fonction calcule une valeur basée sur certaines conditions impliquant la somme de x, y et h, ainsi que la valeur de w.

    # On commence par vérifier la première condition avec un 'if' :
    # Si la somme de x, y et h est inférieure ou égale à 60 (<= 60)
    # ET (and) w est inférieur ou égal à 2 (<= 2),
    # alors la fonction retourne la valeur 600.
    if x + y + h <= 60 and w <= 2:
        return 600

    # 'elif' signifie "else if", on teste une autre condition si la première n'était pas vraie.
    # Ici, si la somme x+y+h est <= 80 ET w <= 5, alors on retourne 800.
    elif x + y + h <= 80 and w <= 5:
        return 800

    # Nouvelle condition : si somme x+y+h <= 100 ET w <= 10, retourner 1000.
    elif x + y + h <= 100 and w <= 10:
        return 1000

    # Si aucun des précédents tests n'a réussi, on teste si somme x+y+h <= 120 ET w <= 15, on retourne 1200.
    elif x + y + h <= 120 and w <= 15:
        return 1200

    # Si toujours aucune condition n'est remplie, on teste somme x+y+h <= 140 ET w <= 20, on retourne 1400.
    elif x + y + h <= 140 and w <= 20:
        return 1400

    # On teste une dernière condition : somme x+y+h <= 160 ET w <= 25, alors retourne 1600.
    elif x + y + h <= 160 and w <= 25:
        return 1600

    # Si aucune des conditions précédentes n'est remplie, on exécute le bloc 'else'
    # qui retourne la valeur 0.
    else:
        return 0

# On crée une liste vide nommée 'result' qui servira à stocker plusieurs résultats numériques.
result = []

# Démarrage d'une boucle infinie, qui va tourner en continu jusqu'à ce qu'on rencontre une instruction 'break'.
while True:
    # Attente d'une entrée utilisateur sous forme de chaîne de caractères obtenue via input().
    # On convertit cette chaîne en entier avec int() et on la stocke dans la variable 'n'.
    n = int(input())

    # Si la variable 'n' est égale à 0, on interrompt la boucle avec 'break'.
    # Cela sert de condition d'arrêt à la lecture des données.
    if n == 0:
        break

    # Initialisation d'une variable 'total' à 0 pour cumuler des résultats.
    total = 0

    # On lance une boucle 'for' qui s'exécutera 'n' fois.
    # Le '_' est une variable conventionnellement utilisée lorsque la variable de boucle n'est pas nécessaire.
    for _ in range(n):
        # On lit une ligne utilisateur contenant quatre entiers séparés par des espaces.
        # input().split() divise la chaîne en une liste de chaînes.
        # map(int, ...) convertit chaque élément de cette liste en entier.
        # L'affectation multiple stocke ces quatre entiers dans x, y, h, et w respectivement.
        x, y, h, w = map(int, input().split())

        # On appelle la fonction 'process' avec ces quatre paramètres.
        # Le résultat retourné (un entier) est ajouté à la variable 'total' avec '+='.
        total += process(x, y, h, w)

    # Après la lecture et le traitement des 'n' lignes, on ajoute la valeur totale calculée à la liste 'result'.
    result.append(total)

# Une fois la boucle principale terminée (après avoir rencontré un 0),
# on convertit chaque entier contenu dans la liste 'result' en chaîne avec map(str, result).
# '\n'.join(...) crée une unique chaîne de caractères où chaque élément de la liste est séparé par un saut de ligne.
# Enfin, print affiche cette chaîne, ce qui produit une sortie ligne par ligne des totaux calculés.
print('\n'.join(map(str, result)))