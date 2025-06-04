def parse_label_input():
    return list(map(int, input().split()))

def parse_op_input():
    return list(input())

def unpack_label(label):
    return label[0], label[1], label[2], label[3], label[4], label[5]

def assign_initial_faces(dice_obj, label):
    dice_obj.top, dice_obj.front, dice_obj.right, dice_obj.left, dice_obj.rear, dice_obj.bottom = unpack_label(label)

def roll_north(dice_obj):
    temp = dice_obj.top
    dice_obj.top   = dice_obj.front
    dice_obj.front = dice_obj.bottom
    dice_obj.bottom= dice_obj.rear
    dice_obj.rear  = temp

def roll_east(dice_obj):
    temp = dice_obj.top
    dice_obj.top    = dice_obj.left
    dice_obj.left   = dice_obj.bottom
    dice_obj.bottom = dice_obj.right
    dice_obj.right  = temp

def roll_west(dice_obj):
    temp = dice_obj.top
    dice_obj.top    = dice_obj.right
    dice_obj.right  = dice_obj.bottom
    dice_obj.bottom = dice_obj.left
    dice_obj.left   = temp

def roll_south(dice_obj):
    temp = dice_obj.top
    dice_obj.top    = dice_obj.rear
    dice_obj.rear   = dice_obj.bottom
    dice_obj.bottom = dice_obj.front
    dice_obj.front  = temp

def apply_roll(dice_obj, op):
    if op == 'N':
        roll_north(dice_obj)
    elif op == 'E':
        roll_east(dice_obj)
    elif op == 'W':
        roll_west(dice_obj)
    elif op == 'S':
        roll_south(dice_obj)

def print_top_face(dice_obj):
    print(dice_obj.top)

class dice:
    def __init__(self, label):
        assign_initial_faces(self, label)
    def roll(self, op):
        apply_roll(self, op)
    def print_top(self):
        print_top_face(self)

def process_operations(d, op_list):
    for op in op_list:
        d.roll(op)

def main():
    label = parse_label_input()
    op_list = parse_op_input()
    d = dice(label)
    process_operations(d, op_list)
    d.print_top()

main()