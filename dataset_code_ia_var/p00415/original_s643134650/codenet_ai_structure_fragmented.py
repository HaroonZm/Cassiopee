import heapq
from _heapq import heappush, heappop

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

class Info:
    def __init__(self, arg_num, arg_loc):
        self.num = arg_num
        self.loc = arg_loc

    def __lt__(self, another):
        if self.num != another.num:
            return self.num > another.num
        else:
            return self.loc < another.loc

def read_input():
    return map(int, input().split())

def read_table(N):
    return list(map(int, input().split()))

def initialize_queue():
    return []

def initialize_variables(N, K):
    rest = N
    need_out = N - K
    out = 0
    return rest, need_out, out

def push_heap(Q, tmp, loc):
    heappush(Q, Info(tmp, loc))

def should_continue(out, rest, need_out):
    return out + rest >= need_out

def pop_min_heap(Q):
    return heappop(Q)

def print_num(num, append_newline=False):
    if append_newline:
        print("")
    else:
        print("%d" % (num), end="")

def remove_smaller_locs(Q, ref_loc):
    while len(Q) > 0 and Q[0].loc <= ref_loc:
        heappop(Q)

def process_loc(Q, table, rest, out, need_out, loc):
    tmp = table[loc]
    push_heap(Q, tmp, loc)
    rest -= 1
    if should_continue(out, rest, need_out):
        return rest, out, False
    info = pop_min_heap(Q)
    print_num(info.num)
    remove_smaller_locs(Q, info.loc)
    out += 1
    return rest, out, True

def process_all(N, K, table):
    Q = initialize_queue()
    rest, need_out, out = initialize_variables(N, K)
    for loc in range(N):
        rest, out, did_output = process_loc(Q, table, rest, out, need_out, loc)
    print_num(0, append_newline=True)  # Actually just prints newline, intentional misuse to reuse

def main():
    N, K = read_input()
    table = read_table(N)
    process_all(N, K, table)

main()