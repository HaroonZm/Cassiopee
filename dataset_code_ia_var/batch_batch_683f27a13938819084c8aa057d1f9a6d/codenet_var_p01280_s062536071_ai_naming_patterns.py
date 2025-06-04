import sys
io_read = sys.stdin.readline
io_write = sys.stdout.write

def math_gcd(val_a, val_b):
    while val_b:
        val_a, val_b = val_b, val_a % val_b
    return val_a

def math_lcm(val_a, val_b):
    return val_a // math_gcd(val_a, val_b) * val_b

def process_case():
    input_n = int(io_read())
    if input_n == 0:
        return False

    skip_cycle_list = [13, 17, 19, 23]
    cycle_buckets = [ [0] * idx for idx in range(25) ]
    result_vector = []
    for idx_case in range(input_n):
        parts = list(map(int, io_read().split()))
        cycle_len, shift_amt = parts[0], parts[1]
        source_data = parts[2:]
        rotated_data = source_data[shift_amt:] + source_data[:shift_amt]
        current_bucket = cycle_buckets[cycle_len]
        for idx_elem in range(cycle_len):
            current_bucket[idx_elem] += rotated_data[idx_elem]
    lcm_val = 13860
    score_vector = [0] * lcm_val
    for idx_cycle in range(1, 25):
        if idx_cycle in skip_cycle_list:
            continue
        if idx_cycle <= 12:
            bucket_src = cycle_buckets[idx_cycle]
            bucket_dst = cycle_buckets[2 * idx_cycle]
            for idx_elem in range(2 * idx_cycle):
                bucket_dst[idx_elem] += bucket_src[idx_elem % idx_cycle]
        else:
            bucket_src = cycle_buckets[idx_cycle]
            if idx_cycle == 16:
                for idx_elem in range(8):
                    bucket_src[idx_elem] = max(bucket_src[idx_elem + 8], bucket_src[idx_elem])
                bucket_dst = cycle_buckets[24]
                for idx_elem in range(24):
                    bucket_dst[idx_elem] += bucket_src[idx_elem % 8]
            elif idx_cycle == 24:
                for idx_elem in range(12):
                    bucket_src[idx_elem] = max(bucket_src[idx_elem + 12], bucket_src[idx_elem])
                for idx_elem in range(lcm_val):
                    score_vector[idx_elem] += bucket_src[idx_elem % 12]
            else:
                for idx_elem in range(lcm_val):
                    score_vector[idx_elem] += bucket_src[idx_elem % idx_cycle]
    result_max = max(score_vector)
    for cycle_idx in skip_cycle_list:
        result_max += max(cycle_buckets[cycle_idx])
    io_write("%d\n" % result_max)
    return True

while process_case():
    pass