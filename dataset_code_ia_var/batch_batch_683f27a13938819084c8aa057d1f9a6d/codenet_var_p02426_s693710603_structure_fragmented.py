def get_int():
    return int(input())

def get_ints():
    return list(map(int, input().split()))

def make_ret(input_list):
    return input_list

def build_retmask(ret):
    retmask = 0
    for i in range(1, ret[0] + 1):
        retmask += 1 << ret[i]
    return retmask

def build_masks(q):
    masks = []
    for _ in range(q):
        ret = make_ret(get_ints())
        masks.append(build_retmask(ret))
    return masks

def process_query_0(n, query):
    temp = 1 << query[1]
    if (n & temp) == 0:
        print(0)
    else:
        print(1)
    return n

def process_query_1(n, query, mask):
    return n | mask[query[1]]

def process_query_2(n, query, mask, MASK):
    return n & (~mask[query[1]] & MASK)

def process_query_3(n, query, mask):
    return n ^ mask[query[1]]

def process_query_4(n, query, mask):
    if n & mask[query[1]] == mask[query[1]]:
        print(1)
    else:
        print(0)
    return n

def process_query_5(n, query, mask):
    if n & mask[query[1]] > 0:
        print(1)
    else:
        print(0)
    return n

def process_query_6(n, query, mask):
    if n & mask[query[1]] == 0:
        print(1)
    else:
        print(0)
    return n

def process_query_7(n, query, mask):
    print(bin(n & mask[query[1]]).count("1"))
    return n

def process_query_8(n, query, mask):
    print(mask[query[1]] & n)
    return n

def process_query(n, query, mask, MASK):
    if query[0] == 0:
        n = process_query_0(n, query)
    elif query[0] == 1:
        n = process_query_1(n, query, mask)
    elif query[0] == 2:
        n = process_query_2(n, query, mask, MASK)
    elif query[0] == 3:
        n = process_query_3(n, query, mask)
    elif query[0] == 4:
        n = process_query_4(n, query, mask)
    elif query[0] == 5:
        n = process_query_5(n, query, mask)
    elif query[0] == 6:
        n = process_query_6(n, query, mask)
    elif query[0] == 7:
        n = process_query_7(n, query, mask)
    elif query[0] == 8:
        n = process_query_8(n, query, mask)
    return n

def process_queries(q, mask, MASK):
    n = 0
    for _ in range(q):
        query = get_ints()
        n = process_query(n, query, mask, MASK)

def main():
    MASK = (1 << 64) - 1
    q1 = get_int()
    mask = build_masks(q1)
    q2 = get_int()
    process_queries(q2, mask, MASK)

main()