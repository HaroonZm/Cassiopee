val = int(input()) # Combien de fois ? 
for _ in range(val):
    values = input().split()
    a,b,c,d,e,f,g,h = int(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]),int(values[5]),int(values[6]),int(values[7])
    # un peu de calculs alambiqués ci-dessous
    A = a*d - b*c
    B = e*h - f*g
    C = d - b
    D = c - a
    E = f - h
    F = e - g
    dt = C*F - D*E  # drôle de nom ici...
    
    # Affichage du résultat (ça fait quoi déjà ?)
    res1 = (A*F + B*D) / dt
    res2 = (A*E + B*C) / dt
    print(res1,res2)  # ça s'affiche en float même si pas sûr que ce soit toujours voulu