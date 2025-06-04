import sys
input_stream = sys.stdin.readline

def process_queries():
    string_source = input_stream()
    string_target = input_stream()
    number_queries = int(input_stream())

    length_source = len(string_source)
    length_target = len(string_target)
    prefix_count_source = [0] * (length_source + 1)
    prefix_count_target = [0] * (length_target + 1)

    for index_source in range(1, length_source + 1):
        prefix_count_source[index_source] = prefix_count_source[index_source - 1] + (string_source[index_source - 1] == "A")
    for index_target in range(1, length_target + 1):
        prefix_count_target[index_target] = prefix_count_target[index_target - 1] + (string_target[index_target - 1] == "A")

    for _ in range(number_queries):
        src_left, src_right, tgt_left, tgt_right = map(int, input_stream().split())
        count_source = prefix_count_source[src_right] - prefix_count_source[src_left - 1] + src_right - src_left + 1
        count_target = prefix_count_target[tgt_right] - prefix_count_target[tgt_left - 1] + tgt_right - tgt_left + 1
        if count_source % 3 == count_target % 3:
            print("YES")
        else:
            print("NO")

process_queries()