nombre_entier_saisi = int(input())

representation_ternaire_équilibrée = []

while nombre_entier_saisi:
    
    reste_division_par_trois = nombre_entier_saisi % 3
    
    if reste_division_par_trois == 0:
        representation_ternaire_équilibrée = ["0"] + representation_ternaire_équilibrée
        nombre_entier_saisi //= 3
    
    elif reste_division_par_trois == 1:
        representation_ternaire_équilibrée = ["+"] + representation_ternaire_équilibrée
        nombre_entier_saisi = (nombre_entier_saisi - 1) // 3
    
    else:  # reste_division_par_trois == 2
        representation_ternaire_équilibrée = ["-"] + representation_ternaire_équilibrée
        nombre_entier_saisi = (nombre_entier_saisi + 1) // 3

print("".join(representation_ternaire_équilibrée))