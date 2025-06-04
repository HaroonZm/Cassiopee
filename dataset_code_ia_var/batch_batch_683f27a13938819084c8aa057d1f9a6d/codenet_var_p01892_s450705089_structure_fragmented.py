def read_input():
    return input()

def parse_input(raw_input):
    return map(int, raw_input.split())

def initialize_score(a, b):
    return abs(a - b)

def generate_range(n):
    return range(1, n + 1)

def compute_new_a(b, x, y):
    return b * x // y

def is_divisible(b, x, y):
    return (b * x) % y == 0

def update_score(current_score, a, new_a):
    return min(current_score, abs(a - new_a))

def inner_loop(a, b, n, score):
    x_range = generate_range(n)
    y_range = generate_range(n)
    for x in x_range:
        score = process_y_loop(a, b, x, y_range, score)
    return score

def process_y_loop(a, b, x, y_range, score):
    for y in y_range:
        if is_divisible(b, x, y):
            new_a = compute_new_a(b, x, y)
            score = update_score(score, a, new_a)
    return score

def main():
    raw_input = read_input()
    a, b, n = parse_input(raw_input)
    score = initialize_score(a, b)
    score = inner_loop(a, b, n, score)
    print(score)

main()