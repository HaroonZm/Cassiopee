def main():
    MODULO_CONSTANT = 1000000007

    source_string = input()
    target_subsequence = input()

    source_length = len(source_string)
    target_length = len(target_subsequence)

    count_subsequences = [
        [0 for index_target in range(target_length + 1)]
        for index_source in range(source_length + 1)
    ]

    count_subsequences[0][0] = 1

    for index_source in range(source_length):
        for index_target in range(target_length - 1, -1, -1):
            count_subsequences[index_source + 1][index_target] += count_subsequences[index_source][index_target]
            count_subsequences[index_source + 1][index_target] %= MODULO_CONSTANT

            if source_string[index_source] == target_subsequence[index_target]:
                count_subsequences[index_source + 1][index_target + 1] += count_subsequences[index_source][index_target]
                count_subsequences[index_source + 1][index_target + 1] %= MODULO_CONSTANT

    total_subsequence_count = 0

    for index_source in range(source_length + 1):
        total_subsequence_count += count_subsequences[index_source][target_length]

    print(total_subsequence_count % MODULO_CONSTANT)

if __name__ == "__main__":
    main()