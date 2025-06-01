def get_input():
    return input()

def ord_letter(letter):
    return ord(letter)

def get_base():
    return ord('A')

def compute_offset(ord_letter_value, base):
    return ord_letter_value - base

def compute_rotated_offset(offset, n):
    return (offset - n) % 26

def compute_rotated_ord(base, rotated_offset):
    return base + rotated_offset

def chr_from_ord(ord_value):
    return chr(ord_value)

def process_letter(letter, n):
    base = get_base()
    ord_val = ord_letter(letter)
    offset = compute_offset(ord_val, base)
    rotated_offset = compute_rotated_offset(offset, n)
    rotated_ord_val = compute_rotated_ord(base, rotated_offset)
    return chr_from_ord(rotated_ord_val)

def rot_n(s, n):
    answer = ''
    for letter in s:
        answer += process_letter(letter, n)
    return answer

def main():
    x = get_input()
    result = rot_n(x, 3)
    print(result)

main()