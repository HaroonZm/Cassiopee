def read_dimensions():
    return map(int, input().split())

def read_line():
    return input()

def is_c(char):
    return char == 'c'

def append_zero(ans):
    ans.append(0)

def append_minus_one(ans):
    ans.append(-1)

def find_distance_to_c(s, idx):
    for distance in range(1, idx + 1):
        if is_c(s[idx - distance]):
            return distance
    return -1

def process_character(ans, s, i):
    if is_c(s[i]):
        append_zero(ans)
    elif i == 0:
        append_minus_one(ans)
    else:
        distance = find_distance_to_c(s, i)
        ans.append(distance)

def process_line(s):
    ans = []
    for i in range(len(s)):
        process_character(ans, s, i)
    return ans

def print_answer(ans):
    print(' '.join(map(str, ans)))

def main():
    h, w = read_dimensions()
    for _ in range(h):
        s = read_line()
        ans = process_line(s)
        print_answer(ans)

main()