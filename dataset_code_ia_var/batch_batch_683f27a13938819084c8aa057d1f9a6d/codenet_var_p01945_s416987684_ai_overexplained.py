# Demande à l'utilisateur de saisir une chaîne de caractères, puis assigne cette chaîne à la variable 's'
s = input()

# Initialise une variable entière 'ans' à zéro. Cette variable servira à compter ou à mémoriser un certain résultat.
ans = 0

# Utilise une boucle for pour itérer sur chaque indice 'i' de la chaîne 's'.
# La fonction len(s) retourne la longueur (le nombre de caractères) de la chaîne s.
# range(len(s)) génère une séquence d'entiers allant de 0 jusqu'à la longueur de s moins un, ce qui permet de parcourir chaque caractère par son indice.
for i in range(len(s)):
    # Vérifie si le caractère actuel de la chaîne (celui à l'indice i) est un astérisque ('*').
    # s[i] permet d'accéder au caractère d'indice i dans la chaîne s.
    if s[i] == "*":
        # Si le caractère actuel est un astérisque, la boucle se termine immédiatement grâce à l'instruction 'break'.
        # 'break' provoque l'arrêt immédiat de la boucle qui l'englobe, même si tous les éléments n'ont pas été parcourus.
        break

    # Si le caractère n'est pas un astérisque, vérifie s'il s'agit du caractère parenthèse ouvrante '('.
    elif s[i] == "(":
        # Si le caractère actuel est une parenthèse ouvrante, incrémente la variable 'ans' de 1.
        # Cela signifie que l'on ajoute 1 à la valeur actuelle de 'ans'.
        ans += 1

    # Si le caractère n'est ni un astérisque ni une parenthèse ouvrante, alors ce bloc s'exécute.
    else:
        # Dans ce cas, décrémente la variable 'ans' de 1.
        # Cela retire 1 à la valeur actuelle de 'ans'.
        ans -= 1

# Après la fin de la boucle (soit après avoir parcouru tous les caractères, soit après avoir rencontré un astérisque), affiche la valeur finale de 'ans' sur la sortie standard.
# La fonction print() affiche à l'écran la valeur passée en argument.
print(ans)