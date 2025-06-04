def get_input():
    return input()

def to_int(s):
    return int(s)

def to_int_list(s):
    return list(map(int, s.split()))

def append_zero(lst):
    lst.append(0)
    return lst

def init_ans():
    return 1

def init_count():
    return 0

def is_one(x):
    return x == 1

def update_ans(count, ans):
    if count >= ans:
        return count + 1
    return ans

def recursive_one_count(data, i, count, ans_obj):
    count = increment_count(count)
    if has_next_one(data, i):
        recursive_one_count(data, i+1, count, ans_obj)
    else:
        ans_obj[0] = update_ans(count, ans_obj[0])

def increment_count(count):
    return count + 1

def has_next_one(data, i):
    return is_one(data[i+1])

def process_index(data, i, ans_obj):
    count = init_count()
    if is_one(data[i]):
        recursive_one_count(data, i, count, ans_obj)

def process_data(N, data, ans_obj):
    for i in range(N):
        process_index(data, i, ans_obj)

def main():
    N = to_int(get_input())
    data = to_int_list(get_input())
    data = append_zero(data)
    ans_obj = [init_ans()]
    process_data(N, data, ans_obj)
    print(ans_obj[0])

main()