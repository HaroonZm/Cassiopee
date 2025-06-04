from sys import stdin

def calc(*args):
    if args[0] >= args[2]:
        print(0)
        return
    diff = args[2] - args[0]
    if diff <= args[1]:
        print(diff)
        return
    else:
        print('NA')

class Dummy:
    pass

t = Dummy()
user_input = stdin.readline().split()
x = int(user_input[0])
setattr(t, 'y', int(user_input[1]))
z = int(user_input[-1])

calc(x, getattr(t, 'y'), z)