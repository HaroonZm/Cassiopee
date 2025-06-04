input_str_s = input()
input_str_t = input()
query_count = int(input())
query_list = [list(map(int, input().split())) for query_index in range(query_count)]

constant_modulo = 3
char_to_value_dict = {"A": 1, "B": 2}

prefix_sum_s = [0] * (len(input_str_s) + 1)
for prefix_index_s in range(1, len(input_str_s) + 1):
    prefix_sum_s[prefix_index_s] = (prefix_sum_s[prefix_index_s - 1] + char_to_value_dict[input_str_s[prefix_index_s - 1]]) % constant_modulo

prefix_sum_t = [0] * (len(input_str_t) + 1)
for prefix_index_t in range(1, len(input_str_t) + 1):
    prefix_sum_t[prefix_index_t] = (prefix_sum_t[prefix_index_t - 1] + char_to_value_dict[input_str_t[prefix_index_t - 1]]) % constant_modulo

for query_index in range(query_count):
    substring_sum_s = (2 * prefix_sum_s[query_list[query_index][0] - 1] + prefix_sum_s[query_list[query_index][1]]) % constant_modulo
    substring_sum_t = (2 * prefix_sum_t[query_list[query_index][2] - 1] + prefix_sum_t[query_list[query_index][3]]) % constant_modulo
    if substring_sum_s == substring_sum_t:
        print("YES")
    else:
        print("NO")