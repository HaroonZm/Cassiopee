while True:
    try:
        input_n_m = raw_input().split()
        count_total, count_interval = map(int, input_n_m)
        if count_total == 0:
            break
        values_list = map(int, raw_input().split())
        values_sorted_desc = sorted(values_list, reverse=True)
        for idx in range(count_interval - 1, count_total, count_interval):
            values_sorted_desc[idx] = 0
        total_sum = sum(values_sorted_desc)
        print total_sum
    except:
        pass