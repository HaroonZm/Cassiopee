def add_answer(ans, answers):
    answers.append(' '.join(map(str, ans)))

def can_use(i, limit):
    return i <= limit

def try_append(i, ans, rest, limit, answers):
    if can_use(i, limit):
        new_ans = ans + [i]
        new_rest = rest - i
        call_square(new_ans, new_rest, i, answers)

def loop_over_i(rest, limit, ans, answers):
    for i in range(rest, 0, -1):
        try_append(i, ans, rest, limit, answers)

def call_square(ans, rest, limit, answers):
    if rest == 0:
        add_answer(ans, answers)
    else:
        loop_over_i(rest, limit, ans, answers)

def read_input():
    import sys
    for line in sys.stdin:
        yield line

def parse_input(lines):
    for line in lines:
        n = int(line)
        yield n

def process_input():
    lines = read_input()
    numbers = parse_input(lines)
    return numbers

def main_loop(numbers, answers):
    for n in numbers:
        if n == 0:
            break
        call_square([], n, n, answers)

def print_answers(answers):
    print('\n'.join(answers))

def solve():
    answers = []
    numbers = process_input()
    main_loop(numbers, answers)
    print_answers(answers)

solve()