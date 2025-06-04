def update_f3_values(a, b, c):
    return (a + b + c + 1) % 100000007, a, b

def f3_iterate_once(a, b, c):
    return update_f3_values(a, b, c)

def f3_loop_body(a, b, c):
    return f3_iterate_once(a, b, c)

def f3_inner_loop(n):
    a = b = c = 0
    for _ in range(n):
        a, b, c = f3_loop_body(a, b, c)
    return a

def f3(n):
    return f3_inner_loop(n)

def update_f5_values(a, b, c, d, e):
    return (a + b + c + d + e + 1) % 100000007, a, b, c, d

def f5_iterate_once(a, b, c, d, e):
    return update_f5_values(a, b, c, d, e)

def f5_loop_body(a, b, c, d, e):
    return f5_iterate_once(a, b, c, d, e)

def f5_inner_loop(n):
    a = b = c = d = e = 0
    for _ in range(n):
        a, b, c, d, e = f5_loop_body(a, b, c, d, e)
    return a

def f5(n):
    return f5_inner_loop(n)

def process_sequence(ans, num, cnt):
    if num in "80":
        return ans * f3(cnt) % 100000007
    else:
        return ans * f5(cnt) % 100000007

def handle_char(ans, num, cnt, n):
    if n == num:
        return ans, num, cnt + 1
    else:
        ans = process_sequence(ans, num, cnt)
        return ans, n, 1

def process_string(s):
    ans = 1
    num = "_"
    cnt = 1
    for n in s + "_":
        ans, num, cnt = handle_char(ans, num, cnt, n)
    return ans

def main_loop():
    while True:
        s = input()
        if s == "#":
            break
        result = process_string(s)
        print(result)

main_loop()