# Boucle pour itérer 9 fois
for i in range(9):
    # Lecture d'une ligne d'entrée et découpage en trois parties : name, p et a
    name, p, a = raw_input().split()
    
    # Conversion des valeurs p et a en entiers
    p, a = int(p), int(a)
    
    # Calcul et affichage :
    # - le nom
    # - la somme de p et a
    # - une valeur calculée avec la formule p*200 + a*300
    print name, p + a, p * 200 + a * 300