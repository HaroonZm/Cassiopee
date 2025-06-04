input_count = int(input())
input_list_a, input_list_b, input_list_c = [list(map(int, input().split())) for _ in range(3)]
total_sum = sum(input_list_b)
for index in range(input_count - 1):
    if input_list_a[index + 1] - input_list_a[index] == 1:
        total_sum += input_list_c[input_list_a[index] - 1]
print(total_sum)