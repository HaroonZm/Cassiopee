def tokenize(filename):
    tokens = []
    i = 0
    while i < len(filename):
        c = filename[i]
        if c.isdigit():
            j = i
            while j < len(filename) and filename[j].isdigit():
                j += 1
            tokens.append(int(filename[i:j]))
            i = j
        else:
            tokens.append(c)
            i += 1
    return tokens

def compare_tokens(a, b):
    len_a, len_b = len(a), len(b)
    for i in range(min(len_a, len_b)):
        item_a, item_b = a[i], b[i]
        a_is_num = isinstance(item_a, int)
        b_is_num = isinstance(item_b, int)
        if a_is_num and b_is_num:
            if item_a != item_b:
                return item_a - item_b
        elif a_is_num and not b_is_num:
            return -1
        elif not a_is_num and b_is_num:
            return 1
        else:
            if item_a != item_b:
                return ord(item_a) - ord(item_b)
    # all compared items equal, shorter token list comes first
    return len_a - len_b

n = int(input())
s0 = input()
files = [input() for _ in range(n)]

s0_tokens = tokenize(s0)

for f in files:
    f_tokens = tokenize(f)
    cmp = compare_tokens(f_tokens, s0_tokens)
    if cmp < 0:
        print("-")
    else:
        print("+")