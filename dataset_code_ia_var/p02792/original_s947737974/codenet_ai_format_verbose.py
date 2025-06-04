nombre_maximal = int(input())

compteur_premiere_derniere_chiffre = [[0] * 10 for _ in range(10)]

for entier_actuel in range(1, nombre_maximal + 1):

    entier_texte = str(entier_actuel)

    premier_chiffre_str = entier_texte[0]
    dernier_chiffre_str = entier_texte[-1]

    if premier_chiffre_str == "0" or dernier_chiffre_str == "0":
        continue

    premier_chiffre = int(premier_chiffre_str)
    dernier_chiffre = int(dernier_chiffre_str)

    compteur_premiere_derniere_chiffre[premier_chiffre][dernier_chiffre] += 1

total_paires_inverses = 0

for premiere_valeur in range(1, 10):
    for derniere_valeur in range(1, 10):
        total_paires_inverses += (
            compteur_premiere_derniere_chiffre[premiere_valeur][derniere_valeur]
            * compteur_premiere_derniere_chiffre[derniere_valeur][premiere_valeur]
        )

print(total_paires_inverses)