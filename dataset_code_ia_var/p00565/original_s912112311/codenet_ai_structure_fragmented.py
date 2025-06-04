def read_input():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def is_one(value):
    return value == 1

def increment_counter(counter):
    return counter + 1

def reset_counter():
    return 0

def update_maximum(current_max, counter):
    if current_max <= counter:
        return counter
    return current_max

def process_list(a):
    mx = 0
    cnt = 0
    for value in a:
        if is_one(value):
            cnt = increment_counter(cnt)
            mx = update_maximum(mx, cnt)
        else:
            cnt = reset_counter()
    return mx

def add_one(value):
    return value + 1

def main():
    n = read_input()
    a = read_list()
    longest = process_list(a)
    result = add_one(longest)
    print(result)

main()