import sys

def read_input():
    return sys.stdin

def is_termination_line(line):
    return line == '-1\n'

def to_int(s):
    return int(s)

def get_iterations(e):
    return max(0, to_int(e)-1)

def create_list_for_loop(n):
    return [0]*n

def initial_complex():
    return 1

def unit_complex(z):
    return 1j * z

def vector_length(z):
    return abs(z)

def next_complex(z):
    d = unit_complex(z)
    d_abs = vector_length(d)
    return z + d / d_abs

def iterate(z, n):
    for _ in create_list_for_loop(n):
        z = next_complex(z)
    return z

def extract_real(z):
    return z.real

def extract_imag(z):
    return z.imag

def print_value(v):
    print(v)

def process_line(e):
    z = initial_complex()
    n = get_iterations(e)
    z = iterate(z, n)
    real_part = extract_real(z)
    imag_part = extract_imag(z)
    print_value(real_part)
    print_value(imag_part)

def main():
    for e in read_input():
        if is_termination_line(e):
            break
        process_line(e)

main()