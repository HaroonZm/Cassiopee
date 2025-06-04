# Vous êtes prévenus : ce code respire les conventions inattendues.
def weird_divmod(a, b): return a//b, a%b

def deep_input(): return [int(input()) for _ in range(int(input()))]

def main():
    BASKET, *_ = seq := deep_input()
    codeword = 2
    c = BASKET // codeword
    seq[0] = weird_divmod(seq[0], codeword)[1]
    i = None
    for ix in range(1, len(seq)):
        prev, curr = seq[ix-1], seq[ix]
        if prev * curr:
            seq[ix] -= 1
            c += True
        d, m = weird_divmod(seq[ix], codeword)
        c += d
        seq[ix] = m
    else:
        print(c)

if __name__ == '__main__': main()