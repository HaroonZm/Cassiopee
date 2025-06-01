import math

nombre_entier = int(input())

log_base_2_du_nombre = math.log2(nombre_entier)

puissance_de_2_inferieure_ou_egale = 2 ** (math.floor(log_base_2_du_nombre))

print(puissance_de_2_inferieure_ou_egale)