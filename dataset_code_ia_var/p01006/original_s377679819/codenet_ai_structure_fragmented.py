def get_ref():
    return {"A": "BD", "B": "ACE", "C": "BF", "D": "AEG", "E": "BDFH", "F": "CEI", "G": "DH", "H": "EGI", "I": "HF"}

def input_loop(times, ref):
    for _ in range(times):
        process_input(ref)

def process_input(ref):
    p = read_input()
    if check_sequence(p, ref):
        output_valid(p)

def read_input():
    return raw_input()

def check_sequence(p, ref):
    for i in range(get_length_minus_one(p)):
        if not is_transition_valid(p, i, ref):
            return False
    return True

def get_length_minus_one(p):
    return len(p) - 1

def is_transition_valid(p, i, ref):
    prev_char = get_char_at(p, i)
    next_char = get_char_at(p, i + 1)
    return next_char_in_ref(prev_char, next_char, ref)

def get_char_at(s, idx):
    return s[idx]

def next_char_in_ref(prev_char, next_char, ref):
    return next_char in ref[prev_char]

def output_valid(p):
    print p

def main():
    ref = get_ref()
    input_loop(1000, ref)

main()