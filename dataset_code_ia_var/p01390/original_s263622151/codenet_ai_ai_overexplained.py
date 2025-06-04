# Afficher à l'utilisateur le texte "?za" pour commencer. 
# Le point d'interrogation "?" est probablement utilisé comme préfixe de commande ou d'invitation.
print("?za")

# Crée une liste appelée 'use' contenant la chaîne "za". 
# Cette liste servira à mémoriser toutes les chaînes déjà utilisées.
use = ["za"]

# Crée une liste appelée 'can' (abréviation probable de "candidates"), qui va contenir des chaînes de caractères générées pour une utilisation ultérieure.

# Première partie de la liste 'can' : une compréhension de liste génère des caractères de code ASCII allant de 98 ('b') à 98+24 (c'est-à-dire 122, soit 'z').
# La fonction 'chr(i)' convertit le code numérique ASCII 'i' en caractère.
# 'range(98, 98+24)' génère les entiers de 98 à 121 inclus, ce qui correspond à 'b' à 'y'.
can = [chr(i) for i in range(98, 98+24)]

# Deuxième partie de la liste 'can' : concatène à la suite de la première partie de nouvelles chaînes.
# Pour chaque entier de 97 ('a') à 122 ('z') inclus, construit une chaîne de caractères composée de la lettre 'a' suivie du caractère correspondant à 'i' (soit "aa", "ab", ..., "az").
# 'extend' ajoute chaque élément généré à la fin de la liste 'can'.
can.extend(["a"+chr(i) for i in range(97, 97+26)])

# Boucle infinie : ceci garantit que le code à l'intérieur du bloc 'while' continuera à s'exécuter tant que rien ne vient briser la boucle (break).
while 1:
    # Demande à l'utilisateur d'entrer une chaîne qui sera stockée dans la variable 's'.
    s = input()

    # Si le premier caractère de la chaîne 's' n'est pas 'a', OU si 's' se trouve déjà dans la liste 'use'
    # (c'est-à-dire si l'entrée de l'utilisateur ne commence pas par 'a' ou a déjà été utilisée précédemment) :
    if s[0] != "a" or s in use:
        # Affiche "!OUT" -- peut indiquer une erreur ou signifier la fin du programme
        print("!OUT")
        # Interrompt la boucle infinie et termine le programme
        break

    # Si l'entrée utilisateur est valide, ajoute 's' à la liste 'use' pour éviter une utilisation future répétée.
    use.append(s)

    # Déterminer la prochaine chaîne à utiliser : 
    # Si l'utilisateur a entré "a" exactement (c'est-à-dire la chaîne d'un seul caractère "a"), alors :
    if s == "a":
        # La prochaine chaîne à proposer sera "aa"
        p = "aa"
    # Sinon, si l'utilisateur a entré "aa" exactement, alors :
    elif s == "aa":
        # La prochaine chaîne à proposer sera "a"
        p = "a"
    # Pour tous les autres cas (i.e. s n'est ni "a" ni "aa") :
    else:
        # 's[-1]' prend le dernier caractère de la chaîne 's'.
        # 'can.pop(0)' enlève et retourne le premier élément de la liste 'can'.
        # On construit une nouvelle chaîne constituée du dernier caractère de 's', suivi de la première chaîne de 'can', puis suivi de "a".
        p = s[-1] + can.pop(0) + "a"

    # Affiche à l'utilisateur la chaîne à suggérer, avec un préfixe "?"
    print("?" + p)

    # Ajoute la chaîne proposée 'p' à la liste 'use' pour qu'elle ne puisse être réutilisée ni par erreur ni dupliquée.
    use.append(p)