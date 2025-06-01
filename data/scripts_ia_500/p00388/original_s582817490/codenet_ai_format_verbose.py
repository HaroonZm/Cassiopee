hauteur, borne_inf, borne_sup = map(int, input().split())

nombre_diviseurs = 0

for candidat_diviseur in range(borne_inf, borne_sup + 1) :
    
    if hauteur % candidat_diviseur == 0 :
        
        nombre_diviseurs += 1

print(nombre_diviseurs)