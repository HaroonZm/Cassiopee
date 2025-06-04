nombre_de_caracteres = int(input())

chaine_a_verifier = input()

if nombre_de_caracteres % 2 != 0:
    print("No")
    exit()

indice_milieu = int(len(chaine_a_verifier) / 2)

premiere_moitie = chaine_a_verifier[0:indice_milieu]

seconde_moitie = chaine_a_verifier[indice_milieu:len(chaine_a_verifier)]

if premiere_moitie == seconde_moitie:
    print("Yes")
else:
    print("No")