def read_integer():
    return int(input())

def read_integers():
    return list(map(int, input().split()))

def increment_count(dictionary, key):
    try:
        dictionary[key] += 1
    except KeyError:
        dictionary[key] = 1

def count_elements(L):
    cnt = {}
    for l in L:
        increment_count(cnt, l)
    return cnt

def get_element_keys(dictionary):
    return list(dictionary.keys())

def check_key_exists(dictionary, key):
    try:
        dictionary[key]
        return True
    except KeyError:
        return False

def get_value(dictionary, key):
    return dictionary[key]

def check_counts_enough(countD, countT):
    keys = get_element_keys(countT)
    for i in keys:
        if not check_key_exists(countD, i):
            return False
        if get_value(countD, i) < get_value(countT, i):
            return False
    return True

def print_result(flag):
    if flag:
        print('YES')
    else:
        print('NO')

def main():
    N = read_integer()
    D = read_integers()
    M = read_integer()
    T = read_integers()
    countD = count_elements(D)
    countT = count_elements(T)
    flag = check_counts_enough(countD, countT)
    print_result(flag)

main()