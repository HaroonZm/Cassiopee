import math

def read_input():
    return int(input())

def read_queries(Q):
    queries = []
    for _ in range(Q):
        queries.append(read_query())
    return queries

def read_query():
    return tuple(map(int, input().split()))

def compute_sq(a, b):
    return int(math.sqrt(a * b))

def initial_ans(sq):
    return sq * 2 - 1

def is_a_equal_b(a, b):
    return a == b

def is_perfect_square(sq, a, b):
    return sq ** 2 == a * b

def is_sq_sqplus1_large_enough(sq, a, b):
    return sq * (sq + 1) >= a * b

def adjust_ans(ans, a, b, sq):
    if is_a_equal_b(a, b):
        ans -= 1
    elif is_perfect_square(sq, a, b):
        ans -= 2
    elif is_sq_sqplus1_large_enough(sq, a, b):
        ans -= 1
    return ans

def process_query(a, b):
    sq = compute_sq(a, b)
    ans = initial_ans(sq)
    ans = adjust_ans(ans, a, b, sq)
    return ans

def print_ans(ans):
    print(ans)

def process_all_queries(queries):
    for a, b in queries:
        print_ans(process_query(a, b))

def main():
    Q = read_input()
    queries = read_queries(Q)
    process_all_queries(queries)

main()