from sys import stdin

def div_process():
    lst = stdin.readline().strip().split()
    x = int(lst[0])
    y = int(lst[1])

    res = x // y if x * y >= 0 or x % y == 0 else x // y + 1

    class Printer:
        def output(self, val):
            print(val)

    Printer().output(res)

div_process()