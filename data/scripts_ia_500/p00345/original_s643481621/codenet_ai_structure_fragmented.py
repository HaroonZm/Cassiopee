from math import gcd

def read_input():
    return input()

def split_input(s):
    return s.split(".")

def has_repeating_part(s):
    return "(" in s

def find_parentheses_indices(y):
    da = y.index("(")
    db = y.index(")") - 1
    return da, db

def split_repeating_part(y):
    return y.split("(")

def length_repeating_part(b):
    return len(b) - 1

def form_a(x, ya):
    return int(x + ya)

def form_b(b):
    return int(b[:-1])

def compute_deco(a, b, da, db, lb):
    part1 = a * (10 ** db - 10 ** (db - lb))
    part2 = b * 10 ** da
    return part1 + part2

def compute_nume(da, db, lb):
    return 10 ** da * (10 ** db - 10 ** (db - lb))

def compute_division(deco, nume):
    return gcd(deco, nume)

def print_fraction(deco, nume, div):
    print(deco // div, nume // div, sep="/")

def process_repeating(x, y, s):
    da, db = find_parentheses_indices(y)
    ya, b = split_repeating_part(y)
    lb = length_repeating_part(b)
    a = form_a(x, ya)
    b = form_b(b)
    deco = compute_deco(a, b, da, db, lb)
    nume = compute_nume(da, db, lb)
    div = compute_division(deco, nume)
    print_fraction(deco, nume, div)

def process_non_repeating(x, y):
    da = len(y)
    a = int(x + y)
    deco = a
    nume = 10 ** da
    div = gcd(deco, nume)
    print_fraction(deco, nume, div)

def main():
    s = read_input()
    x, y = split_input(s)
    if has_repeating_part(s):
        process_repeating(x, y, s)
    else:
        process_non_repeating(x, y)

main()