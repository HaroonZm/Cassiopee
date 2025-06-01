from copy import copy

while True:

    number_of_people, step_count_input = [int(value) for value in input().split()]

    if number_of_people == 0 and step_count_input == 0:
        break

    elimination_step = step_count_input - 1

    circle_of_people = [person_id + 1 for person_id in range(number_of_people)]

    while True:

        current_circle_length = len(circle_of_people)

        if current_circle_length == 1:
            print(circle_of_people[0])
            break

        pivot_position = (elimination_step + 1) % current_circle_length

        if pivot_position != 0:
            circle_of_people = copy(circle_of_people[pivot_position:] + circle_of_people[:pivot_position - 1])
        else:
            circle_of_people = copy(circle_of_people[:-1])