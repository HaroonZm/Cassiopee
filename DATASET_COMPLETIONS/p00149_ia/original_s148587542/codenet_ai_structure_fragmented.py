def init_lr():
    return [0 for _ in range(8)]

def read_input():
    try:
        return map(float, input().split())
    except:
        return None

def analyze_value_a(value):
    if value >= 1.1:
        return 0
    elif value >= 0.6:
        return 2
    elif value >= 0.2:
        return 4
    else:
        return 6

def analyze_value_b(value):
    if value >= 1.1:
        return 1
    elif value >= 0.6:
        return 3
    elif value >= 0.2:
        return 5
    else:
        return 7

def increment_lr(lr, index):
    lr[index] += 1

def print_results(lr):
    print(lr[0], lr[1])
    print(lr[2], lr[3])
    print(lr[4], lr[5])
    print(lr[6], lr[7])

def main():
    lr = init_lr()
    while True:
        values = read_input()
        if values is None:
            break
        a, b = values
        index_a = analyze_value_a(a)
        index_b = analyze_value_b(b)
        increment_lr(lr, index_a)
        increment_lr(lr, index_b)
    print_results(lr)

main()