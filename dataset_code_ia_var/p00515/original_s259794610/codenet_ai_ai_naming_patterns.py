score_total = 0
for index in range(5):
    score_saisi = int(input())
    if score_saisi < 40:
        score_saisi = 40
    score_total += score_saisi

score_moyen = score_total // 5
print(score_moyen)