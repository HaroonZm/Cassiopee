def read_n():
    return int(input())

def read_a():
    return list(map(int, input().split()))

def append_large_value(a):
    a.append(20000000000)
    return a

def reversed_range(n):
    return list(range(0, n))[::-1]

def is_unique(a, i):
    return a[i] != a[i-1]

def process_indices(a, indices):
    result = []
    for i in indices:
        if is_unique(a, i):
            result.append(a[i])
    return result

def reverse_list(lst):
    return list(reversed(lst))

def print_list(lst):
    print(*lst)

def main():
    n = read_n()
    a = read_a()
    a = append_large_value(a)
    indices = reversed_range(n)
    ans = process_indices(a, indices)
    ans = reverse_list(ans)
    print_list(ans)

main()