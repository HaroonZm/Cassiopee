def read_nm():
    return map(int, input().split())

def read_xy(m):
    return [read_pair() for _ in range(m)]

def read_pair():
    return list(map(int, input().split()))

def initialize_ball(n):
    return [1] * (n+1)

def initialize_red(n):
    r = [0] * (n+1)
    r[1] = 1
    return r

def process_pairs(xy, ball, red):
    for x, y in xy:
        process_single_pair(x, y, ball, red)

def process_single_pair(x, y, ball, red):
    decrease_ball(x, ball)
    increase_ball(y, ball)
    if is_red(x, red):
        make_red(y, red)
        if is_empty(x, ball):
            remove_red(x, red)

def decrease_ball(idx, ball):
    ball[idx] -= 1

def increase_ball(idx, ball):
    ball[idx] += 1

def is_red(idx, red):
    return red[idx] == 1

def make_red(idx, red):
    red[idx] = 1

def is_empty(idx, ball):
    return ball[idx] == 0

def remove_red(idx, red):
    red[idx] = 0

def count_red(red):
    return sum(red)

def main():
    n, m = read_nm()
    xy = read_xy(m)
    ball = initialize_ball(n)
    red = initialize_red(n)
    process_pairs(xy, ball, red)
    print(count_red(red))

main()