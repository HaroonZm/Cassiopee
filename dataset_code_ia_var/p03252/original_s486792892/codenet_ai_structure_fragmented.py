import math

def read_input():
    return input(), input()

def init_letter_lists():
    return [], [], [], []

def update_letter_count(letter, alp, num):
    idx = find_index(letter, alp)
    if idx != -1:
        num[idx] += 1
    else:
        alp.append(letter)
        num.append(1)

def find_index(letter, alp):
    for idx, char in enumerate(alp):
        if char == letter:
            return idx
    return -1

def process_step(i, s, t, alp_s, alp_t, num_s, num_t):
    process_letter(s[i], alp_s, num_s)
    process_letter(t[i], alp_t, num_t)
    return num_s, num_t

def process_letter(char, alp, num):
    cnt = 0
    for j in alp:
        if char == j:
            num[cnt] += 1
        cnt += 1
    if not char in alp:
        alp.append(char)
        num.append(1)

def print_and_quit(msg):
    print(msg)
    quit()

def check_num_lists(num_s, num_t):
    if num_s != num_t:
        print_and_quit('No')

def process_strings(s, t):
    alp_s, alp_t, num_s, num_t = init_letter_lists()
    for i in range(len(s)):
        process_letter(s[i], alp_s, num_s)
        process_letter(t[i], alp_t, num_t)
        check_num_lists(num_s, num_t)
    print('Yes')

def main():
    s, t = read_input()
    process_strings(s, t)

main()