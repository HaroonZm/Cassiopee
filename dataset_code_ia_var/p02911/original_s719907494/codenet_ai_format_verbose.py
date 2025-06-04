number_of_players, number_of_questions, number_of_events = map(int, input().split())

player_correct_answers = [0] * number_of_players

for event_index in range(number_of_events):
    answered_player_index = int(input()) - 1
    player_correct_answers[answered_player_index] += 1

for player_index in range(number_of_players):
    questions_not_answered = number_of_events - player_correct_answers[player_index]
    remaining_lives = number_of_questions - questions_not_answered

    if remaining_lives > 0:
        print("Yes")
    else:
        print("No")