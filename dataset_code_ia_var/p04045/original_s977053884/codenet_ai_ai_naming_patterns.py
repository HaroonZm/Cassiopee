num_target, num_forbidden = map(int, input().split())
forbidden_digits_list = list(map(int, input().split()))

def is_valid_number():
    for idx_forbidden_digit in range(num_forbidden):
        if str(num_target).find(str(forbidden_digits_list[idx_forbidden_digit])) >= 0:
            return False
    return True

for idx_candidate in range(100000):
    if is_valid_number():
        print(num_target)
        break
    else:
        num_target += 1