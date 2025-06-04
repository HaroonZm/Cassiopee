input_total_students, input_max_a, input_max_b = map(int, input().split())
input_students_sequence = input()
count_a = 0
count_b = 0
for index_student in range(len(input_students_sequence)):
    current_student_type = input_students_sequence[index_student]
    if current_student_type == "a":
        if count_a + count_b < input_max_a + input_max_b:
            print("Yes")
            count_a += 1
        else:
            print("No")
    elif current_student_type == "b":
        if count_a + count_b < input_max_a + input_max_b and count_b < input_max_b:
            print("Yes")
            count_b += 1
        else:
            print("No")
    else:
        print("No")