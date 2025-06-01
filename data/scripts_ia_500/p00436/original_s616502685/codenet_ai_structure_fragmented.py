def read_int():
    return int(input())

def create_initial_list(n):
    return [i for i in range(1, 2 * n + 1)]

def rotate_list(s, a):
    return s[a:] + s[:a]

def interleave_halves(s, n):
    result = []
    for i in range(n):
        for j in [0, 1]:
            result.append(s[i + n * j])
    return result

def process_rotation(s, n, a):
    if a:
        s = rotate_list(s, a)
    else:
        s = interleave_halves(s, n)
    return s

def main():
    n = read_int()
    s = create_initial_list(n)
    q = read_int()
    for _ in range(q):
        a = read_int()
        s = process_rotation(s, n, a)
    for value in s:
        print(value)

main()