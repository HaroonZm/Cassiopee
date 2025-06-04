n = int(input())
digits = list(map(int, input().split()))

def is_subsequence(num_str, digits):
    idx = 0
    for d in digits:
        if d == int(num_str[idx]):
            idx += 1
            if idx == len(num_str):
                return True
    return False

i = 0
while True:
    if not is_subsequence(str(i), digits):
        print(i)
        break
    i += 1