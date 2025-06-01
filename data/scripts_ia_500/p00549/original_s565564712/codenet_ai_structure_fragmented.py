def read_int():
    return int(input())

def read_string():
    return input()

def update_j_count(c, j_cnt):
    if c == "J":
        return j_cnt + 1
    return j_cnt

def update_o_count_and_jo_cnt(c, o_cnt, j_cnt, jo_cnt):
    if c == "O":
        o_cnt += 1
        jo_cnt += j_cnt
    return o_cnt, jo_cnt

def update_i_counts_and_joi_cnt(c, i_cnt, o_cnt, oi_cnt, jo_cnt, joi_cnt):
    if c != "J" and c != "O":
        i_cnt += 1
        oi_cnt += o_cnt
        joi_cnt += jo_cnt
    return i_cnt, oi_cnt, joi_cnt

def append_accumulators(j_acc, o_acc, i_acc, j_cnt, o_cnt, i_cnt):
    j_acc.append(j_cnt)
    o_acc.append(o_cnt)
    i_acc.append(i_cnt)

def calculate_ji_cnt(n, j_acc, i_acc):
    max_val = 0
    total_i = i_acc[-1]
    for i in range(n):
        val = j_acc[i] * (total_i - i_acc[i])
        if val > max_val:
            max_val = val
    return max_val

def main():
    n = read_int()
    s = read_string()
    jo_cnt = 0
    oi_cnt = 0
    j_cnt = 0
    o_cnt = 0
    i_cnt = 0
    joi_cnt = 0
    j_acc = []
    o_acc = []
    i_acc = []
    for c in s:
        j_cnt = update_j_count(c, j_cnt)
        o_cnt, jo_cnt = update_o_count_and_jo_cnt(c, o_cnt, j_cnt, jo_cnt)
        i_cnt, oi_cnt, joi_cnt = update_i_counts_and_joi_cnt(c, i_cnt, o_cnt, oi_cnt, jo_cnt, joi_cnt)
        append_accumulators(j_acc, o_acc, i_acc, j_cnt, o_cnt, i_cnt)
    ji_cnt = calculate_ji_cnt(n, j_acc, i_acc)
    print(joi_cnt + max(jo_cnt, oi_cnt, ji_cnt))

main()