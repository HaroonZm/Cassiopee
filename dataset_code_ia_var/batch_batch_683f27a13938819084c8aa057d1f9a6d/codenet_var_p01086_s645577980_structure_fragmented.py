def read_input():
    return int(input())

def read_line_length():
    return len(input())

def read_lines_lengths(n):
    return [read_line_length() for _ in range(n)]

def pattern():
    return [5, 7, 5, 7, 7]

def update_ans(ans, value):
    return min(ans, value)

def process_window(w, a, n):
    ans = n + 1
    for i in range(n):
        k, s = 0, 0
        current_result = process_inner_window(w, a, n, i, k, s)
        if current_result is not None:
            ans = update_ans(ans, current_result)
    return ans

def process_inner_window(w, a, n, i, k, s):
    for j in range(i, n):
        s, k, found = process_element(w, a, j, k, s)
        if found:
            return i + 1
        if k == -1:
            break
    return None

def process_element(w, a, j, k, s):
    s += w[j]
    if k < 5 and s == a[k]:
        s = 0
        k += 1
    elif k < 5 and s > a[k]:
        k = -1
    if k == 5:
        return s, k, True
    if k == -1:
        return s, k, False
    return s, k, False

def main_loop():
    while True:
        n = read_input()
        if n == 0:
            break
        w = read_lines_lengths(n)
        a = pattern()
        ans = process_window(w, a, n)
        print(ans)

main_loop()