def read_dice():
    return input().split()

def read_number_of_queries():
    return int(input())

def read_query():
    return input().split()

def assign_dice(dice):
    return [d for d in dice]

def swap_north(dice):
    return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

def swap_east(dice):
    return [dice[0], dice[2], dice[4], dice[1], dice[3], dice[5]]

def swap_west(dice):
    return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]

def perform_west_loop(dice, top, front, maxloop):
    for w in range(maxloop):
        if check_top_front(dice, top, front):
            return dice, True
        dice = swap_west(dice)
    return dice, False

def perform_north_loop(dice, top, front, maxloop):
    for n in range(maxloop):
        d, found = perform_west_loop(dice, top, front, maxloop)
        if found:
            return d, True
        dice = swap_north(dice)
    return dice, False

def perform_east_loop(dice, top, front, maxloop):
    for e in range(maxloop):
        d, found = perform_north_loop(dice, top, front, maxloop)
        if found:
            return d, True
        dice = swap_east(dice)
    return dice, False

def check_top_front(dice, top, front):
    return dice[0] == top and dice[1] == front

def print_right_face(dice):
    print(dice[2])

def process_query(orig_dice, top, front, maxloop):
    dice = assign_dice(orig_dice)
    new_dice, found = perform_east_loop(dice, top, front, maxloop)
    if found:
        print_right_face(new_dice)

def main():
    maxloop = 4
    dice = read_dice()
    q = read_number_of_queries()
    orig_dice = assign_dice(dice)
    for _ in range(q):
        query = read_query()
        top, front = query[0], query[1]
        process_query(orig_dice, top, front, maxloop)

main()