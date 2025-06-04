input_count_a = int(input())
input_set_a = set(map(int, input().split()))
input_count_b = int(input())
input_set_b = set(map(int, input().split()))
difference_set = input_set_b - input_set_a
if difference_set:
    print(0)
else:
    print(1)