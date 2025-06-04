# Définition d'une liste contenant toutes les lettres minuscules de l'alphabet anglais, chacune représentée par une chaîne de caractères d'un seul caractère.
# Cette liste sera utilisée pour faire la correspondance entre les lettres et leurs indices numériques allant de 0 pour 'a' à 25 pour 'z'.
dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",\
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Définition d'une liste appelée lsalpha qui contient certains nombres impairs entre 1 et 25.
# Ces valeurs sont précalculées et sont toutes des entiers impairs inférieurs à 26.
# Ces nombres servent d'éventuelles valeurs pour le paramètre 'alpha' lors de la décryption.
lsalpha = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

# Définition d'une fonction nommée 'decode' qui prend trois arguments :
#   - alpha : un entier utilisé dans la formule d'encodage affine
#   - beta : un entier qui est l'autre paramètre de la fonction affine
#   - code : une chaîne de caractères représentant le texte chiffré à décoder
def decode(alpha, beta, code):
    # Initialisation d'une chaîne vide qui servira à stocker le message décodé au fur et à mesure.
    msg = ""
    # Parcours de chaque caractère (chara) du texte chiffré fourni dans 'code'.
    for chara in code:
        # Vérification si le caractère courant n'est pas un espace.
        if chara != " ":
            # Recherche de la position (index) du caractère dans la liste dict.
            # Cela permet d'obtenir la valeur numérique associée à la lettre.
            f = dict.index(chara)
            # Parcours de tous les entiers i de 0 à 25 inclus.
            for i in range(26):
                # Application de la formule de chiffrement affine inversée :
                # Pour chaque valeur de i, on calcule (alpha*i + beta) modulo 26,
                # et on vérifie si le résultat est égal à la valeur 'f' trouvée précédemment.
                if (alpha * i + beta) % 26 == f:
                    # Si c'est le cas, cela signifie que l'indice décrypté est i,
                    # on retrouve alors la lettre correspondant à i dans dict.
                    dechara = dict[i]
                    # On quitte la boucle car on n'a plus besoin de vérifier d'autres valeurs de i.
                    break
            # On ajoute la lettre déchiffrée au message en cours de reconstruction.
            msg += dechara
        else:
            # Si le caractère dans le texte chiffré est un espace,
            # on ajoute un espace à la construction du message déchiffré pour préserver la structure du texte.
            msg += " "
    # À la fin de la fonction, on retourne la chaîne représentant le message déchiffré.
    return msg

# Lecture d'un entier depuis l'entrée standard.
# Cela permet de savoir combien de fois on devra répéter la suite du code (donc combien de messages chiffrés à traiter).
# La conversion en entier est nécessaire car la fonction raw_input retourne une chaîne de caractères.
n = int(raw_input())

# Boucle principale qui va itérer 'n' fois, chacune correspondant à un message chiffré à traiter.
for roop in range(n):
    # Lecture du texte chiffré depuis l'entrée standard.
    # Cela récupère une ligne saisie par l'utilisateur et la stocke dans la variable 'code'.
    code = raw_input()
    # Boucle qui parcourt toutes les valeurs possibles d'alpha définies dans la liste lsalpha.
    for alpha in lsalpha:
        # Initialisation d'un indicateur (flag) à 0.
        # Cette variable servira à savoir si un résultat satisfaisant a été trouvé.
        flag = 0
        # Boucle imbriquée qui va essayer toutes les valeurs possibles de beta de 0 à 25 inclus.
        for beta in range(26):
            # Appel de la fonction decode avec les valeurs courantes de alpha, beta,
            # et la chaîne de caractères chiffrée 'code'. Le résultat est stocké dans 'msg'.
            msg = decode(alpha, beta, code)
            # Vérification si le message décrypté contient le mot "that" ou le mot "this".
            # Cela se fait en comptant le nombre d'occurrences de l'un ou l'autre dans la chaîne.
            if msg.count("that") > 0 or msg.count("this") > 0:
                # Si au moins une des deux chaînes est trouvée, cela signifie probablement que la décryption est correcte.
                # On marque donc flag à 1 pour signaler qu'on a trouvé une décryption valide.
                flag = 1
                # On arrête la recherche des autres valeurs de beta pour cet alpha.
                break
        # Si l'indicateur flag est passé à 1, cela signifie qu'on a trouvé un chiffrement valide,
        # et on arrête de chercher d'autres valeurs de alpha.
        if flag == 1:
            break
    # On affiche finalement le message décodé trouvé, que ce soit après la recherche exhaustive ou à la première solution.
    print msg