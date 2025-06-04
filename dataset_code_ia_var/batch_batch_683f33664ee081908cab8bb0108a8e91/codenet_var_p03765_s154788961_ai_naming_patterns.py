import sys
input_stream = sys.stdin

sys.setrecursionlimit(10**5)

def read_int_map(): return map(int, input_stream.readline().split())
def read_int_zero_map(): return map(lambda x: int(x)-1, input_stream.readline().split())
def read_float_map(): return map(float, input_stream.readline().split())
def read_str_list(): return input_stream.readline().split()
def read_str(): return input_stream.readline().rstrip()
def read_char_list(): return list(read_str())
def read_int(): return int(input_stream.readline())
def read_float(): return float(input_stream.readline())

str_s = read_str()
str_t = read_str()
num_q = read_int()

prefix_a_s = [0]
prefix_b_s = [0]
prefix_a_t = [0]
prefix_b_t = [0]

for char_s in str_s:
    if char_s == "A":
        prefix_a_s.append(prefix_a_s[-1] + 1)
        prefix_b_s.append(prefix_b_s[-1])
    else:
        prefix_a_s.append(prefix_a_s[-1])
        prefix_b_s.append(prefix_b_s[-1] + 1)

for char_t in str_t:
    if char_t == "A":
        prefix_a_t.append(prefix_a_t[-1] + 1)
        prefix_b_t.append(prefix_b_t[-1])
    else:
        prefix_a_t.append(prefix_a_t[-1])
        prefix_b_t.append(prefix_b_t[-1] + 1)

for _ in range(num_q):
    idx_a, idx_b, idx_c, idx_d = read_int_map()

    count_a_s = prefix_a_s[idx_b] - prefix_a_s[idx_a-1]
    count_b_s = prefix_b_s[idx_b] - prefix_b_s[idx_a-1]

    count_a_t = prefix_a_t[idx_d] - prefix_a_t[idx_c-1]
    count_b_t = prefix_b_t[idx_d] - prefix_b_t[idx_c-1]

    norm_count_s = count_a_s + 2 * count_b_s
    norm_count_t = count_a_t + 2 * count_b_t

    if norm_count_s % 3 == norm_count_t % 3:
        print('YES')
    else:
        print('NO')