input_count_a = input()
input_set_a = set(map(int, input().split()))
input_count_b = input()
input_set_b = set(map(int, input().split()))
intersection_sorted_values = sorted(input_set_a & input_set_b)
for value_in_intersection in intersection_sorted_values:
    print(value_in_intersection)