nombre_de_tours = int(raw_input())

score_taro = 0
score_hana = 0

for index_du_tour in range(nombre_de_tours):
    
    cartes_taro_hana = raw_input().split(" ")
    
    carte_taro = cartes_taro_hana[0]
    carte_hana = cartes_taro_hana[1]
    
    if carte_taro > carte_hana:
        score_taro += 3
    
    elif carte_hana > carte_taro:
        score_hana += 3
    
    else:
        score_taro += 1
        score_hana += 1

print score_taro, score_hana