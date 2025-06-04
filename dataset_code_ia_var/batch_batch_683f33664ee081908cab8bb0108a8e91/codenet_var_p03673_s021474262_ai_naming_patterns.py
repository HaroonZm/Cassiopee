from collections import deque

input_length = int(input())
input_sequence = list(map(int, input().split()))

is_even_length = (input_length % 2 == 0)

processed_deque = deque()
for index in range(input_length):
    if index % 2 == 0:
        processed_deque.append(input_sequence[index])
    else:
        processed_deque.appendleft(input_sequence[index])

ordered_sequence = list(processed_deque)
if is_even_length:
    for value in ordered_sequence:
        print(value, end=" ")
else:
    for value in reversed(ordered_sequence):
        print(value, end=" ")