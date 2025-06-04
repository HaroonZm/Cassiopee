def init_lr():
    return [0 for _ in range(8)]

def read_input():
    try:
        return map(float, input().split())
    except:
        return None

def classify_value(val):
    if val >= 1.1:
        return 0
    elif val >= 0.6:
        return 2
    elif val >= 0.2:
        return 4
    else:
        return 6

def get_offset(is_b):
    # a: False -> offset 0, b: True -> offset 1
    return 1 if is_b else 0

def update_lr_single(lr, idx, is_b):
    lr[idx + get_offset(is_b)] += 1

def process_pair(lr, a, b):
    idx_a = classify_value(a)
    idx_b = classify_value(b)
    update_lr_single(lr, idx_a, False)
    update_lr_single(lr, idx_b, True)

def print_lr_rows(lr):
    print(lr[0], lr[1])
    print(lr[2], lr[3])
    print(lr[4], lr[5])
    print(lr[6], lr[7])

def loop_input(lr):
    while True:
        pair = read_input()
        if pair is None:
            break
        a, b = pair
        process_pair(lr, a, b)

def main():
    lr = init_lr()
    loop_input(lr)
    print_lr_rows(lr)

main()