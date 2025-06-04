# On crée un dictionnaire vide nommé 'dic', qui contiendra des clés correspondant à chaque lettre minuscule de l'alphabet anglais (de 'a' à 'z'), et chaque clé aura une liste associée.
dic = {}

# Cette boucle externe va itérer sur les codes ASCII des lettres minuscules de 'a' à 'z'.
# La fonction ord() convertit une lettre en son code ASCII entier.
# range(ord("a"), ord("z") + 1) génère tous les entiers de 97 (inclus) à 122 (inclus), qui correspondent à 'a'-'z'.
for num1 in range(ord("a"), ord("z") + 1):

    # chr() convertit un code ASCII (nombre entier) en son caractère correspondant. 
    # Ici, on récupère la lettre correspondant à num1 (par exemple, 97 devient 'a', 98 devient 'b', etc.)
    c1 = chr(num1)

    # On initialise la valeur correspondant à la clé c1 avec une liste vide.
    # Cette liste va contenir toutes les chaînes générées par les boucles imbriquées suivantes.
    dic[c1] = []

    # Deuxième boucle : encore sur tous les caractères de 'a' à 'z'.
    for num2 in range(ord("a"), ord("z") + 1):
        # On obtient le caractère correspondant à num2.
        c2 = chr(num2)

        # Troisième boucle : encore de 'a' à 'z'.
        for num3 in range(ord("a"), ord("z") + 1):
            # On obtient le caractère correspondant à num3.
            c3 = chr(num3)

            # On construit une chaîne composée de c1, c2, c3, et la lettre 'a' (par exemple : 'aaaa', 'aaba', etc.).
            # On ajoute cette chaîne à la liste dic[c1].
            dic[c1].append(c1 + c2 + c3 + "a")

# Après la génération du dictionnaire, on commence la partie interactive du code.

# dic["a"].pop() va retirer (et retourner) le dernier élément de la liste correspondant à la clé 'a'.
# On concatène un point d'interrogation "?" devant la chaîne et on l'affiche à l'écran.
print("?" + dic["a"].pop())

# On crée un ensemble vide nommé 'used' pour garder en mémoire toutes les chaînes saisies qui ont déjà été utilisées.
# Les ensembles (set) en Python ne contiennent pas de doublons et permettent des recherches rapides.
used = set()

# On commence une boucle infinie qui ne sera arrêtée que par le mot-clé 'break'.
while True:

    # La fonction input() met le programme en pause et attend que l'utilisateur saisisse une ligne de texte
    # qui sera stockée sous forme de chaîne dans la variable 's'.
    s = input()

    # On vérifie deux conditions pour décider si on arrête la boucle :
    # 1. Si s est déjà dans l'ensemble 'used' (la chaîne a déjà été saisie)
    # 2. Si le premier caractère de s (s[0]) n'est PAS égal à "a".
    if s in used or s[0] != "a":
        # Si une des conditions est vraie, on affiche "!OUT" puis on sort de la boucle avec 'break'
        print("!OUT")
        break

    # Si ni l'une ni l'autre des conditions n'est remplie,
    # On ajoute la chaîne saisie 's' à l'ensemble 'used' pour garder une trace qu'elle a déjà été vue.
    used.add(s)

    # On prend le dernier caractère de la chaîne saisie avec 's[-1]'
    # Puis, on prend la liste correspondant à cette lettre dans 'dic'
    # Ensuite, on retire (pop()) le dernier élément de cette liste (une chaîne générée plus tôt)
    # On ajoute un "?" devant cette chaîne, puis on l'affiche.
    print("?" + dic[s[-1]].pop())