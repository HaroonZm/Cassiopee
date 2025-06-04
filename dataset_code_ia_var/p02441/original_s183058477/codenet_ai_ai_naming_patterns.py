if __name__ == '__main__':

    input_list_length = int(input())
    input_list_values = list(map(int, input().split()))

    query_count = int(input())

    for query_index in range(query_count):
        query_begin, query_end, query_value = map(int, input().split())
        sublist = input_list_values[query_begin:query_end]
        value_count = sublist.count(query_value)
        print(value_count)