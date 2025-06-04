def read_input():
    return input(), input()

def get_length(s):
    return len(s)

def calc_repeat_factor(len_s, len_t):
    return ((len_t + len_s - 1) // len_s) * 2

def extend_string(s, factor):
    return s * factor

def compute_hash_arr(s, base, mod):
    hash_arr = [0]
    for c in s:
        hash_arr.append((hash_arr[-1] * base + ord(c) - 97) % mod)
    return hash_arr

def compute_hash_val(t, base, mod):
    hash_val = 0
    for c in t:
        hash_val = (hash_val * base + ord(c) - 97) % mod
    return hash_val

def pow_mod(base, exp, mod):
    return pow(base, exp, mod)

def check_matches(hash_s, hash_t, base, mod, len_t, len0):
    return [is_match(hash_s, i, hash_t, base, mod, len_t) for i in range(len0)]

def is_match(hash_s, i, hash_t, base, mod, len_t):
    left = hash_s[i + len_t]
    right = (hash_s[i] * pow_mod(base, len_t, mod)) % mod
    return (left - right) % mod == hash_t

def initialize_visited(len0):
    return [-1] * len0

def find_max_chain(ok, len0, len_t):
    ret = 0
    visited = initialize_visited(len0)
    for i in range(len0):
        if ok[i] and visited[i] == -1:
            cnt = process_chain(i, ok, visited, len0, len_t)
            if cnt == -1:
                return -1
            visited[i] = cnt
            ret = max(ret, cnt)
    return ret

def process_chain(start, ok, visited, len0, len_t):
    j = start
    count = 0
    while ok[j]:
        if visited[j] != -1:
            count += visited[j]
            break
        count += 1
        visited[j] = 1
        j = next_index(j, len_t, len0)
        if has_cycle(j, start):
            return -1
    return count

def next_index(j, len_t, len0):
    return (j + len_t) % len0

def has_cycle(j, start):
    return j == start

def main():
    S, T = read_input()
    len0 = get_length(S)
    len_t = get_length(T)
    base = 26
    MOD = 2 ** 31 + 7

    rep = calc_repeat_factor(len0, len_t)
    S_ext = extend_string(S, rep)

    hashS = compute_hash_arr(S_ext, base, MOD)
    hashT = compute_hash_val(T, base, MOD)

    ok = check_matches(hashS, hashT, base, MOD, len_t, len0)
    
    ret = find_max_chain(ok, len0, len_t)
    print(ret)

main()