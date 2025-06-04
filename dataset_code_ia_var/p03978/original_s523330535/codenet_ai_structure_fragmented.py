import sys
from collections import deque

def query(s1, s2):
    print("{0}\n{1}".format("".join(s1), "".join(s2)))
    sys.stdout.flush()
    return raw_input()

def get_initial_patterns():
    return [(".", "."), (".", "#"), ("#", "."), ("#", "#")]

def read_input_numbers():
    return map(int, raw_input().split())

def filter_valid_patterns(dss):
    tmp_dss = []
    for ds in dss:
        res = query([ds[0]], [ds[1]])
        if res == "T":
            tmp_dss.append(ds)
    return tmp_dss

def initialize_deques(ds):
    return deque(ds[0]), deque(ds[1])

def try_extend_right(dss, s1, s2):
    for ds1, ds2 in dss:
        s1.append(ds1)
        s2.append(ds2)
        res = query(s1, s2)
        if res == "end":
            return True, False
        if res == "T":
            return False, True
        s1.pop()
        s2.pop()
    return False, False

def extend_right_loop(dss, s1, s2, max_iter=420):
    for _ in xrange(max_iter):
        ended, found = try_extend_right(dss, s1, s2)
        if ended:
            return True
        if not found:
            break
    return False

def try_extend_left(dss, s1, s2):
    for ds1, ds2 in dss:
        s1.appendleft(ds1)
        s2.appendleft(ds2)
        res = query(s1, s2)
        if res == "end":
            return True, False
        if res == "T":
            return False, True
        s1.popleft()
        s2.popleft()
    return False, False

def extend_left_loop(dss, s1, s2, max_iter=420):
    for _ in xrange(max_iter):
        ended, found = try_extend_left(dss, s1, s2)
        if ended:
            return True
        if not found:
            break
    return False

def solve():
    dss = get_initial_patterns()
    _ = read_input_numbers()
    dss = filter_valid_patterns(dss)
    s1, s2 = initialize_deques(dss[0])
    if extend_right_loop(dss, s1, s2):
        return
    if extend_left_loop(dss, s1, s2):
        return

solve()