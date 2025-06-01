def read_int():
    return int(input())

def read_line():
    return input()

def parse_line_to_score(line):
    parts = line.split()
    return parts

def count_win_draw(parts):
    win = 0
    draw = 0
    for i in range(1, len(parts)):
        if parts[i] == '1':
            continue
        elif parts[i] == '0':
            win += 1
        else:
            draw += 1
    return win, draw

def process_scores(N):
    score = []
    for _ in range(N):
        line = read_line()
        parts = parse_line_to_score(line)
        win, draw = count_win_draw(parts)
        score.append((parts[0], win, draw))
    return score

def sort_scores(score):
    return sorted(score, reverse=True, key=lambda x: (x[1], x[2]))

def print_scores(sorted_score):
    for s in sorted_score:
        print(s[0])

def solve():
    N = read_int()
    if check_zero(N):
        return -1
    scores = process_scores(N)
    sorted_scores = sort_scores(scores)
    print_scores(sorted_scores)

def check_zero(N):
    return N == 0

def main_loop():
    while True:
        if solve() is not None:
            break

main_loop()