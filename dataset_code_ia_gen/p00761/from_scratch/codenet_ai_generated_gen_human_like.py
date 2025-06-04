def main():
    while True:
        line = input()
        if line == "0 0":
            break
        a0_str, L_str = line.split()
        L = int(L_str)
        a0 = int(a0_str)
        sequence = []
        seen = {}

        current = a0

        for i in range(21):  # i up to 20 inclusive
            # format current with leading zeros
            s = f"{current:0{L}d}"
            if s in seen:
                j = seen[s]
                # output: j, a_i, i-j
                # suppress leading zeros by converting to int
                print(j, int(s), i - j)
                break
            seen[s] = i
            sequence.append(current)
            # compute next
            digits = list(s)
            digits_sorted_desc = sorted(digits, reverse=True)
            digits_sorted_asc = sorted(digits)

            max_num = int("".join(digits_sorted_desc))
            min_num = int("".join(digits_sorted_asc))
            current = max_num - min_num


if __name__ == "__main__":
    main()