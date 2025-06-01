def read_dimensions():
    return map(int, input().split())

def read_field(n):
    field = []
    for _ in range(n):
        field.append(list(str(input())))
    return field

def count_w_couplings(field, n):
    W_num = []
    W_cou = 0
    for k in range(n):
        W_cou += field[k].count('B') + field[k].count('R')
        W_num.append(W_cou)
    return W_num

def count_b_couplings(field, n):
    B_num = []
    B_cou = 0
    for k in range(n):
        B_cou += field[k].count('W') + field[k].count('R')
        B_num.append(B_cou)
    return B_num

def count_r_couplings(field, n):
    R_num = []
    R_cou = 0
    for k in range(n):
        R_cou += field[k].count('B') + field[k].count('W')
        R_num.append(R_cou)
    return R_num

def calculate_combinations(n, W_num, B_num, R_num):
    ans_lis = []
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            val = W_num[i - 1] + B_num[j - 1] - B_num[i - 1] + R_num[n - 1] - R_num[j - 1]
            ans_lis.append(val)
    return ans_lis

def find_min_value(ans_lis):
    return min(ans_lis)

def main():
    n, m = read_dimensions()
    field = read_field(n)
    W_num = count_w_couplings(field, n)
    B_num = count_b_couplings(field, n)
    R_num = count_r_couplings(field, n)
    ans_lis = calculate_combinations(n, W_num, B_num, R_num)
    print(find_min_value(ans_lis))

main()