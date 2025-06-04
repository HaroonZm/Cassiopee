import sys

sys.setrecursionlimit(10000000)
inf = 10 ** 20

def get_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def get_int_list_minus1():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def get_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def get_str_list():
    return sys.stdin.readline().split()

def get_int():
    return int(sys.stdin.readline())

def get_float():
    return float(sys.stdin.readline())

def get_str():
    return input()

def main():
    results = []
    while True:
        n = get_int()
        if n == 0:
            break
        a = get_str_list()
        answer = None
        for i in range(n):
            if a[i] == 'x':
                if i > 0 and a[i-1] == 'x':
                    answer = 'none'
                    break
            else:
                a[i] = int(a[i])
                if i > 0 and a[i-1] != 'x':
                    if i % 2 == 0:
                        if a[i-1] <= a[i]:
                            answer = 'none'
                            break
                    else:
                        if a[i-1] >= a[i]:
                            answer = 'none'
                            break
        if answer is not None:
            results.append(answer)
            continue
        max_value = -inf
        min_value = inf
        for i in range(n):
            if a[i] != 'x':
                continue
            if i % 2 == 0:
                if i > 0 and a[i-1] != 'x':
                    min_value = min(min_value, a[i-1] - 1)
                if i < n-1 and a[i+1] != 'x':
                    min_value = min(min_value, a[i+1] - 1)
            else:
                if i > 0 and a[i-1] != 'x':
                    max_value = max(max_value, a[i-1] + 1)
                if i < n-1 and a[i+1] != 'x':
                    max_value = max(max_value, a[i+1] + 1)
        if max_value == min_value:
            results.append(max_value)
        elif max_value == -inf or min_value == inf:
            results.append('ambiguous')
        elif max_value > min_value:
            results.append('none')
        else:
            results.append('ambiguous')
    return '\n'.join(str(x) for x in results)

print(main())