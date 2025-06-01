# Cette solution lit les 5 scores des élèves, ajuste ceux inférieurs à 40 à 40, puis calcule et affiche la moyenne entière
scores = [int(input()) for _ in range(5)]

# On remplace chaque score inférieur à 40 par 40, sinon on garde le score original
adjusted_scores = [score if score >= 40 else 40 for score in scores]

# Calculer la somme des scores ajustés
total = sum(adjusted_scores)

# Puis calculer la moyenne par division entière (division normale car la moyenne est garantie entière)
average = total // 5

# Affichage de la moyenne finale
print(average)