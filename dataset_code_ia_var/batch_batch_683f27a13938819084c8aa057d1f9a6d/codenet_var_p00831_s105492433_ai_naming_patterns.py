import collections
import itertools
import sys

input_reader = sys.stdin.readline
output_writer = sys.stdout.write

def process_cases():
    string_count = int(input_reader())
    if string_count == 0:
        return False

    max_distance = int(input_reader())
    string_list = [input_reader().strip() for _ in range(string_count)]
    result_pairs = []

    def compute_edit_distance(str_a, str_b):
        len_a = len(str_a)
        len_b = len(str_b)
        inf_value = 10**18
        dp_table = [[inf_value] * (len_b + 1) for _ in range(len_a + 1)]
        dp_table[0][0] = 0
        for idx_a in range(len_a):
            for idx_b in range(len_b):
                curr_val = dp_table[idx_a][idx_b]
                if str_a[idx_a] == str_b[idx_b]:
                    dp_table[idx_a + 1][idx_b + 1] = min(dp_table[idx_a + 1][idx_b + 1], curr_val)
                else:
                    dp_table[idx_a + 1][idx_b + 1] = min(dp_table[idx_a + 1][idx_b + 1], curr_val + 1)
                dp_table[idx_a + 1][idx_b] = min(dp_table[idx_a + 1][idx_b], curr_val + 1)
                dp_table[idx_a][idx_b + 1] = min(dp_table[idx_a][idx_b + 1], curr_val + 1)
            dp_table[idx_a + 1][len_b] = min(dp_table[idx_a + 1][len_b], dp_table[idx_a][len_b] + 1)
        for idx_b in range(len_b):
            dp_table[len_a][idx_b + 1] = min(dp_table[len_a][idx_b + 1], dp_table[len_a][idx_b] + 1)
        return dp_table[len_a][len_b]

    def is_similar(str_a, str_b):
        len_a = len(str_a)
        len_b = len(str_b)
        if abs(len_a - len_b) > max_distance:
            return False
        distance = compute_edit_distance(str_a, str_b)
        if distance <= max_distance:
            return True
        if distance == 2 and len_a == len_b:
            diff_indices = []
            diff_a = []
            diff_b = []
            for idx in range(len_a):
                if str_a[idx] != str_b[idx]:
                    diff_indices.append(idx)
                    diff_a.append(str_a[idx])
                    diff_b.append(str_b[idx])
            if len(diff_indices) == 2 and diff_indices[1] - diff_indices[0] == 1:
                diff_a.reverse()
                if diff_a == diff_b:
                    return True
        if max_distance == 2:
            if distance == 4 and len_a == len_b:
                diff_indices = []
                diff_a = []
                diff_b = []
                for idx in range(len_a):
                    if str_a[idx] != str_b[idx]:
                        diff_indices.append(idx)
                        diff_a.append(str_a[idx])
                        diff_b.append(str_b[idx])
                if len(diff_indices) == 4 and diff_indices[1] - diff_indices[0] == 1 and diff_indices[3] - diff_indices[2] == 1:
                    diff_a[0], diff_a[1] = diff_a[1], diff_a[0]
                    diff_a[2], diff_a[3] = diff_a[3], diff_a[2]
                    if diff_a == diff_b:
                        return True
            if distance == 3 and abs(len_a - len_b) < max_distance:
                seq_a = list(str_a)
                seq_b = list(str_b)
                la, lb = len_a, len_b
                if not la < lb:
                    la, lb = lb, la
                    seq_a, seq_b = seq_b, seq_a
                for swap1 in range(la - 1):
                    seq_a[swap1], seq_a[swap1 + 1] = seq_a[swap1 + 1], seq_a[swap1]
                    if compute_edit_distance(seq_a, seq_b) <= max_distance - 1:
                        return True
                    for swap2 in range(la - 1):
                        seq_a[swap2], seq_a[swap2 + 1] = seq_a[swap2 + 1], seq_a[swap2]
                        if seq_a == seq_b:
                            return True
                        seq_a[swap2], seq_a[swap2 + 1] = seq_a[swap2 + 1], seq_a[swap2]
                    seq_a[swap1], seq_a[swap1 + 1] = seq_a[swap1 + 1], seq_a[swap1]
        return False

    for idx_i in range(string_count):
        for idx_j in range(idx_i + 1, string_count):
            if is_similar(string_list[idx_i], string_list[idx_j]):
                pair = (string_list[idx_i], string_list[idx_j]) if string_list[idx_i] < string_list[idx_j] else (string_list[idx_j], string_list[idx_i])
                result_pairs.append(pair)

    result_pairs.sort()
    for string_pair in result_pairs:
        output_writer("%s,%s\n" % string_pair)
    output_writer("%d\n" % len(result_pairs))
    return True

while process_cases():
    pass