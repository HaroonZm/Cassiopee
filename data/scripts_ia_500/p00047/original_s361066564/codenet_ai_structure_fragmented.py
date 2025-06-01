def read_input():
    return input()

def parse_input(line):
    return line.split(',')

def char_to_index(c):
    return ord(c) - ord("A")

def swap_balls(balls, idx1, idx2):
    balls[idx1], balls[idx2] = balls[idx2], balls[idx1]

def find_ball_index(balls):
    for i in range(len(balls)):
        if balls[i]:
            return i
    return None

def index_to_char(i):
    return chr(i + ord("A"))

def main_loop(balls):
    while True:
        try:
            line = read_input()
            a, b = parse_input(line)
            i1 = char_to_index(a)
            i2 = char_to_index(b)
            swap_balls(balls, i1, i2)
        except:
            break

def main():
    balls = [1,0,0]
    main_loop(balls)
    idx = find_ball_index(balls)
    if idx is not None:
        print(index_to_char(idx))

main()