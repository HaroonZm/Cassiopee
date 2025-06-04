class Dice:
    def __init__(self, pip):
        self.pip = pip

def create_dice(pip):
    return Dice(pip)

def parse_pip_input():
    return list(map(int, input().split()))

def parse_query_count():
    return int(input())

def parse_query():
    return map(int, input().split())

def roll_east(pip):
    a, b, c, d, e, f = pip
    return [d, b, a, f, e, c]

def roll_west(pip):
    a, b, c, d, e, f = pip
    return [c, b, f, a, e, d]

def roll_north(pip):
    a, b, c, d, e, f = pip
    return [b, f, c, d, a, e]

def roll_south(pip):
    a, b, c, d, e, f = pip
    return [e, a, c, d, f, b]

def move_dice(dice, direction):
    if direction == "E":
        dice.pip = roll_east(dice.pip)
    elif direction == "W":
        dice.pip = roll_west(dice.pip)
    elif direction == "N":
        dice.pip = roll_north(dice.pip)
    elif direction == "S":
        dice.pip = roll_south(dice.pip)

def should_stop(dice, top, front):
    return dice.pip[0] == top and dice.pip[1] == front

def do_alignment_rotation(dice, top, front):
    for op in "EEENEEENEEESEEESEEENEEEN":
        if should_stop(dice, top, front):
            break
        move_dice(dice, op)

def print_right_face(dice):
    print(dice.pip[2])

def handle_single_query(dice):
    top, front = parse_query()
    do_alignment_rotation(dice, top, front)
    print_right_face(dice)

def handle_queries(dice, n):
    for _ in range(n):
        handle_single_query(dice)

def main():
    dice = create_dice(parse_pip_input())
    n = parse_query_count()
    handle_queries(dice, n)

main()