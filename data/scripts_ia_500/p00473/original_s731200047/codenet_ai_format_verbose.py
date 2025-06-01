nombre_de_points = int(input())

distance_minimale = [float('inf')] * (nombre_de_points + 1)
distance_minimale[0] = 0

couts_deplacement = [int(input()) for _ in range(nombre_de_points - 1)]

for position_courante in range(1, nombre_de_points):
    
    for position_precedente in range(position_courante):
        
        cout_depuis_opposé = distance_minimale[position_courante - position_precedente] + couts_deplacement[position_courante - 1]
        if cout_depuis_opposé < distance_minimale[position_precedente]:
            distance_minimale[position_precedente] = cout_depuis_opposé
        
        cout_depuis_precedente = distance_minimale[position_precedente] + couts_deplacement[position_courante - 1]
        if cout_depuis_precedente < distance_minimale[position_courante - position_precedente]:
            distance_minimale[position_courante - position_precedente] = cout_depuis_precedente

print(distance_minimale[nombre_de_points // 2])