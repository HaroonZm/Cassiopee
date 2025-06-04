nombre_de_personnes, capacite_maximale = [int(entree_utilisateur) for entree_utilisateur in input().split(" ")]

if nombre_de_personnes <= capacite_maximale:

    print(1)

else:

    print(0)