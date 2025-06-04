def read_ints():
    return map(int, input().rstrip().split())

def main():
    num_items, max_weight = read_ints()
    item_list = [list(read_ints()) for item_idx in range(num_items)]

    dp_table = [0] * (max_weight + 1)

    def decompose_item(item):
        value, weight, count = item
        counts = []
        power = 1
        remaining = count
        while power <= remaining:
            counts.append(power)
            remaining -= power
            power <<= 1
        if remaining:
            counts.append(remaining)
        return value, weight, counts

    decomposed_items = map(decompose_item, item_list)

    for item_value, item_weight, item_counts in decomposed_items:
        for count in item_counts:
            total_value = item_value * count
            total_weight = item_weight * count
            for curr_capacity in range(max_weight, total_weight - 1, -1):
                prev_capacity = curr_capacity - total_weight
                candidate_value = dp_table[prev_capacity] + total_value
                if dp_table[curr_capacity] < candidate_value:
                    dp_table[curr_capacity] = candidate_value
    print(dp_table[max_weight])

if __name__ == "__main__":
    main()