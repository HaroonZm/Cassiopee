# Initialisation d'une variable de compteur appelée 'ans' qui va stocker le nombre de fois où deux caractères consécutifs de la chaîne sont différents.
ans = 0

# On demande à l'utilisateur de rentrer une chaîne de caractères.
# La fonction input() affiche une invite (ici vide) et attend que l'utilisateur tape des caractères puis appuie sur Entrée.
# Le texte tapé est alors stocké dans la variable 's' sous forme de chaîne de caractères (str).
s = input()

# La fonction range() est utilisée pour créer une séquence d’entiers.
# Ici, range(1, len(s)) crée une séquence commençant par 1 jusqu'à (mais sans inclure) len(s).
# len(s) renvoie le nombre de caractères de la chaîne 's'.
# La boucle for va donc parcourir tous les indices de 1 jusqu’à len(s) - 1 inclus.
for i in range(1, len(s)):
    # À chaque itération, on compare le caractère à l’indice actuel 'i' avec le caractère précédent, qui se trouve à l’indice 'i - 1'.
    # L’opérateur != signifie "différent de" : la condition est donc vraie si les deux caractères sont différents.
    if s[i] != s[i - 1]:
        # Si la condition précédente est vérifiée (les deux caractères consécutifs sont différents), on incrémente la variable 'ans' de 1.
        # Cela signifie que l’on a trouvé un endroit où deux caractères consécutifs ne sont pas identiques.
        ans += 1

# Après avoir examiné toute la chaîne, on vérifie la valeur de 'ans'.
# En Python, une valeur entière de 0 est considérée comme False dans un contexte booléen, et toute autre valeur est considérée comme True.
if ans:
    # Si 'ans' est différent de 0 (donc il y a eu au moins un endroit où deux caractères consécutifs sont différents),
    # on affiche la chaîne de caractères "Yes" à l'écran.
    print("Yes")
else:
    # Si 'ans' est égal à 0 (tous les caractères consécutifs sont identiques ou la chaîne a un seul caractère),
    # on affiche "No".
    print("No")