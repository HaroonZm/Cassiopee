def is_balanced_bracket_sequence():
    """
    Vérifie si la séquence de parenthèses et de valeurs fournies forme une séquence correcte et équilibrée.

    Retour :
        None. Affiche 'YES' si la séquence est équilibrée, 'NO' sinon.

    Principe :
        Lis chaque opération, met à jour les compteurs de parenthèses ouvrantes et fermantes. 
        La séquence est correcte si le total des ouvrantes égale celui des fermantes
        et jamais à aucun moment il n'y a eu plus de fermantes que d'ouvrantes.
    """
    n = int(input())  # Lit le nombre d'opérations à effectuer

    a, b = 0, 0       # a : total de parenthèses ouvrantes, b : total de fermantes
    flag = 0          # flag : indicateur d'erreur de séquence (plus de fermantes que d'ouvrantes à un instant)

    for i in range(n):
        p, x = map(str, input().split())  # Lit un symbole (parenthèse) et une valeur

        if p == "(":                      # Si c'est une ouvrante
            a += int(x)                   # Ajoute la valeur au compte des ouvrantes
        else:                             # Sinon, c'est une fermante
            b += int(x)                   # Ajoute la valeur au compte des fermantes

        if a < b:                         # À tout moment, s'il y a plus de fermantes que d'ouvrantes
            flag = 1                      # on marque que la séquence est incorrecte
            break                         # et on cesse le traitement

    if flag == 1 or a != b:               # Si erreur détectée ou si déséquilibre à la fin
        print("NO")                       # La séquence n'est pas correcte
    else:
        print("YES")                      # La séquence est correcte et équilibrée

# Appel de la fonction principale
is_balanced_bracket_sequence()