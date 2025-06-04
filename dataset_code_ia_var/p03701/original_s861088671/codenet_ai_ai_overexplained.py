# Initialise une liste vide qui sera nommée 'a'. Cette liste va contenir des éléments.
# La syntaxe '[input() for i in range(input())]' est appelée une compréhension de liste.
# 'input()' lit une entrée de l'utilisateur au clavier sous forme de chaîne de caractères.
# Nous faisons 'range(input())' : or, 'input()' retourne une chaîne, donc en Python 2 ce code marche car il considère une chaîne numérique. 
# Pour chaque valeur de i dans range du nombre donné, on lit une entrée de l'utilisateur (input()).
# Les résultats (chaînes) sont collectés dans une liste.
# Ensuite, nous ajoutons à cette liste le nombre 0 via + [0] (concaténation de liste contenant 0).
a = [input() for i in range(input())] + [0]

# On veut calculer la somme des éléments de la liste 'a'. 
# Cependant, 'a' contient des chaînes de caractères (input() produit des chaînes).
# En Python2, la somme de chaînes lève une exception, donc on suppose que les entrées sont des entiers.
# Donc implicitement, l'utilisateur doit saisir des entiers et la somme fonctionnera.
s = sum(a)  # 'sum' additionne chaque élément de la liste 'a' et retourne la somme totale

# Nous créons une variable 'z' et lui assignons la valeur 0.
# Cette variable va servir à mémoriser la plus grande valeur admissible trouvée.
z = 0

# On commence une boucle for pour parcourir chaque élément 'i' dans la liste 'a'.
for i in a:
    # Nous soustrayons 'i' de la somme totale 's', pour obtenir la somme de tous les autres éléments sauf 'i'.
    # On vérifie si cette nouvelle somme ('s - i') n'est PAS un multiple de 10.
    # L'opérateur '%' est le modulo : '(s - i) % 10' donne le reste de la division de '(s - i)' par 10.
    # Si ce reste est strictement supérieur à 0, cela veut dire que '(s - i)' n'est pas un multiple de 10.
    if (s - i) % 10 > 0:
        # Nous utilisons la fonction max pour garder la plus grande valeur entre l'actuelle 'z' et '(s - i)'.
        # Si '(s - i)' est plus grand que 'z', 'z' prend cette nouvelle valeur, sinon il reste inchangé.
        z = max(z, s - i)

# Enfin, nous affichons la valeur de 'z' à l'écran avec 'print'.
print z