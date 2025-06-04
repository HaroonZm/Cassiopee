flag = False

def dbg(a, b=None):
    _dbg_core(a, b)

def _dbg_core(a, b):
    if flag:
        print(a, b)

def hante(arr, num):
    return _hante_logic(arr, num)

def _hante_logic(arr, num):
    sum_val = _init_sum()
    for i in range(_get_length(arr)):
        sum_val = _increment_sum(sum_val, arr, i)
        if _is_equal(sum_val, num):
            dbg((True, i), arr)
            return _return_true(i)
        if _is_greater(sum_val, num):
            dbg((False, None), arr)
            return _return_false()
    dbg((False, None), arr)
    return _return_false()

def _init_sum():
    return 0

def _get_length(arr):
    return len(arr)

def _increment_sum(sum_val, arr, i):
    return sum_val + arr[i]

def _is_equal(a, b):
    return a == b

def _is_greater(a, b):
    return a > b

def _return_true(i):
    return (True, i+1)

def _return_false():
    return (False, None)

def main_loop():
    while True:
        n = _input_n()
        if _zero_check(n):
            break
        _process_n(n)

def _input_n():
    return int(input())

def _zero_check(n):
    return n == 0

def _process_n(n):
    mojisuu = _init_mojisuu()
    w = _create_w_list(n)
    mojisuu, w = _fill_w_and_mojisuu(n, mojisuu, w)
    _search_pattern(mojisuu, w)

def _init_mojisuu():
    return 0

def _create_w_list(n):
    return ["" for _ in range(n)]

def _fill_w_and_mojisuu(n, mojisuu, w):
    for i in range(n):
        x = _get_input_length()
        w[i] = x
        mojisuu = _add_mojisuu(mojisuu, x)
    return mojisuu, w

def _get_input_length():
    return len(input())

def _add_mojisuu(mojisuu, x):
    return mojisuu + x

def _search_pattern(mojisuu, w):
    start = _init_start()
    while start < mojisuu:
        indices = _get_indices(start, w)
        if indices:
            break
        start = _increment_start(start)
    _print_result(start)

def _init_start():
    return 0

def _get_indices(start, w):
    h1 = hante(w[start:], 5)
    if not h1[0]:
        return None
    h2 = hante(w[start + h1[1]:], 7)
    if not h2[0]:
        return None
    h3 = hante(w[start + h1[1] + h2[1]:], 5)
    if not h3[0]:
        return None
    h4 = hante(w[start + h1[1] + h2[1] + h3[1]:], 7)
    if not h4[0]:
        return None
    h5 = hante(w[start + h1[1] + h2[1] + h3[1] + h4[1]:], 7)
    if not h5[0]:
        return None
    return (h1, h2, h3, h4, h5)

def _increment_start(start):
    return start + 1

def _print_result(start):
    print(start + 1)

main_loop()