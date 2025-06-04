number_of_hiroshi_type1_matches, number_of_hiroshi_type2_matches = [int(value) for value in input().split()]

number_of_kenjiro_type1_matches, number_of_kenjiro_type2_matches = [int(value) for value in input().split()]

points_per_type1_win, points_per_type2_win, bonus_per_10_type1_wins, bonus_per_20_type2_wins = [int(value) for value in input().split()]

hiroshi_total_score = (
    points_per_type1_win * number_of_hiroshi_type1_matches
    + bonus_per_10_type1_wins * (number_of_hiroshi_type1_matches // 10)
    + points_per_type2_win * number_of_hiroshi_type2_matches
    + bonus_per_20_type2_wins * (number_of_hiroshi_type2_matches // 20)
)

kenjiro_total_score = (
    points_per_type1_win * number_of_kenjiro_type1_matches
    + bonus_per_10_type1_wins * (number_of_kenjiro_type1_matches // 10)
    + points_per_type2_win * number_of_kenjiro_type2_matches
    + bonus_per_20_type2_wins * (number_of_kenjiro_type2_matches // 20)
)

if hiroshi_total_score > kenjiro_total_score:
    print("hiroshi")
elif hiroshi_total_score < kenjiro_total_score:
    print("kenjiro")
else:
    print("even")