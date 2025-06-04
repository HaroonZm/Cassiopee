# On assigne la valeur 999 à la variable 'm'. 
# 'm' va contenir la différence minimale entre le nombre 753 et une séquence de 3 chiffres consécutifs trouvée dans la chaîne saisie.
m = 999

# On demande à l'utilisateur d'entrer une chaîne de caractères, puis on l'assigne à la variable 's'.
# input() permet de récupérer la saisie de l'utilisateur sous forme de texte (string).
s = input()

# On commence une boucle 'for' pour parcourir la chaîne 's'. 
# 'range(len(s) - 2)' génère une séquence de nombres de 0 à (longueur de s - 3 incluse).
# Cela garantit qu'on peut toujours extraire une sous-chaîne de 3 caractères sans dépasser la longueur de la chaîne.
for i in range(len(s) - 2):
    # On extrait une sous-chaîne de 3 caractères de 's', en commençant à l'indice 'i'.
    # s[i:i+3] signifie prendre les caractères à partir de l'indice i (inclus) jusqu'à i+3 (exclu)
    sous_chaine = s[i:i+3]
    
    # On convertit la sous-chaîne extraite en entier avec int().
    # Cela fonctionne seulement si la sous-chaîne contient uniquement des chiffres.
    nombre = int(sous_chaine)
    
    # On calcule la valeur absolue de la différence entre 753 et le nombre extrait,
    # c'est-à-dire la distance numérique entre ces deux nombres.
    difference = abs(753 - nombre)
    
    # On vérifie si la différence obtenue est inférieure à la valeur actuellement stockée dans 'm'.
    # Si oui, cela signifie qu'on a trouvé une différence plus faible, donc on met à jour 'm'.
    if difference < m:
        m = difference

# On affiche la plus petite différence trouvée.
print(m)