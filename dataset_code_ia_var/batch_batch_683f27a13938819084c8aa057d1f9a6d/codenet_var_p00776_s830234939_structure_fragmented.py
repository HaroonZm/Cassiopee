def clear_ans(ans):
    ans.clear()

def clear_x(x):
    x.clear()

def get_alphabet():
    return ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","}"]

def get_empty_ans():
    return [""]

def remove_first_from_ans(ans):
    ans.pop()

def get_empty_x():
    return [0]

def remove_first_from_x(x):
    x.pop()

def uni(seq):
    return _uni_helper(seq)

def _uni_helper(seq):
    seen = set()
    return _uni_loop(seq, seen)

def _uni_loop(seq, seen):
    res = []
    for x in seq:
        if x not in seen:
            res.append(x)
            seen.add(x)
    return res

def is_prefix_equal(a, s):
    n = len(a)
    return a == s[0:n]

def replace_chars_once(a, w):
    for i in range(1, 26):
        a = a.replace(w[i], w[i-1], 1)
    return a

def check(a, s, w):
    modified = replace_chars_once(a, w)
    return is_prefix_equal(modified, s)

def append_to_ans_if_check(a, s, w, ans):
    if check(a, s, w):
        ans.append(a)

def is_done(n, a):
    return n == len(a)

def get_next_char(s, sz):
    return s[sz]

def append_next_char(a, s, sz):
    return a + get_next_char(s, sz)

def should_try_add_next(w, x, sz):
    return w[x[sz]] != "z"

def get_char_incremented(a, w, x, sz):
    return a + w[x[sz]+1]

def call_foo(t, n, s, w, ans, x):
    foo(t, n, s, w, ans, x)

def foo(a, n, s, w, ans, x):
    if is_done(n, a):
        append_to_ans_if_check(a, s, w, ans)
        return
    sz = len(a)
    t = append_next_char(a, s, sz)
    if check(t, s, w):
        call_foo(t, n, s, w, ans, x)
    if not should_try_add_next(w, x, sz):
        return
    t2 = get_char_incremented(a, w, x, sz)
    if check(t2, s, w):
        call_foo(t2, n, s, w, ans, x)

def process_x(s, w):
    x = get_empty_x()
    remove_first_from_x(x)
    for i in range(len(s)):
        for j in range(26):
            if w[j] == s[i]:
                x.append(j)
    return x

def output_ans(ans):
    ans.sort()
    if len(ans) <= 10:
        print(len(ans))
        for item in ans:
            print(item)
    else:
        print(len(ans))
        for i in range(5):
            print(ans[i])
        for i in range(5):
            print(ans[len(ans)-5+i])

def main_loop():
    w = get_alphabet()
    while True:
        s = raw_input()
        if s == "#":
            break
        ans = get_empty_ans()
        remove_first_from_ans(ans)
        x = process_x(s, w)
        foo("", len(s), s, w, ans, x)
        output_ans(ans)

main_loop()