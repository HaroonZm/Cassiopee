from collections import deque

input_length = int(input())
input_values = list(map(int, input().split()))

output_deque = deque()

for index in range(input_length):
    if index % 2 == 0:
        output_deque.append(input_values[index])
    else:
        output_deque.appendleft(input_values[index])

output_list = list(output_deque)
if input_length % 2 == 1:
    output_list = reversed(output_list)

print(*output_list)