def to_numbers(line):
    return list(map(int, line.split()))

def build_number_dict(numbers):
    return {1:numbers[0], 2:numbers[1], 3:numbers[2], -3:numbers[3], -2:numbers[4], -1: numbers[5]}

def create_dice(numbers):
    return {
        'numbers': numbers,
        'number_dict': build_number_dict(numbers),
        'top': 1,
        'front': 2,
        'right': 3
    }

def set_move_n(dice):
    dice['top'], dice['front'] = dice['front'], -dice['top']

def set_move_s(dice):
    dice['top'], dice['front'] = -dice['front'], dice['top']

def set_move_e(dice):
    dice['top'], dice['right'] = -dice['right'], dice['top']

def set_move_w(dice):
    dice['top'], dice['right'] = dice['right'], -dice['top']

def move_dice(dice, direction):
    if direction == 'N':
        set_move_n(dice)
    elif direction == 'S':
        set_move_s(dice)
    elif direction == 'E':
        set_move_e(dice)
    else:
        set_move_w(dice)

def show_dice_number(dice):
    print(dice['number_dict'][dice['top']])

def get_input_numbers():
    return input()

def get_input_moves():
    return input()

def main():
    numbers = to_numbers(get_input_numbers())
    dice = create_dice(numbers)
    move_cmd = get_input_moves()
    for char in move_cmd:
        move_dice(dice, char)
    show_dice_number(dice)

main()