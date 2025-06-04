from itertools import combinations as itertools_combinations

while True:
    number_of_people = int(input())
    if number_of_people == 0:
        break

    person_to_gift_names = {}
    possible_gift_recipients = {}
    required_gift_count = {}
    list_of_people_names = []

    for _ in range(number_of_people):
        input_parts = input().split()
        person_name = input_parts[0]
        gift_names = input_parts[2:]
        person_to_gift_names[person_name] = gift_names
        list_of_people_names.append(person_name)

    for combination in list(itertools_combinations(person_to_gift_names.items(), number_of_people - 1)):
        excluded_people = []
        collected_gift_names = []

        for person, gifts in combination:
            excluded_people.append(person)
            collected_gift_names += gifts

        for person_name in list_of_people_names:
            if person_name not in excluded_people:
                possible_gift_recipients[person_name] = collected_gift_names
                break

    for person_name in person_to_gift_names.keys():
        unique_gift_counter = 0
        for given_gift_name in person_to_gift_names[person_name]:
            count_of_gift = possible_gift_recipients[person_name].count(given_gift_name)
            unique_gift_counter += number_of_people - count_of_gift
        required_gift_count[person_name] = unique_gift_counter

    sorted_results = sorted(
        required_gift_count.items(),
        key=lambda item: (item[1], item[0])
    )
    minimal_gift_person = sorted_results[0]
    print(minimal_gift_person[1], minimal_gift_person[0])