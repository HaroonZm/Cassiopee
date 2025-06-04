input_count_a, input_count_b = [int(input_value) for input_value in input().split()]
set_elements_a = {int(element) for element in input().split()}
set_elements_b = {int(element) for element in input().split()}

intersection_ab = set_elements_a & set_elements_b
union_ab = set_elements_a | set_elements_b

print('{} {}'.format(len(intersection_ab), len(union_ab)))
for intersection_element in sorted(intersection_ab):
    print(intersection_element)
for union_element in sorted(union_ab):
    print(union_element)