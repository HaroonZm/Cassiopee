MOVE = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5], [1, 4, 6], [2, 5, 7], [3, 6]]
answers = {"01234567": 0}

def convert_to_list(field):
    return list(field)

def swap_positions(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]

def convert_to_string(lst):
    return "".join(lst)

def swap(field, a, b):
    tmp = convert_to_list(field)
    swap_positions(tmp, a, b)
    return convert_to_string(tmp)

def initialize_queue():
    return [[0, "01234567"]]

def queue_not_empty(q):
    return len(q) != 0

def pop_from_queue(q):
    return q.pop(0)

def find_zero(field):
    return field.find("0")

def get_moves(position):
    return MOVE[position]

def is_not_in_answers(field, answers):
    return field not in answers

def add_to_answers(field, cost, answers):
    answers[field] = cost

def append_to_queue(queue, element):
    queue.append(element)

def breadth_first_search(answers):
    q = initialize_queue()

    while queue_not_empty(q):
        g, field = pop_from_queue(q)
        a = find_zero(field)

        for b in get_moves(a):
            tmp = swap(field, a, b)

            if is_not_in_answers(tmp, answers):
                add_to_answers(tmp, g+1, answers)
                append_to_queue(q, [g+1, tmp])

    return answers

def read_input():
    return raw_input()

def clean_input(input_str):
    return input_str.replace(" ", "")

def output_answer(answers, key):
    print answers[key]

answers = breadth_first_search(answers)

while True:
    try:
        user_input = read_input()
        clean_key = clean_input(user_input)
        output_answer(answers, clean_key)
    except:
        break