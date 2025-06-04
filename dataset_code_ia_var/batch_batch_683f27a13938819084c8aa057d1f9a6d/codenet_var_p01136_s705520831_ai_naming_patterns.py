while True:
    input_count = int(input())
    if input_count == 0:
        break
    digit_sets = [[] for _ in range(30)]
    for index_doc in range(input_count):
        doc_data = list(map(int, input().split()))
        for digit in doc_data[1:]:
            digit_sets[digit - 1].append(index_doc)
    doc_bitmasks = [1 << index for index in range(input_count)]
    for digit_index in range(30):
        for doc_i in digit_sets[digit_index]:
            for doc_j in digit_sets[digit_index]:
                doc_bitmasks[doc_i] |= doc_bitmasks[doc_j]
        full_mask = (1 << input_count) - 1
        if any(bitmask == full_mask for bitmask in doc_bitmasks):
            print(digit_index + 1)
            break
    else:
        print(-1)