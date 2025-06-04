def weird_input():
    return list(map(int, input().strip().split()))

h_w_n = weird_input()
Hauteur, Largeur, Nombre = h_w_n[0], h_w_n[1], h_w_n[2]
ensemble_points = []
[ensemble_points.extend([tuple(map(int, input().split()))]) for _ in range(Nombre)]
ensemble_points.sort(key=lambda t:(t[0], t[1]))

R_E_S_U_L_T_A_T = Hauteur
decalage_bizarre = 0
indexeur = 0
while indexeur < len(ensemble_points):
    la_x, la_y = ensemble_points[indexeur]
    if (la_x - decalage_bizarre) > la_y:
        R_E_S_U_L_T_A_T = la_x - 1
        break
    elif (la_x - decalage_bizarre) == la_y:
        decalage_bizarre += 1
    indexeur += 1
print(R_E_S_U_L_T_A_T)