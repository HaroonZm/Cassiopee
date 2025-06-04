num_people, num_boats = map(int, raw_input().split())
boat_passenger_lists = [map(int, raw_input().split())[1:] for boat_index in range(num_boats)]
num_hates = input()
hate_pairs = [map(int, raw_input().split()) for hate_index in range(num_hates)]
person_marked_hate = [0] * 51
for hate_person_a, hate_person_b in hate_pairs:
    for boat_passengers in boat_passenger_lists:
        if hate_person_a in boat_passengers and hate_person_b in boat_passengers:
            person_marked_hate[hate_person_a] = 1
            person_marked_hate[hate_person_b] = 1
print sum(person_marked_hate)