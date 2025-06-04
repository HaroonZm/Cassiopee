import sys

YES = "Possible"
NO = "Impossible"

def get_amax(a):
    return max(a)

def get_vmin(amax):
    return (amax + 1) // 2

def get_nmin(amax):
    return amax % 2 + 1

def count_occurrences(a, value):
    return a.count(value)

def check_lower(vmin, a):
    for i in range(1, vmin):
        if count_occurrences(a, i) > 0:
            return False
    return True

def check_equal(vmin, nmin, a):
    return count_occurrences(a, vmin) == nmin

def check_higher(vmin, amax, a):
    for i in range(vmin+1, amax+1):
        if count_occurrences(a, i) < 2:
            return False
    return True

def output_result(flag):
    if flag:
        print(YES)
    else:
        print(NO)

def check_possible(N, a):
    amax = get_amax(a)
    vmin = get_vmin(amax)
    nmin = get_nmin(amax)
    if not check_lower(vmin, a):
        return False
    if not check_equal(vmin, nmin, a):
        return False
    if not check_higher(vmin, amax, a):
        return False
    return True

def solve(N, a):
    flag = check_possible(N, a)
    output_result(flag)

def read_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word

def read_N(tokens):
    return int(next(tokens))

def read_a(tokens, N):
    return [int(next(tokens)) for _ in range(N)]

def main():
    tokens = read_tokens()
    N = read_N(tokens)
    a = read_a(tokens, N)
    solve(N, a)

if __name__ == '__main__':
    main()