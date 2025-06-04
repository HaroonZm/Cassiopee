from sys import exit

LEFT_CHARS = set('qwertasdfgzxcvb')

def left_strike(ch): return ch in LEFT_CHARS

def process(seq):
    flag, total = left_strike(seq[0]), 0
    for char in seq:
        if left_strike(char):
            if flag is False:
                flag = True; total += 1
        else:
            if flag: flag = False; total += 1
    return total

def main():
    while 1:
        inp = input()
        if inp.startswith('#'):
            exit(0)
        s = list(inp)
        if len(s) == 0:
            print(0)
            continue
        print(process(s))

main()