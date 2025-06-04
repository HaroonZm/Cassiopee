from collections import defaultdict

def parse_n(arg):
    return int(arg)

def parse_A(arg):
    return list(map(int, arg.split()))

def initialize_ret():
    return 0

def initialize_X():
    return defaultdict(int)

def update_X(X, a, i):
    X[a+i] += 1

def compute_key(i, a):
    return i - a

def is_valid_key(key):
    return key >= 0

def update_ret(ret, X, key):
    ret += X[key]
    return ret

def process_element(i, a, X, ret):
    update_X(X, a, i)
    key = compute_key(i, a)
    if is_valid_key(key):
        ret = update_ret(ret, X, key)
    return ret

def process_list(A):
    ret = initialize_ret()
    X = initialize_X()
    for i, a in enumerate(A):
        ret = process_element(i, a, X, ret)
    return ret

def solve(*args: str) -> str:
    n = parse_n(args[0])
    A = parse_A(args[1])
    result = process_list(A)
    return str(result)

if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))