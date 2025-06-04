import sys

def set_recursion():
    sys.setrecursionlimit(10 ** 7)
    
def get_input():
    return sys.stdin.readline

def parse_n_q(input_func):
    return map(int, input_func().split())

def read_ab(q, input_func):
    ab_list = []
    for _ in range(q):
        ab_list.append([int(x) for x in input_func().split()])
    return ab_list

def make_initial_cup(n):
    return list(range(n+1)) + [0]

def make_initial_set():
    return set([0,1,2])

def swap_cups(cup, a, b):
    cup[a], cup[b] = cup[b], cup[a]
    
def find_ball_position(cup, a, b, curr_ball):
    new_ball = curr_ball
    for x in [a, b]:
        if cup[x] == 1:
            new_ball = x
    return new_ball

def update_set(se, cup, ball):
    se.add(cup[ball-1])
    se.add(cup[ball+1])

def remove_zero(se):
    if 0 in se:
        se.remove(0)

def compute_answer(se):
    return len(se)

def output(ans):
    print(ans)

def main():
    set_recursion()
    input_func = get_input()
    N, Q = parse_n_q(input_func)
    AB = read_ab(Q, input_func)
    cup = make_initial_cup(N)
    se = make_initial_set()
    ball = 1
    for a, b in AB:
        swap_cups(cup, a, b)
        ball = find_ball_position(cup, a, b, ball)
        update_set(se, cup, ball)
    remove_zero(se)
    answer = compute_answer(se)
    output(answer)

main()