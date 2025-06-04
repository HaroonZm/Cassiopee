num_people, num_boats = map(int, raw_input().split())
boat_list = [map(int, raw_input().split()) for boat_idx in range(num_boats)]
num_hate_pairs = input()
hate_pair_list = [map(int, raw_input().split()) for hate_idx in range(num_hate_pairs)]
person_hate_flag = [0] * 51
for person_a, person_b in hate_pair_list:
    for boat_info in boat_list:
        if person_a in boat_info[1:] and person_b in boat_info[1:]:
            person_hate_flag[person_a] = 1
            person_hate_flag[person_b] = 1
print sum(person_hate_flag)