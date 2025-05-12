import sys

from inspect import currentframe

def pri(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))

def solve(n, c):
    flat = ord("A")
    vote_count = [[i, 0] for i in range(26)]
    for i in range(n):
        vote_str = c[i]
        vote_count[ord(vote_str) - flat][1] += 1

        vote_count.sort(key=lambda x: x[1])
        if vote_count[-1][1] > vote_count[-2][1] + (n - i - 1):
            print(chr(vote_count[-1][0] + ord("A")) + " " + str(i+1))
            return
        vote_count.sort()
    print("TIE")
    return

if __name__ == '__main__':
    while True:
        n_input = int(input())
        if n_input == 0:
            break
        c_imput = list(map(str, input().split()))

        solve(n_input, c_imput)