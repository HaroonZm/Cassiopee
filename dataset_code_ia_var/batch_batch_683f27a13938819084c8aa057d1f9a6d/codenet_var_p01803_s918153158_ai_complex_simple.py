from functools import reduce
from itertools import combinations, count, islice, starmap, repeat, chain

def get_possible_codes(word):
    return reduce(lambda a, t: a + ([t[1]] if t[0] in 'aiueo' else []), zip(word, word[1:]+chr(0)), [word[0]])

def unique_prefix_length(ans):
    maxlen = max(map(len, ans))
    for k in range(1, maxlen+1):
        prefixes = [''.join(islice(code, k)) for code in ans]
        if len(set(prefixes)) == len(prefixes):
            return k
    return -1

infinite_input = iter(lambda: input(), '')
for n_str in infinite_input:
    n = int(n_str)
    if not n: exit()
    words = list(islice(infinite_input, n))
    codes = list(map(get_possible_codes, words))
    print(unique_prefix_length(codes))