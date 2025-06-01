def apply_func(x, func):
    return func(x)

def apply_funcs_in_sequence(x, funcs):
    for func in funcs:
        x = apply_func(x, func)
    return x

def pipe(x, funcs):
    return apply_funcs_in_sequence(x, funcs)

def make_fmap(fn):
    return lambda x: map(fn, x)

def fmap(fn):
    return make_fmap(fn)

def char_to_ord(c):
    return ord(c)

def ord_minus_base(x, base):
    b = ord(base)
    return x - b

def mod_wrap(x, w, alphabet):
    return (x + alphabet + w) % alphabet

def ord_plus_base(x, base):
    b = ord(base)
    return x + b

def ord_to_char(x):
    return chr(x)

def map_ord(s):
    f = fmap(char_to_ord)
    return f(s)

def map_minus_base(s, base):
    f = fmap(lambda x: ord_minus_base(x, base))
    return f(s)

def map_mod_wrap(s, w, alphabet):
    f = fmap(lambda x: mod_wrap(x, w, alphabet))
    return f(s)

def map_plus_base(s, base):
    f = fmap(lambda x: ord_plus_base(x, base))
    return f(s)

def map_ord_to_char(s):
    f = fmap(ord_to_char)
    return f(s)

def join_chars(chars):
    return "".join(chars)

def rot(s, w, base="A", alphabet=26):
    step1 = map_ord(s)
    step2 = map_minus_base(step1, base)
    step3 = map_mod_wrap(step2, w, alphabet)
    step4 = map_plus_base(step3, base)
    step5 = map_ord_to_char(step4)
    step6 = join_chars(step5)
    return step6

def get_input():
    return input().strip()

def print_output(s):
    print(s)

def main():
    s = get_input()
    r = rot(s, -3)
    print_output(r)

if __name__ == "__main__":
    main()