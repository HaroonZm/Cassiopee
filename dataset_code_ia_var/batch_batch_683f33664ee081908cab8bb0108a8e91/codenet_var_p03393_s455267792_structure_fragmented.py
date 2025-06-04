def read_input():
    return input()

def is_last_permutation(S):
    return S == "zyxwvutsrqponmlkjihgfedcba"

def str_to_code(S):
    return list(map(lambda x: ord(x) - ord('a'), list(S)))

def find_smallest_missing_letter(code):
    for i in range(26):
        if i not in code:
            return i
    return None

def append_if_missing_letter(code):
    smallest_missing = find_smallest_missing_letter(code)
    if smallest_missing is not None:
        code.append(smallest_missing)
        return True
    return False

def can_increment_last_letter(code):
    if not code:
        return False
    return code[-1] != 25

def find_next_greater(code, last):
    for i in range(last+1,26):
        if i not in code:
            return i
    return None

def try_increment(code):
    while len(code) > 0:
        last = code[-1]
        new_code = code[:-1]
        if last == 25:
            code.pop()
            continue
        next_greater = find_next_greater(new_code, last)
        if next_greater is not None:
            new_code.append(next_greater)
            return new_code, True
        else:
            code.pop()
    return code, False

def code_to_str(code):
    return ''.join(list(map(lambda x: chr(x + ord('a')), code)))

def main():
    S = read_input()
    if is_last_permutation(S):
        print(-1)
        return

    code = str_to_code(S)
    done = False

    if not done:
        done = append_if_missing_letter(code)

    while len(code) > 0 and not done:
        code, done = try_increment(code)
        if done:
            break

    print(code_to_str(code))

main()