import sys

def cmp(x, y):
    if x == y:
        return "EQUAL"
    return "GREATER" if x > y else "LESS"

class Input:
    def __init__(self):
        self.x, self.y = [int(i) for i in sys.stdin.readline().split()]

def dispatch():
    input_vals = Input()
    print(cmp(input_vals.x, input_vals.y))

dispatch()