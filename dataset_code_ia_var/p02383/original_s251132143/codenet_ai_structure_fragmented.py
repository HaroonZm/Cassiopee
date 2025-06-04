def parse_labels(input_str):
    return [int(i) for i in input_str.split()]

def get_command(input_str):
    return input_str

def assign_north(d):
    a, b, c, f = d[0], d[1], d[5], d[4]
    return [b, c, d[2], d[3], a, f]

def assign_south(d):
    a, b, c, f = d[0], d[1], d[5], d[4]
    return [f, a, d[2], d[3], c, b]

def assign_east(d):
    a, c, f, d_ = d[0], d[2], d[5], d[3]
    return [d_, d[1], a, f, d[4], c]

def assign_west(d):
    a, c, f, d_ = d[0], d[2], d[5], d[3]
    return [c, d[1], f, a, d[4], d_]

def roll_north(d):
    new_d = assign_north(d)
    d[0], d[1], d[4], d[5] = new_d[0], new_d[1], new_d[4], new_d[5]

def roll_south(d):
    new_d = assign_south(d)
    d[0], d[1], d[4], d[5] = new_d[0], new_d[1], new_d[4], new_d[5]

def roll_east(d):
    new_d = assign_east(d)
    d[0], d[2], d[3], d[5] = new_d[0], new_d[2], new_d[3], new_d[5]

def roll_west(d):
    new_d = assign_west(d)
    d[0], d[2], d[3], d[5] = new_d[0], new_d[2], new_d[3], new_d[5]

def do_roll(d, direction):
    if direction == "N":
        roll_north(d)
    elif direction == "S":
        roll_south(d)
    elif direction == "E":
        roll_east(d)
    else:
        roll_west(d)

def create_dice(labels):
    return {'d': labels}

def dice_roll(dice, direction):
    do_roll(dice['d'], direction)

def process_commands(dice, commands):
    for direction in commands:
        dice_roll(dice, direction)

def get_top(dice):
    return dice['d'][0]

def main():
    label_input = input()
    cmd_input = input()
    labels = parse_labels(label_input)
    commands = get_command(cmd_input)
    dice = create_dice(labels)
    process_commands(dice, commands)
    print(get_top(dice))

main()