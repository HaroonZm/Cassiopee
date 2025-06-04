# Demande à l'utilisateur d'entrer un entier par le clavier.
# La fonction input() lit une ligne de texte saisie par l'utilisateur et retourne une chaîne de caractères (str).
# La fonction int() convertit cette chaîne de caractères en un entier.
N = int(input())

# Création d'une liste qui va contenir des chaînes de caractères.
# La compréhension de liste suivante utilise une boucle for pour répéter N+1 fois.
# À chaque itération, la fonction input() est appelée pour lire une ligne de texte et l'ajouter à la liste.
S = [input() for _ in range(N + 1)]

# Définition d'une fonction nommée 'convert' qui prend un argument s.
# Cette fonction va convertir une chaîne de caractères en une liste contenant soit des entiers (pour les chiffres consécutifs)
# soit des caractères (pour tout le reste).
def convert(s):
    # Initialisation d'une liste vide l qui servira à stocker les résultats intermédiaires.
    l = []
    # On parcourt la chaîne de caractères caractère par caractère en utilisant son indice i.
    for i in range(len(s)):
        # On vérifie si le caractère courant s[i] est un chiffre.
        # La méthode isdigit() renvoie True si s[i] est dans '0123456789'.
        if s[i].isdigit():
            # Si la liste l n'est pas vide et si le dernier élément de l est une liste (c'est-à-dire déjà en train de collecter des chiffres consécutifs),
            if len(l) != 0 and isinstance(l[-1], list):
                # Alors on ajoute le chiffre courant à la dernière sous-liste pour agrandir le groupe de chiffres consécutifs.
                l[-1].append(s[i])
            else:
                # Sinon, on démarre un nouveau groupe de chiffres : on ajoute une nouvelle sous-liste contenant ce chiffre.
                l.append([s[i]])
        else:
            # Si le caractère courant n'est pas un chiffre, on l'ajoute tel quel (en tant que caractère) à la liste principale l.
            l.append(s[i])

    # À la fin, on parcourt la liste obtenue l,
    # Si un élément e est une liste (c'est-à-dire une liste de chiffres sous forme de chaînes de caractères),
    # on les joint ensemble avec ''.join(e) pour reconstituer un nombre entier sous forme de chaîne, puis on convertit cette chaîne en entier avec int().
    # Sinon, on garde le caractère tel quel.
    # Le résultat est une nouvelle liste où chaque groupe de chiffres consécutifs est remplacé par son équivalent entier,
    # et les caractères non numériques restent inchangés.
    return [int(''.join(e)) if isinstance(e, list) else e for e in l]

# On applique la fonction convert à chaque élément de la liste S grâce à une compréhension de liste.
# On remplace chaque chaîne de S par sa version décomposée en entiers et caractères.
S = [convert(e) for e in S]

# On sauvegarde le premier élément de S (qui vient de input()), qui servira de référence pour comparer les autres.
t = S[0]

# Définition d'une fonction compare qui prend en argument une liste s issue de la conversion.
def compare(s):
    # On veut comparer la liste courante s à la référence t, élément par élément.
    # On parcourt les deux listes en parallèle, sur la longueur du plus court des deux (pour éviter un index out-of-range).
    for i in range(min([len(s), len(t)])):
        # Si s[i] et t[i] sont du même type (par exemple : tous deux entiers OU tous deux caractères),
        if type(s[i]) == type(t[i]):
            # Si la valeur de l'élément courant de s est inférieure à celle de t, on retourne le signe '-'.
            if s[i] < t[i]:
                return '-'
            # Si la valeur de l'élément courant de s est supérieure à celle de t, on retourne le signe '+'.
            elif s[i] > t[i]:
                return '+'
        else:
            # Si les types des éléments courants diffèrent (exemple : un int et un str),
            # alors, si l'élément de s est un entier (donc t[i] est un caractère), on considère que s est plus petit et on retourne '-'.
            if type(s[i]) == int:
                return '-'
            # Sinon (donc t[i] est un entier et s[i] est un caractère), on considère que s est plus grand et on retourne '+'.
            else:
                return '+'
    # Si on arrive ici, c'est que tous les éléments comparés sont égaux jusqu'à ce que l'une des deux listes soit terminée.
    # Il faut alors comparer la longueur des listes.
    # Si la longueur de la référence t est inférieure ou égale à celle de s, alors s est considéré plus grand ou égal, on retourne '+'.
    if len(t) <= len(s):
        return '+'
    # Sinon, la liste s est plus courte, donc considérée plus petite, on retourne '-'.
    else:
        return '-'

# Pour chaque élément s dans la liste S, à partir du deuxième élément jusqu'à la fin (donc pour S[1], S[2], ..., S[N]),
for s in S[1:]:
    # On affiche le résultat de la comparaison de s avec la référence t par la fonction compare.
    print(compare(s))