def get_input():
    return int(input())

def initialize_sum():
    return 0

def can_use_unit(p, unit):
    return p >= unit

def calculate_unit(p, unit):
    return (p // unit) * unit

def deduct_unit(p, unit):
    return p - (p // unit) * unit

def update_sum(s, add):
    return s + add

def process_unit(p, s, unit):
    if can_use_unit(p, unit):
        add = calculate_unit(p, unit)
        s = update_sum(s, add)
        p = deduct_unit(p, unit)
    return p, s

def main():
    p = get_input()
    s = initialize_sum()
    for unit in [10000, 5000, 1000, 500]:
        p, s = process_unit(p, s, unit)
    print(s)

main()