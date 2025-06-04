def read_input():
    n, m = map(int, input().split())
    return n, m

def initialize_redball(n):
    redball = [0] * n
    set_first_redball(redball)
    return redball

def set_first_redball(redball):
    redball[0] = 1

def initialize_ball_cnt(n):
    return [1] * n

def read_transfer():
    x, y = map(int, input().split())
    return x - 1, y - 1

def process_transfer(x, y, redball, ball_cnt):
    if should_move_redball_only(x, ball_cnt, redball):
        move_redball(x, y, redball)
    elif should_influence_by_red(x, ball_cnt, redball):
        set_redball_to_y(y, redball)
    update_balls(x, y, ball_cnt)

def should_move_redball_only(x, ball_cnt, redball):
    return ball_cnt[x] == 1 and redball[x] == 1

def move_redball(x, y, redball):
    redball[x] = 0
    redball[y] = 1

def should_influence_by_red(x, ball_cnt, redball):
    return ball_cnt[x] > 1 and redball[x] == 1

def set_redball_to_y(y, redball):
    redball[y] = 1

def update_balls(x, y, ball_cnt):
    ball_cnt[x] -= 1
    ball_cnt[y] += 1

def count_redballs(redball):
    return redball.count(1)

def main():
    n, m = read_input()
    redball = initialize_redball(n)
    ball_cnt = initialize_ball_cnt(n)
    for _ in range(m):
        x, y = read_transfer()
        process_transfer(x, y, redball, ball_cnt)
    print(count_redballs(redball))

main()