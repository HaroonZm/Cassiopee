input_count = int(input())
input_list_a = list(map(int, input().split()))
input_list_b = list(map(int, input().split()))
input_list_c = list(map(int, input().split()))
total_score = sum(input_list_b)
for index in range(input_count - 1):
    if input_list_a[index + 1] == input_list_a[index] + 1:
        total_score += input_list_c[input_list_a[index] - 1]
print(total_score)