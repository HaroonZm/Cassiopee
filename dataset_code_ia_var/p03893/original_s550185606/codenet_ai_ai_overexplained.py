# Demande à l'utilisateur de saisir une valeur via le clavier, lit l'entrée sous forme de chaîne de caractères (string),
# puis convertit cette chaîne en un entier (int), c'est-à-dire un nombre sans décimale.
x = int(input())

# Initialise une variable nommée 'now' à la valeur 3.
# L'affectation (=) permet de stocker la valeur 3 dans la variable 'now'.
now = 3

# Commence une boucle for, qui va répéter les instructions indentées qui suivent.
# La fonction range(x) génère une séquence de nombres de 0 à (x-1), soit exactement 'x' itérations au total.
# Pour chaque itération, la variable inutile '_' prend la valeur du compteur, mais elle n'est pas utilisée ici,
# selon une convention qui consiste à nommer par '_' les variables non utilisées.
for _ in range(x):
    # À chaque passage dans la boucle, la variable 'now' devient le double de sa valeur actuelle augmenté de 1.
    # L'opération 'now * 2' multiplie la valeur de 'now' par 2 (autrement dit la double).
    # Ensuite, on ajoute 1 à ce résultat.
    # Enfin, le nouvel entier obtenu est affecté à 'now', écrasant sa précédente valeur.
    now = now * 2 + 1

# À la sortie de la boucle, on affiche (imprime) une valeur dans la console à l'aide de la fonction print().
# La valeur affichée est 'now - 1', c'est-à-dire la valeur actuelle de 'now', à laquelle on soustrait 1.
# Cette opération de soustraction (-) retire 1 à la dernière valeur de 'now'.
print(now - 1)