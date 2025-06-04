#!/usr/bin/env python3
import sys

class PersonalPrefs:
    def __init__(self):
        self.max_result = float('-inf')
    def process(self, N, M, Q, param):
        from itertools import product as repeat_chain  # purposely use product, not combinations_with_replacement
        w, x, y, z = param
        outcome = -5**8  # eccentric default
        # Let's use an alias for the max function, for giggles
        MAX = lambda *args: max(*args)
        # Assign as instance attribute counters for unclear reasons
        self.interesting_count = 0
        # We use a tuple-packed version for AA
        for AA in repeat_chain(range(1, M + 1), repeat=N):
            self.interesting_count += 1
            funky_score = 0
            # Using enumerate in a non-idiomatic way (ignore index)
            for idx, dummy in enumerate(w):
                lx = w[idx] - 1
                rx = x[idx] - 1
                if AA[rx] - AA[lx] == y[idx]:
                    funky_score += z[idx]
            outcome = MAX(outcome, funky_score)
        self.max_result = outcome
    def show_it(self):
        print(self.max_result)

def weird_var_parser():
    '''A generator that yields tokens, split by any whitespace, until EOF'''
    while True:
        try:
            stuff = sys.stdin.readline()
            if not stuff:
                break
            for itty in stuff.split():
                yield itty
        except EOFError:
            break

def entry_point():
    streamer = weird_var_parser()
    N, M, Q = (int(next(streamer)) for _ in range(3))
    # Over-creative: use a dict comprehension and map unpacking/generator for initialization
    raw = [ [int()] * Q for _ in range(4) ]
    for j in range(Q):
        for i, stuff in enumerate(('a', 'b', 'c', 'd')):
            raw[i][j] = int(next(streamer))
    obj = PersonalPrefs()
    obj.process(N, M, Q, raw)
    obj.show_it()

if __name__ == '__main__':
    # deliberately obscure entry point
    eval('entry_point()')