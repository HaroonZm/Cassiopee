participants_point_totals = {}

number_of_entries = int(input())

for _ in range(number_of_entries):
    participant_name, points_earned = input().split()
    participants_point_totals[participant_name] = participants_point_totals.get(participant_name, 0) + int(points_earned)

sorted_participants_by_name_length = sorted([(len(name), name) for name in participants_point_totals.keys()])

for name_length, participant_name in sorted_participants_by_name_length:
    print(participant_name, participants_point_totals[participant_name])