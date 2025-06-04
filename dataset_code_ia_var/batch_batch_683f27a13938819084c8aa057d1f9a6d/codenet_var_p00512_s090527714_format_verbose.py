nombre_de_lignes_a_traiter = int(input())

somme_des_valeurs_par_cle = {}

for _ in [0] * nombre_de_lignes_a_traiter:
    cle_chaine, valeur_chaine = input().split()
    valeur_entier = int(valeur_chaine)
    somme_des_valeurs_par_cle[cle_chaine] = somme_des_valeurs_par_cle.get(cle_chaine, 0) + valeur_entier

def valeur_ordinale_de_cle(cle):
    return sum(
        27 ** position * (ord(caractere) - 64)
        for position, caractere in enumerate(cle[::-1])
    )

cles_triees = sorted(
    somme_des_valeurs_par_cle,
    key=lambda cle: (valeur_ordinale_de_cle(cle), cle)
)

for cle in cles_triees:
    print(cle, somme_des_valeurs_par_cle[cle])