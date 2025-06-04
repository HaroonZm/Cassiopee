original_text = input()
pattern = input()

is_subsequence = True

leftmost_positions = [0] * len(pattern)
pattern_index_forward = 0

for current_index_in_text, current_character_in_text in enumerate(original_text):

    if pattern_index_forward < len(pattern) and current_character_in_text == pattern[pattern_index_forward]:
        leftmost_positions[pattern_index_forward] = current_index_in_text
        pattern_index_forward += 1

if pattern_index_forward < len(pattern):
    is_subsequence = False

rightmost_positions = [0] * len(pattern)
pattern_index_backward = len(pattern) - 1

for current_index_in_text in range(len(original_text) - 1, -1, -1):

    current_character_in_text = original_text[current_index_in_text]

    if pattern_index_backward >= 0 and current_character_in_text == pattern[pattern_index_backward]:
        rightmost_positions[pattern_index_backward] = current_index_in_text
        pattern_index_backward -= 1

if pattern_index_backward >= 0:
    is_subsequence = False

if is_subsequence and leftmost_positions == rightmost_positions:
    print("yes")
else:
    print("no")