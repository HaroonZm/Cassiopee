def read_input():
    return map(int, raw_input().split())

def read_string():
    return raw_input()

def get_rolling_hash1(s):
    return create_rolling_hash(s, 13, 10**9+7)

def get_rolling_hash2(s):
    return create_rolling_hash(s, 17, 10**9+7)

def create_rolling_hash(s, base, MOD):
    h = initialize_hash_list(len(s))
    fill_hash_list(s, base, MOD, h)
    return build_rolling_hash_object(s, base, MOD, h)

def initialize_hash_list(length):
    return [0] * (length + 1)

def fill_hash_list(s, base, MOD, h):
    l = len(s)
    for i in xrange(l):
        h[i+1] = (h[i] * base + ord(s[i])) % MOD

def build_rolling_hash_object(s, base, MOD, h):
    obj = {}
    obj['s'] = s
    obj['l'] = len(s)
    obj['base'] = base
    obj['MOD'] = MOD
    obj['h'] = h
    obj['get'] = lambda l, r: get_hash_value(obj, l, r)
    return obj

def get_hash_value(obj, l, r):
    MOD = obj['MOD']
    base = obj['base']
    return ((obj['h'][r] - obj['h'][l] * pow(base, r-l, MOD) + MOD)) % MOD

def get_query():
    return raw_input()

def process_query(q, l, r):
    new_l, new_r = l, r
    if q == "R++":
        new_r += 1
    elif q == "R--":
        new_r -= 1
    elif q == "L++":
        new_l += 1
    else:
        new_l -= 1
    return new_l, new_r

def get_hashes(h1, h2, l, r):
    return (h1['get'](l, r), h2['get'](l, r))

def update_results(v, vs, ans):
    if v not in vs:
        vs.add(v)
        ans += 1
    return ans

def main():
    n, m = read_input()
    s = read_string()
    h1 = get_rolling_hash1(s)
    h2 = get_rolling_hash2(s)
    l = 0
    r = 1
    vs = set()
    ans = 0
    for _ in xrange(m):
        q = get_query()
        l, r = process_query(q, l, r)
        v = get_hashes(h1, h2, l, r)
        ans = update_results(v, vs, ans)
    print ans

main()