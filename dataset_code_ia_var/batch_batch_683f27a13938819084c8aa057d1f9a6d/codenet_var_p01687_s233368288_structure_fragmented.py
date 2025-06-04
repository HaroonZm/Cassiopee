def get_reference():
    return list("AADINNUY")

def get_aizu():
    return "AIZUNYAN"

def get_input():
    return raw_input()

def is_shorter_than_eight(inp):
    return len(inp) < 8

def print_input(inp):
    print inp

def get_input_length(inp):
    return len(inp)

def need_replacement(inp, i, l, ref):
    return i <= l-8 and sorted(inp[i:i+8]) == ref

def append_aizu(ans, aizu):
    return ans + aizu

def append_char(ans, char):
    return ans + char

def increment_by_eight(i):
    return i + 8

def increment_by_one(i):
    return i + 1

def process_input(inp, ref, aizu):
    ans = ""
    l = get_input_length(inp)
    i = 0
    while i < l:
        if need_replacement(inp, i, l, ref):
            ans = append_aizu(ans, aizu)
            i = increment_by_eight(i)
        else:
            ans = append_char(ans, inp[i])
            i = increment_by_one(i)
    return ans

def print_ans(ans):
    print ans

def main():
    ref = get_reference()
    aizu = get_aizu()
    inp = get_input()
    if is_shorter_than_eight(inp):
        print_input(inp)
    else:
        ans = process_input(inp, ref, aizu)
        print_ans(ans)

main()