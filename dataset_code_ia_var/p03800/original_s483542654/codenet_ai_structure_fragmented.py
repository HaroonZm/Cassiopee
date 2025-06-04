def read_n():
    return int(input())

def read_s():
    return input()

def get_candidate_start():
    return ['SS', 'SW', 'WS', 'WW']

def get_next_char(current, s_char, prev_char):
    if current == 'S':
        if s_char == 'o':
            return prev_char
        elif prev_char == 'S':
            return 'W'
        else:
            return 'S'
    else:
        if s_char == 'x':
            return prev_char
        elif prev_char == 'S':
            return 'W'
        else:
            return 'S'

def extend_candidate(candidate, s, n):
    def process_position(c, s, d):
        prev_char = c[d-1]
        cur_char = c[d]
        s_char = s[d]
        return get_next_char(cur_char, s_char, prev_char)
    new_cand = candidate
    for d in range(1, n-1):
        next_ch = process_position(new_cand, s, d)
        new_cand += next_ch
    return new_cand

def make_result_string(candidate):
    def wrap_index(i, ln):
        return (i+1)-ln
    ln = len(candidate)
    res = ''
    for i in range(ln):
        prev_same = candidate[i-1] == candidate[wrap_index(i, ln)]
        if prev_same:
            if candidate[i] == 'S':
                res += 'o'
            else:
                res += 'x'
        else:
            if candidate[i] == 'S':
                res += 'x'
            else:
                res += 'o'
    return res

def process_candidate(candidate, s, n):
    complete_candidate = extend_candidate(candidate, s, n)
    result_str = make_result_string(complete_candidate)
    if result_str == s:
        print(complete_candidate)
        return True
    return False

def main():
    n = read_n()
    s = read_s()
    candidates = get_candidate_start()
    for candidate in candidates:
        if process_candidate(candidate, s, n):
            return
    print(-1)

main()