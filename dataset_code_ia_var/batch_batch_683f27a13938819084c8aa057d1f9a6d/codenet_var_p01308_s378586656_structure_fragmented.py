def get_note_dict():
    return {
        "C": 0, "C#": 1, "D": 2, "D#": 3,
        "E": 4, "F": 5, "F#": 6, "G": 7,
        "G#": 8, "A": 9, "A#": 10, "B": 11
    }

def get_input_count():
    return int(input())

def get_case_input():
    n, m = map(int, input().split())
    t_input = input().split()
    s_input = input().split()
    return n, m, t_input, s_input

def convert_notes_to_numbers(notes_list, note_dict):
    return list(map(lambda x: note_dict[x], notes_list))

def prepare_t_lst(t_input, note_dict):
    base = [-100]
    converted = convert_notes_to_numbers(t_input, note_dict)
    return base + converted

def prepare_s_lst(s_input, note_dict):
    converted = convert_notes_to_numbers(s_input, note_dict)
    converted.reverse()
    return converted

def mod_12(x):
    return x % 12

def push_if_diff(stack, diff, t_index, s_index):
    if diff == 1:
        stack.append((t_index - 2, s_index + 1))
    if diff == 0:
        stack.append((t_index - 1, s_index + 1))
    if diff == 11:
        stack.append((t_index + 1, s_index + 1))

def valid_indices(t_index, n):
    return 0 < t_index <= n

def search_step(stack, t_lst, s_lst, n, m):
    t_index, s_index = stack.pop()
    if s_index == m:
        return t_index == 0
    if not valid_indices(t_index, n):
        return False
    base = t_lst[t_index]
    proc = s_lst[s_index]
    diff = mod_12(proc - base)
    push_if_diff(stack, diff, t_index, s_index)
    return False

def solve_case(n, m, t_input, s_input, note_dict):
    t_lst = prepare_t_lst(t_input, note_dict)
    s_lst = prepare_s_lst(s_input, note_dict)
    stack = [(n, 0), (n - 1, 0)]
    while stack:
        if search_step(stack, t_lst, s_lst, n, m):
            print("Yes")
            break
    else:
        print("No")

def main():
    note_dict = get_note_dict()
    t = get_input_count()
    for _ in range(t):
        n, m, t_input, s_input = get_case_input()
        solve_case(n, m, t_input, s_input, note_dict)

main()