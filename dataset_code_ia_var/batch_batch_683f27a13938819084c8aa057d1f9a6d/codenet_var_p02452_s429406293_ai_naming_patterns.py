input_count_a = input()
set_a_elements = set(input().split())
input_count_b = input()
set_b_elements = set(input().split())
intersection_ab = set_a_elements & set_b_elements
is_b_subset_of_a = int(intersection_ab == set_b_elements)
print(is_b_subset_of_a)