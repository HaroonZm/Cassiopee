# Initialisation d'une variable appelée 'ans' avec la valeur entière zéro.
# Cette variable servira à stocker la somme cumulative résultante
ans = 0

# Utilisation d'une boucle 'for' qui itère un nombre fixe de fois.
# La fonction range(5) génère une séquence de 5 nombres allant de 0 à 4 inclus.
# La variable 'i' prendra successivement chacune de ces valeurs, mais ici elle n'est pas utilisée dans le corps de la boucle.
for i in range(5):
    # Demande à l'utilisateur d'entrer une valeur via 'input()'.
    # 'input()' lit une chaîne de caractères depuis l'entrée standard (le clavier).
    # La fonction 'int()' convertit cette chaîne en un entier.
    utilisateur_valeur = int(input())
    
    # La fonction 'max(a, b)' retourne la valeur la plus grande entre 'a' et 'b'.
    # Ici on compare 40 et la valeur entrée par l'utilisateur.
    # Cela signifie qu'on prend au minimum 40, même si l'entrée est inférieure.
    valeur_max = max(40, utilisateur_valeur)
    
    # On divise la valeur retournée par 'max' par 5 en utilisant la division entière '//'.
    # La division entière donne le quotient sans la partie décimale.
    division = valeur_max // 5
    
    # On ajoute ce quotient à la variable cumulative 'ans' en utilisant l'opérateur '+='.
    # L'opérateur '+=' est un raccourci pour 'ans = ans + division'.
    ans += division

# Après la fin de la boucle, on affiche la valeur finale de 'ans' qui est la somme calculée.
# 'print()' affiche la valeur donnée à la sortie standard (par exemple l'écran).
print(ans)