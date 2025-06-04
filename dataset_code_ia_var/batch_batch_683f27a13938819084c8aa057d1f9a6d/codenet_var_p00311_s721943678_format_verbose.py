# Lecture des hauteurs pour Hiroshi et Kenjiro
hiroshi_height_1, hiroshi_height_2 = map(int, input().split())

kenjiro_height_1, kenjiro_height_2 = map(int, input().split())

score_coefficient_a, score_coefficient_b, bonus_coefficient_c, bonus_coefficient_d = map(int, input().split())


def calculer_score(score_value_1, score_value_2):
    score = (
        score_coefficient_a * score_value_1
        + score_coefficient_b * score_value_2
        + bonus_coefficient_c * (score_value_1 // 10)
        + bonus_coefficient_d * (score_value_2 // 20)
    )
    return score


hiroshi_total_score = calculer_score(hiroshi_height_1, hiroshi_height_2)
kenjiro_total_score = calculer_score(kenjiro_height_1, kenjiro_height_2)

gagnant = 'even'

if hiroshi_total_score > kenjiro_total_score:
    gagnant = 'hiroshi'
elif hiroshi_total_score < kenjiro_total_score:
    gagnant = 'kenjiro'

print(gagnant)