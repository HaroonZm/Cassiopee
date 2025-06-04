def get_operation_dict():
    return {
        0: lambda x, y: max(x, y),
        1: lambda x, y: min(x, y)
    }

def read_int():
    return int(input())

def should_break(n):
    return n == 0

def get_initial_ans():
    return [0, 500]

def read_scores():
    return list(map(int, input().split()))

def compute_score(scores):
    return sum(scores)

def update_ans(ans, score, op_dict):
    updated = []
    for i in range(2):
        updated.append(op_dict[i](ans[i], score))
    return updated

def process_one_case(n, op_dict):
    ans = get_initial_ans()
    for _ in range(n):
        scores = read_scores()
        score = compute_score(scores)
        ans = update_ans(ans, score, op_dict)
    print_results(ans)

def print_results(ans):
    print(*ans)

def main_loop():
    op_dict = get_operation_dict()
    while True:
        n = read_int()
        if should_break(n):
            break
        process_one_case(n, op_dict)

main_loop()