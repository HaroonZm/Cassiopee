input_string = input()

MODULO_BASE = 10 ** 9 + 7

number_of_ways_to_form_ABC = 0
number_of_ways_to_form_BC = 0
number_of_ways_to_form_C = 0
number_of_question_marks_seen = 0

for character in reversed(input_string):

    if character == "A":
        number_of_ways_to_form_ABC = (number_of_ways_to_form_ABC + number_of_ways_to_form_BC) % MODULO_BASE

    if character == "B":
        number_of_ways_to_form_BC = (number_of_ways_to_form_BC + number_of_ways_to_form_C) % MODULO_BASE

    if character == "C":
        number_of_ways_to_form_C = (pow(3, number_of_question_marks_seen, MODULO_BASE) + number_of_ways_to_form_C) % MODULO_BASE

    if character == "?":
        number_of_ways_to_form_ABC = (number_of_ways_to_form_ABC * 3 + number_of_ways_to_form_BC) % MODULO_BASE
        number_of_ways_to_form_BC = (number_of_ways_to_form_BC * 3 + number_of_ways_to_form_C) % MODULO_BASE
        number_of_ways_to_form_C = (pow(3, number_of_question_marks_seen, MODULO_BASE) + number_of_ways_to_form_C * 3) % MODULO_BASE
        number_of_question_marks_seen += 1

print(int(number_of_ways_to_form_ABC))