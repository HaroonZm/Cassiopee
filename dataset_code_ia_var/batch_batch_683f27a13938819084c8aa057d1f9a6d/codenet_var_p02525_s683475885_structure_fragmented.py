import math

def read_input():
    return int(raw_input())

def read_scores():
    return map(float, raw_input().split())

def compute_mean(scores):
    return sum(scores) / len(scores)

def diff_square(score, mean):
    return (score - mean) ** 2

def accumulate_variance(scores, mean, n):
    total = 0
    for i in range(n):
        total += diff_square(scores[i], mean) / n
    return total

def compute_stddev(variance):
    return math.sqrt(variance)

def format_result(result):
    return '%.6f' % result

def process_case():
    n = read_input()
    if n == 0:
        return False
    scores = read_scores()
    mean = compute_mean(scores)
    variance = accumulate_variance(scores, mean, n)
    stddev = compute_stddev(variance)
    print format_result(stddev)
    return True

def main_loop():
    while True:
        if not process_case():
            break

main_loop()