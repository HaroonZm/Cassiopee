nombre_elements, nombre_choisis = [int(valeur) for valeur in input().split()]

modulo = 10**9 + 7

facteurielle_max_N = 10**6

liste_factorielles = [1]
liste_factorielles_inverses = [0] * (facteurielle_max_N + 4)

for indice in range(facteurielle_max_N + 3):
    nouvelle_valeur = liste_factorielles[-1] * (indice + 1) % modulo
    liste_factorielles.append(nouvelle_valeur)

liste_factorielles_inverses[-1] = pow(liste_factorielles[-1], modulo - 2, modulo)

for indice in range(facteurielle_max_N + 2, -1, -1):
    liste_factorielles_inverses[indice] = (
        liste_factorielles_inverses[indice + 1] * (indice + 1) % modulo
    )

def combinaison_modulo(n, k, modulo):
    if k < 0 or k > n:
        return 0
    return (
        liste_factorielles[n]
        * liste_factorielles_inverses[k] % modulo
        * liste_factorielles_inverses[n - k] % modulo
    )

if nombre_choisis >= nombre_elements:

    resultat = combinaison_modulo(2 * nombre_elements - 1, nombre_elements, modulo)
    print(resultat)

else:

    resultat_cumulatif = 1

    for valeur_indice in range(1, nombre_choisis + 1):

        valeur_combinaison_1 = combinaison_modulo(nombre_elements, valeur_indice, modulo)
        valeur_combinaison_2 = combinaison_modulo(
            nombre_elements - 1, nombre_elements - valeur_indice - 1, modulo
        )
        resultat_cumulatif = (
            resultat_cumulatif + valeur_combinaison_1 * valeur_combinaison_2
        ) % modulo

    print(resultat_cumulatif)