def read_input():
    return list(map(int, input().split()))

def is_negative(x):
    return x < 0

def compute_q_negative(x, d):
    return (x // d) * -1

def compute_q_positive(x, d):
    return x // d

def should_use_first_branch(k, q):
    return k < q

def compute_x_neg_first_branch(x, d, k):
    return x + d * k

def compute_ak(k, q):
    return (k - q) % 2

def compute_x_neg_second_branch(x, d, q, ak):
    return x + d * q - d * ak

def compute_x_pos_first_branch(x, d, k):
    return x - d * k

def compute_x_pos_second_branch(x, d, q, ak):
    return x - d * q - d * ak

def main():
    x, k, d = read_input()
    if is_negative(x):
        q = compute_q_negative(x, d)
        if should_use_first_branch(k, q):
            x = compute_x_neg_first_branch(x, d, k)
        else:
            ak = compute_ak(k, q)
            x = compute_x_neg_second_branch(x, d, q, ak)
    else:
        q = compute_q_positive(x, d)
        if should_use_first_branch(k, q):
            x = compute_x_pos_first_branch(x, d, k)
        else:
            ak = compute_ak(k, q)
            x = compute_x_pos_second_branch(x, d, q, ak)
    print(abs(x))

main()