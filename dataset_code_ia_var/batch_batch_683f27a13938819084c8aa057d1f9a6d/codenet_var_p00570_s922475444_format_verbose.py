nombre_de_jours, nombre_de_sessions = map(int, input().split())

liste_jours_occupation = [int(input()) for _ in range(nombre_de_jours)]

liste_ecarts_jours = [0 for _ in range(nombre_de_jours - 1)]

for indice_jour in range(nombre_de_jours - 1):
    liste_ecarts_jours[indice_jour] = (
        liste_jours_occupation[indice_jour + 1] 
        - liste_jours_occupation[indice_jour] 
        - 1
    )

liste_ecarts_jours.sort(reverse=True)

nombre_total_jours_necessaires = (
    liste_jours_occupation[-1] 
    - liste_jours_occupation[0] 
    + 1 
    - sum(liste_ecarts_jours[:nombre_de_sessions - 1])
)

print(nombre_total_jours_necessaires)