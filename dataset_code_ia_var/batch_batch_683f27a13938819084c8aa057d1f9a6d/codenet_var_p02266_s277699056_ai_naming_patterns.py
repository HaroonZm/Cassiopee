input_string = input()
pond_stack = []
segment_stack = []
total_area = 0

for current_index, char in enumerate(input_string):
    if char == "\\":
        pond_stack.append(current_index)
    elif char == "/" and pond_stack:
        left_edge = pond_stack.pop()
        current_area = current_index - left_edge
        total_area += current_area
        while segment_stack and segment_stack[-1][0] > left_edge:
            current_area += segment_stack.pop()[1]
        segment_stack.append([left_edge, current_area])

print(total_area)
print(len(segment_stack), *[segment[1] for segment in segment_stack])