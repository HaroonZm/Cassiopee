# Demande à l'utilisateur d'entrer une chaîne de caractères (par exemple, une suite de '0' et '1')
s = input()

# Utilise la méthode .count() sur la chaîne s pour compter combien il y a de caractères '0'
# Le résultat est stocké dans la variable c0
c0 = s.count('0')

# De la même manière, compte combien il y a de caractères '1' dans la chaîne s
# Le résultat est stocké dans la variable c1
c1 = s.count('1')

# La fonction min(c0, c1) permet de trouver le plus petit nombre entre c0 et c1
# Cela correspond au nombre minimal de paires '0'-'1' qu'on peut former (chaque paire utilise un '0' et un '1')
# On multiplie ce minimum par 2 pour avoir le nombre total de caractères impliqués dans ces paires
# Enfin, la fonction print() affiche le résultat à l'écran pour l'utilisateur
print(2 * min(c0, c1))