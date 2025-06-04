from itertools import zip_longest, count

def compare_quoted_strings(s1, s2):
    w1, w2 = s1.split('"'), s2.split('"')
    if len(w1) != len(w2):
        return "DIFFERENT"
    state = "IDENTICAL"
    for i, (a, b) in enumerate(zip(w1, w2)):
        if a != b:
            if i % 2 == 0:
                return "DIFFERENT"
            if state == "IDENTICAL":
                state = "CLOSE"
            else:
                return "DIFFERENT"
    return state

for s1 in iter(input, '.'):
    s2 = input()
    print(compare_quoted_strings(s1, s2))