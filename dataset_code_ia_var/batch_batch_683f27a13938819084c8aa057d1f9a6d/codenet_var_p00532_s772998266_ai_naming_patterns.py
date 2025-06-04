num_elements = int(input())
num_iterations = int(input())

input_list = list(map(int, input().split()))
count_list = [0] * num_elements

for iteration_index in range(num_iterations):
    compare_list = list(map(int, input().split()))
    for element_index in range(num_elements):
        if input_list[iteration_index] == compare_list[element_index]:
            count_list[element_index] += 1
        else:
            count_list[input_list[iteration_index] - 1] += 1

for output_index in range(num_elements):
    print(count_list[output_index])