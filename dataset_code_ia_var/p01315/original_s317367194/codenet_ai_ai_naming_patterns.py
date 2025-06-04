while True:
    num_entries = int(input())
    if num_entries == 0:
        break

    entry_list = []
    for _ in range(num_entries):
        input_values = input().split()
        param_label = input_values[0]
        param_p, param_a, param_b, param_c, param_d, param_e, param_f, param_s, param_m = map(int, input_values[1:])
        total_time = param_a + param_b + param_c + param_m * (param_d + param_e)
        total_money = param_m * param_f * param_s - param_p
        entry_score = total_money / total_time
        entry_list.append([param_label, entry_score])

    entry_list.sort(key=lambda entry: entry[0])
    entry_list.sort(key=lambda entry: -entry[1])
    for idx in range(num_entries):
        print(entry_list[idx][0])
    print('#')