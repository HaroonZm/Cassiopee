def get_input():
    return float(input())

def initialize_sum():
    return 0

def initialize_retu(a):
    return 3 * a

def update_retu(retu, i):
    if i % 2 == 0:
        return retu / 3
    else:
        return retu * 2

def update_sum(current_sum, retu):
    return current_sum + retu

def process_loop(a):
    Sum = initialize_sum()
    retu = initialize_retu(a)
    for i in range(10):
        retu = update_retu(retu, i)
        Sum = update_sum(Sum, retu)
    return Sum

def main():
    while True:
        try:
            a = get_input()
            result = process_loop(a)
            print(result)
        except EOFError:
            break

main()