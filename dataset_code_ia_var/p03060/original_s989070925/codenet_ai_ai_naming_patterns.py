input_count = int(input())
value_list = list(map(int, input().split()))
cost_list = list(map(int, input().split()))
total_score = 0
for index in range(input_count):
    difference_score = value_list[index] - cost_list[index]
    if difference_score > 0:
        total_score += difference_score
print(total_score)