def process_intersection():
    input_first_size = int(input())
    input_first_list = list(map(int, input().split()))
    input_second_size = int(input())
    input_second_list = list(map(int, input().split()))
    intersection_sorted_list = sorted(set(input_first_list) & set(input_second_list))
    for intersection_element in intersection_sorted_list:
        print(intersection_element)

if __name__ == '__main__':
    process_intersection()