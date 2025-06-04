input_total_persons, input_total_boats = map(int, raw_input().split())
list_boat_person_map = [map(int, raw_input().split()) for boat_index in range(input_total_boats)]
input_total_hate_pairs = input()
list_hate_pairs = [map(int, raw_input().split()) for hate_pair_index in range(input_total_hate_pairs)]
list_person_hate_conflict = []
for hate_person_a, hate_person_b in list_hate_pairs:
    for boat_persons in list_boat_person_map:
        boat_members = boat_persons[1:]
        if hate_person_a in boat_members and hate_person_b in boat_members:
            if hate_person_a not in list_person_hate_conflict:
                list_person_hate_conflict.append(hate_person_a)
            if hate_person_b not in list_person_hate_conflict:
                list_person_hate_conflict.append(hate_person_b)
print len(list_person_hate_conflict)