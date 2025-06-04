def get_input_n():
    return int(input())

def get_input_list():
    return list(map(int, input().split()))

def calc_sum(li):
    return sum(li)

def calc_length(li):
    return len(li)

def calc_kumi(lee):
    return lee // 2

def calc_tmp(li, kumi):
    def get_index(i):
        return 2 * (i - 1)
    def get_value(i):
        return 2 * li[get_index(i)]
    tmp = 0
    for i in range(1, kumi + 1):
        tmp += get_value(i)
    return tmp

def calc_last(s, tmp):
    return s - tmp

def get_last_element(li):
    return li[-1]

def calc_first(last_elem, last):
    return last_elem * 2 - last

def init_ans_li(first):
    return [first]

def append_to_ans(ans_li, l):
    last_val = ans_li[-1]
    ans_li.append(l * 2 - last_val)

def process_ans_li(li, first):
    ans_li = init_ans_li(first)
    for l in li:
        append_to_ans(ans_li, l)
    return ans_li

def remove_last(ans_li):
    ans_li.pop(-1)

def print_ans_li(ans_li):
    print(*ans_li)

def main():
    n = get_input_n()
    li = get_input_list()
    s = calc_sum(li)
    lee = calc_length(li)
    kumi = calc_kumi(lee)
    tmp = calc_tmp(li, kumi)
    last = calc_last(s, tmp)
    last_elem = get_last_element(li)
    first = calc_first(last_elem, last)
    ans_li = process_ans_li(li, first)
    remove_last(ans_li)
    print_ans_li(ans_li)

main()