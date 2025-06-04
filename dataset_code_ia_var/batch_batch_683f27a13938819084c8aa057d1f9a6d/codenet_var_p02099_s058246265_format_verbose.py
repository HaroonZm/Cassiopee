from bisect import bisect_left as bisect_left_index
from bisect import bisect_right as bisect_right_index

number_of_students = int(input())

gpa_list = []
for _ in range(number_of_students):
    gpa_list.append(float(input()))

sorted_gpa_list = sorted(gpa_list)

for current_gpa in gpa_list:
    count_of_lower_gpa = bisect_left_index(sorted_gpa_list, current_gpa)
    count_of_higher_gpa = bisect_right_index(sorted_gpa_list, current_gpa)
    
    number_of_students_with_lower_gpa = count_of_lower_gpa
    number_of_students_with_higher_gpa = len(sorted_gpa_list) - count_of_higher_gpa
    number_of_students_with_same_gpa = count_of_higher_gpa - count_of_lower_gpa - 1

    result = number_of_students_with_lower_gpa * 3 + number_of_students_with_same_gpa
    print(result)