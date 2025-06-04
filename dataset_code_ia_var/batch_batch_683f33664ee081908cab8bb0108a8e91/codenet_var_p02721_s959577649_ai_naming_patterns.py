num_total, num_select, interval_dist = map(int, input().split())
seats_str = input()

left_indices = [0] * num_select
left_ptr = 0
for idx_left in range(num_select):
    while seats_str[left_ptr] == "x":
        left_ptr += 1
    left_indices[idx_left] = left_ptr
    left_ptr += interval_dist + 1

right_indices = [0] * num_select
right_ptr = num_total - 1
for idx_right in range(num_select - 1, -1, -1):
    while seats_str[right_ptr] == "x":
        right_ptr -= 1
    right_indices[idx_right] = right_ptr
    right_ptr -= interval_dist + 1

for index_left, index_right in zip(left_indices, right_indices):
    if index_left == index_right:
        print(index_left + 1)