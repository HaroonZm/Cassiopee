if __name__ == "__main__":
    bits = [0] * 64

    num_mask = int(input())
    masks = [[] for _ in range(num_mask)]  # type: ignore
    for idx in range(num_mask):
        k, *v = map(lambda x: int(x), input().split())
        for value in v:
            masks[idx].append(value)

    num_query = int(input())
    for _ in range(num_query):
        op, *v = map(lambda x: int(x), input().split())
        if (0 == op):
            if (1 == bits[v[0]]):
                print(1)
            else:
                print(0)
        elif (1 == op):
            for m_idx in masks[v[0]]:
                bits[m_idx] = 1
        elif (2 == op):
            for m_idx in masks[v[0]]:
                bits[m_idx] = 0
        elif (3 == op):
            for m_idx in masks[v[0]]:
                bits[m_idx] = 1 if bits[m_idx] == 0 else 0
        elif (4 == op):
            all_flg = 1
            for m_idx in masks[v[0]]:
                all_flg *= bits[m_idx]
            if all_flg:
                print(1)
            else:
                print(0)
        elif (5 == op):
            any_flg = 0
            for m_idx in masks[v[0]]:
                any_flg += bits[m_idx]
            if any_flg:
                print(1)
            else:
                print(0)
        elif (6 == op):
            none_flg = 0
            for m_idx in masks[v[0]]:
                none_flg += bits[m_idx]
            if not none_flg:
                print(1)
            else:
                print(0)
        elif (7 == op):
            count = 0
            for m_idx in masks[v[0]]:
                count += bits[m_idx]
            print(count)
        else:
            ans = [0] * 64
            for m_idx in masks[v[0]]:
                ans[m_idx] = bits[m_idx]
            bin_str = "".join([str(elem) for elem in ans[::-1]])
            print(f"{int(bin_str, 2)}")