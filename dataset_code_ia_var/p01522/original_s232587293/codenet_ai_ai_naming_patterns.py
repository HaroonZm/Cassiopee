num_people, num_boats = map(int, input().split())
boat_person_sets = [set(map(int, input().split()[1:])) for _ in range(num_boats)]
num_requests = int(input())
excluded_people_set = set()
for _ in range(num_requests):
    person_a, person_b = map(int, input().split())
    for person_set in boat_person_sets:
        if person_a in person_set and person_b in person_set:
            excluded_people_set.add(person_a)
            excluded_people_set.add(person_b)
            break
print(len(excluded_people_set))