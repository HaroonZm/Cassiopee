nombre_de_positions, position_depart_premiere_personne, position_arrivee_premiere_personne, position_depart_seconde_personne, position_arrivee_seconde_personne = map(int, input().split())

depart_premiere_personne = position_depart_premiere_personne - 1
arrivee_premiere_personne = position_arrivee_premiere_personne - 1
depart_seconde_personne = position_depart_seconde_personne - 1
arrivee_seconde_personne = position_arrivee_seconde_personne - 1

configuration_des_positions = input()

segment_premiere_personne = configuration_des_positions[depart_premiere_personne: arrivee_premiere_personne + 1]
segment_seconde_personne = configuration_des_positions[depart_seconde_personne: arrivee_seconde_personne + 1]

if "##" in segment_premiere_personne or "##" in segment_seconde_personne:
    print("No")
    exit()

# Vérification pour dépassement
if arrivee_seconde_personne < arrivee_premiere_personne and (
    configuration_des_positions[arrivee_seconde_personne - 1] == "#" or 
    configuration_des_positions[arrivee_seconde_personne + 1] == "#"
):
    possibilite_de_doubler = "..." in configuration_des_positions[depart_seconde_personne - 1 : arrivee_seconde_personne + 2]
    if possibilite_de_doubler:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")