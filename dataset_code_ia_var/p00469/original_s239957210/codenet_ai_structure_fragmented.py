import itertools

def read_n():
    return int(input())

def read_k():
    return int(input())

def should_terminate(n, k):
    return n == 0 and k == 0

def read_inputs(n):
    inputs = []
    for _ in range(n):
        inputs.append(input())
    return inputs

def generate_permutations(lst, k):
    return list(itertools.permutations(lst, k))

def join_permutations(permutations):
    result = []
    for item in permutations:
        result.append(''.join(item))
    return result

def unique_permutations(permutations):
    return list(set(permutations))

def print_result(count):
    print(count)

def process_once():
    n = read_n()
    k = read_k()
    if should_terminate(n, k):
        return False
    a = read_inputs(n)
    p = generate_permutations(a, k)
    b = join_permutations(p)
    c = unique_permutations(b)
    print_result(len(c))
    return True

def main_loop():
    while True:
        if not process_once():
            break

main_loop()