# Demande à l'utilisateur de rentrer une valeur entière, qui sera assignée à la variable s
s = int(input())  # input() lit une chaîne de caractères depuis l'entrée standard, int() convertit cette chaîne en entier

# Définit la valeur du modulo, une grande valeur première couramment utilisée pour éviter les débordements lors de calculs avec de grandes valeurs
mod = 10 ** 9 + 7  # ** est l'opérateur de puissance en Python, donc 10 à la puissance 9 plus 7 donne 1000000007

# Initialise la variable de la réponse finale à 0
ans = 0  # Cette variable va accumuler la somme totale au fur et à mesure de la boucle principale

# Commence une boucle for où l commence à 1 et s'incrémente jusqu'à 999 inclus (range(1, 1000) crée une séquence d'entiers de 1 à 999 inclus)
for l in range(1, 1000):
    # Calcule la valeur intermédiaire ss en soustrayant deux fois l et 1 à la valeur s.
    # L'opération 2*l consiste à multiplier l par 2, puis on enlève encore 1.
    ss = s - 2 * l - 1

    # Vérifie si ss est strictement négatif, c'est-à-dire si le nombre d'éléments restants est insuffisant
    if ss < 0:
        # Si ss est négatif, passe à l'itération suivante de la boucle for, sans exécuter le reste du bloc courant
        continue

    # Initialise une variable pour le calcul du coefficient binomial (combinaison)
    comb = 1  # On commence le produit à 1 car c'est l'élément neutre de la multiplication

    # Boucle pour calculer le coefficient binomial C(ss, l-1) = ss! / [(l-1)! * (ss - l + 1)!]
    for i in range(l - 1):
        # À chaque itération :
        # - On multiplie comb par (ss - i), ce qui revient à calculer la partie supérieure du produit pour le coefficient binomial
        comb *= ss - i

        # - Ensuite, on divise le résultat par (i + 1), ce qui correspond à la partie inférieure du produit (factorielle)
        comb //= i + 1  # // pour une division entière (non flottante), pour éviter de perdre la partie entière

    # Ajoute le coefficient binomial calculé à la réponse totale
    ans += comb

    # Prend le modulo pour éviter d'obtenir des nombres trop grands, ce qui peut causer un dépassement de capacité (overflow)
    ans %= mod

# Après avoir terminé toutes les itérations de la boucle for, affiche la réponse finale calculée
print(ans)  # print() affiche la valeur ans à la sortie standard (par exemple, dans la console)