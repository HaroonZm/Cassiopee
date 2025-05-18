import bisect

q = int(input())
M = {}
sortedList = []

for value in range(q):
    query, *inp = input().split()
    key = inp[0]

    # insert
    if query == "0":
        x = int(inp[1])

        if key not in M:
            bisect.insort_left(sortedList, key)
            M[key] = []

        M[key].append(x)

    # get
    elif query == "1":
        if key in M:
            if M[key]:
                for value in M[key]:
                    print(value)

    # delete
    elif query == "2":
        if key in M:
            M[key] = []

    # dump
    else:
        L = inp[0]
        R = inp[1]

        index_left = bisect.bisect_left(sortedList, L)
        index_right = bisect.bisect_right(sortedList, R)

        for value in range(index_left, index_right):
            keyAns = sortedList[value]
            if M[keyAns]:
                for valueAns in M[keyAns]:
                    print(keyAns, valueAns)