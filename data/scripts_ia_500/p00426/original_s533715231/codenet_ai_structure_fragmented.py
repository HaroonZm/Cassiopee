def solve():
    from sys import stdin
    f_i = stdin

    def read_input():
        return map(int, f_i.readline().split())

    def read_cups(n):
        cups = [None] * n
        def assign_trays(tray):
            itr = map(int, f_i.readline().split())
            next(itr)
            def assign_indices():
                for i in itr:
                    cups[i - 1] = tray
            assign_indices()
        for tray in 'ABC':
            assign_trays(tray)
        return cups

    def power_of_three(exp):
        return 3 ** exp

    def rec(i, cups, n):
        def base_case():
            return 0
        def get_tray():
            return cups[n - i]
        def rec_decrement():
            return rec(i - 1, cups, n)
        def calculate_B():
            return 2 * power_of_three(i - 1) - 1 - rec_decrement()
        def calculate_C():
            return rec_decrement() + 2 * power_of_three(i - 1)
        if i == 0:
            return base_case()
        tray = get_tray()
        if tray == 'A':
            return rec_decrement()
        elif tray == 'B':
            return calculate_B()
        else:
            return calculate_C()

    def process_case(n, m):
        cups = read_cups(n)
        num = rec(n, cups, n)
        max_val = power_of_three(n) - 1
        def get_min_num():
            return min(num, max_val - num)
        ans = get_min_num()
        def print_result():
            if ans <= m:
                print(ans)
            else:
                print(-1)
        print_result()

    def main_loop():
        while True:
            n, m = read_input()
            if n == 0:
                break
            process_case(n, m)

    main_loop()

solve()