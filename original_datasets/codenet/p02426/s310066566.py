n = int(input())

list_mask = []

for _ in range(n):

    k, *list_b = map(int, input().split())

    mask = 0

    for i in range(k):
        mask += 2 ** list_b[i]

    list_mask.append(mask)

q = int(input())

bit_flag = 0

for _ in range(q):

    command, *list_num = input().split()

    m = int(list_num[0])

    if   command == "0":
        # test(i)
        i = m
        if bit_flag & (2 ** i):
            print(1)
        else:
            print(0)
    elif command == "1":
        # set(m)
        bit_flag = bit_flag | list_mask[m]
    elif command == "2":
        # clear(m)
        bit_flag = bit_flag & ~list_mask[m]
    elif command == "3":
        # flip(m)
        bit_flag = bit_flag ^ list_mask[m]
    elif command == "4":
        # all(m)
        if (bit_flag & list_mask[m]) == list_mask[m]:
            print(1)
        else:
            print(0)
    elif command == "5":
        # any(m)
        if bit_flag & list_mask[m]:
            print(1)
        else:
            print(0)
    elif command == "6":
        # none(m)
        if not bit_flag & list_mask[m]:
            print(1)
        else:
            print(0)
    elif command == "7":
        # count(m)
        print(bin(bit_flag & list_mask[m]).count("1"))
    elif command == "8":
        # val(m)
        print(bit_flag & list_mask[m])
    else:
        raise