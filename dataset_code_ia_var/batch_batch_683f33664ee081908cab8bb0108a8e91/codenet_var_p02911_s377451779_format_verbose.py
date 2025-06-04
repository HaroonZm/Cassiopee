number_of_players, number_of_initial_points, number_of_questions = map(int, input().split())

question_correct_responders = [None] * number_of_questions

player_total_points = [number_of_initial_points - number_of_questions] * number_of_players

for question_index in range(number_of_questions):
    responder_id = int(input()) - 1
    question_correct_responders[question_index] = responder_id
    player_total_points[responder_id] += 1

for player_index in range(number_of_players):
    if player_total_points[player_index] > 0:
        print('Yes')
    else:
        print('No')