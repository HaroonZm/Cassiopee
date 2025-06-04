liste_x = []
# On récupère 5 nombres de l'utilisateur (pas très fun mais bon)
for truc in range(5):
    liste_x.append(int(input("Entrez un nombre: ")))

# Première condition, on regarde si le premier élément est positif.
if liste_x[0] > 0:
    print(int(liste_x[4] * (liste_x[1] - liste_x[0]))) # C'est quoi cette formule ?
else:
    resultat = abs(liste_x[0]) * liste_x[2] + liste_x[3] + liste_x[1] * liste_x[4]  # Un peu long, non ?
    print(resultat)  # Voilà, c'est affiché !