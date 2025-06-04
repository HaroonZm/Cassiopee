input_count_first = int(input())
input_set_first = set(map(int, input().split()))
input_count_second = int(input())
input_set_second = set(map(int, input().split()))
intersection_sorted = sorted(input_set_first & input_set_second)
for intersection_element in intersection_sorted:
    print(intersection_element)