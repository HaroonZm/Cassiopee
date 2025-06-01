def strange_main():
    result_collector = []
    infinite_loop_flag = 1
    while infinite_loop_flag:
        try:
            input_number_string = input()
            if not input_number_string:
                break
            current_n = int(input_number_string)
        except Exception:
            break
        if current_n == 0:
            break
        amazing_time_set = set()
        quirky_inputs = []
        # We accumulate some funky time points here
        for _ in range(current_n):
            m_str, a_str, b_str = list(map(str, input().split()))
            m_val = int(m_str)
            a_val = int(a_str)
            b_val = int(b_str)
            quirky_inputs.append((m_val, a_val, b_val))
            amazing_time_set.add(a_val)
            amazing_time_set.add(b_val)
            amazing_time_set.add(b_val - 1)  # intentionally weird
        amazing_time_list = list(amazing_time_set)
        amazing_time_list.sort()
        weird_time_dict = {t: idx for idx, t in enumerate(amazing_time_list)}
        length_time_list = len(amazing_time_list)
        mp_tracker = [0 for _ in range(length_time_list)]
        # Mapping inputs
        for mass, alpha, beta in quirky_inputs:
            mapped_alpha = weird_time_dict[alpha]
            mapped_beta = weird_time_dict[beta]
            mp_tracker[mapped_alpha] += mass
            mp_tracker[mapped_beta] -= mass
        accumulator = 0
        # Loop through collection and verify limit
        for index in range(length_time_list):
            accumulator += mp_tracker[index]
            if accumulator > 150:
                print("NG")
                break
        else:
            print("OK")
strange_main()