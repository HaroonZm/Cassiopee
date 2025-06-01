# Initialisation d'une variable booléenne nommée 'flag' à False.
# Cette variable sert généralement à contrôler un comportement conditionnel, ici pour gérer l'affichage d'une ligne vide entre les résultats.
flag = False

# Début d'une boucle infinie. Cette boucle va continuer indéfiniment jusqu'à ce qu'une instruction 'break' soit rencontrée.
while True:
    # Lecture d'une ligne d'entrée utilisateur avec raw_input(), qui retourne une chaîne de caractères.
    # La méthode split() découpe cette chaîne selon les espaces en une liste de chaînes.
    # La fonction map applique la fonction int à chaque élément de cette liste pour convertir ces chaînes en entiers.
    # Le résultat est décompressé en deux variables a et b.
    a, b = map(int, raw_input().split())

    # Condition de terminaison de la boucle.
    # Si le tuple (a, b) est égal à (0, 0), cela signifie que l'utilisateur a entré les deux zéros.
    # On exécute alors un 'break' pour sortir immédiatement de la boucle infinie.
    if (a, b) == (0, 0):
        break

    # Si flag est False (ce qui arrive au premier tour de boucle), on le passe à True.
    # Sinon, si flag est déjà True (c'est-à-dire pas la première itération), on imprime une ligne vide.
    # Ce mécanisme sert à séparer visuellement les sorties des différentes itérations par une ligne vide.
    if not flag:
        flag = True
    else:
        print  # Impression d'une ligne vide (print sans argument imprime un saut de ligne)

    # Création d'une liste nommée 'ans' contenant tous les entiers y dans l'intervalle [a, b], c'est-à-dire de a à b inclus.
    # La fonction xrange est utilisée pour générer cette séquence efficace en mémoire (fonctionne comme range mais en version générateur).
    # Pour chaque y, on vérifie si y est une année bissextile selon la règle suivante:
    # - y divisible par 4 ET non divisible par 100 (donc y%4==0 and not y%100==0)
    # OU
    # - y divisible par 400 (y%400==0)
    # Seules les années respectant cette condition seront incluses dans la liste ans.
    ans = [y for y in xrange(a, b + 1) if (y % 4 == 0 and not y % 100 == 0) or y % 400 == 0]

    # Vérification si la liste ans est vide, c'est-à-dire qu'aucune année bissextile n'a été trouvée dans l'intervalle.
    if not ans:
        # Impression de "NA" pour indiquer qu'il n'existe aucune année bissextile dans l'intervalle fourni.
        print "NA"
    else:
        # Sinon, on imprime chaque année bissextile trouvée, chacune sur une ligne séparée.
        # map(str, ans) convertit chaque entier en chaîne de caractères pour pouvoir les afficher.
        # '\n'.join(...) crée une seule chaîne avec les années séparées par un saut de ligne.
        # print affiche cette chaîne, donc chaque année sur une ligne distincte.
        print "\n".join(map(str, ans))