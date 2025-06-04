num_elements = int(input())
num_iterations = int(input())
reference_list = list(map(int, input().split()))
score_list = [0 for idx_element in range(num_elements)]

for idx_iteration in range(num_iterations):
    input_list = list(map(int, input().split()))
    for idx_element in range(num_elements):
        if input_list[idx_element] == reference_list[idx_iteration]:
            score_list[idx_element] += 1
    score_list[reference_list[idx_iteration] - 1] += num_elements - input_list.count(reference_list[idx_iteration])

for idx_element in range(num_elements):
    print(score_list[idx_element])