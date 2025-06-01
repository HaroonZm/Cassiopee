nombre_de_passagers = int(input())
nombre_d_arrets = int(input())
passagers_max = nombre_d_arrets
passagers_courants = nombre_d_arrets

for arret_index in range(nombre_de_passagers):
    passagers_sortants, passagers_entrants = map(int, input().split())
    passagers_courants += passagers_entrants - passagers_sortants
    if passagers_courants < 0:
        print(0)
        break
    passagers_max = max(passagers_max, passagers_courants)
else:
    print(passagers_max)