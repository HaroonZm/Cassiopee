# Demande à l'utilisateur d'entrer une chaîne de caractères, et assigne cette chaîne à la variable S.
S = input()  # input() lit une entrée de l'utilisateur sous forme de chaîne de caractères.

# Initialise une variable appelée 'cur' à la lettre 'A'.
# Cette variable va garder en mémoire le caractère courant pour comparaison.
cur = 'A'  # On commence la comparaison avec le caractère 'A' en tant que référence initiale.

# Initialise une variable appelée 'ans' à 0.
# Cette variable va compter le nombre de fois que certaines conditions sont vérifiées dans la boucle.
ans = 0  # Le compteur commence donc à zéro.

# Crée une boucle qui va parcourir chaque indice 'i' de la chaîne S, c'est-à-dire de 0 jusqu'à la longueur de S moins 1.
for i in range(len(S)):
    # 'range' génère une séquence d'entiers, ici de 0 jusqu'à len(S)-1.
    # 'len(S)' donne le nombre total de caractères dans la chaîne S.
    # 'for i in ...' répète le bloc de code indenté pour chaque valeur de 'i'.

    # Vérifie si le caractère à la position i dans S est égal au caractère stocké dans 'cur'.
    # Ici, S[i] permet d'accéder au caractère à l'indice i de la chaîne S.
    if (S[i] == cur):
        # Si le caractère dans S est le même que 'cur', on incrémente le compteur 'ans' de 1.
        ans += 1  # Cela signifie que l'on a trouvé une "occurence" qui correspond à la condition.
    else:
        # Si le caractère courant S[i] n'est pas égal à 'cur', on entre dans ce bloc 'else'.

        # On vérifie si le caractère sauvegardé dans 'cur' a une valeur supérieure (dans l'ordre Unicode)
        # au caractère courant S[i]. En Python, la comparaison de caractères se fait selon leur code Unicode.
        if (cur > S[i]):
            # Si 'cur' est plus grand que S[i], alors on incrémente également 'ans' de 1.
            ans += 1

        # Dans tous les cas où S[i] != cur, on met à jour 'cur' pour qu'il devienne S[i].
        cur = S[i]  # Cela permet de garder en mémoire la dernière lettre traitée pour la prochaine boucle.

# Affiche la valeur finale du compteur 'ans' après avoir parcouru toute la chaîne S.
print(ans)  # print() affiche la valeur à l'écran.