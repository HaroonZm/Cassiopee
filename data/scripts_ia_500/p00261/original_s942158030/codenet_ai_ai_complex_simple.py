from functools import reduce
from operator import itemgetter

transitions = {
    'A': {'0': 'X', '1': 'Y'},
    'B': {'0': 'Y', '1': 'X'},
    'X': {'0': 'NA', '1': 'Z'},
    'Y': {'0': 'X', '1': 'NA'},
    'Z': {'0': 'W', '1': 'B'},
    'W': {'0': 'B', '1': 'Y'}
}

def awkward_status_fold(current_status, char):
    return transitions.get(current_status, {}).get(char, 'NA')

def convoluted_input_stream():
    import sys, itertools
    return (line.rstrip('\n\r') for line in itertools.chain.from_iterable([sys.stdin]))

def binary_cat_status(state_seq):
    return reduce(awkward_status_fold, state_seq, 'A')

for S in convoluted_input_stream():
    if S == '#':
        break
    status = binary_cat_status(S)
    print((lambda s: {True:"Yes", False:"No"}.get(s=='B'))(status))