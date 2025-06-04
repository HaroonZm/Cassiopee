def to_minutes(h, m):
    return h * 60 + m

def main():
    N = int(input())
    customers = []
    for _ in range(N):
        data = list(map(int, input().split()))
        ast, aet, hst, het, bst, bet = data
        b_start = to_minutes(ast, aet)
        b_end = to_minutes(hst, het)
        l_start = to_minutes(hst, het)
        l_end = to_minutes(bst, bet)
        s_start = to_minutes(bst, bet)
        s_end = to_minutes(data[10], data[11]) if len(data) > 11 else to_minutes(bst, bet)
        # Actually input format: ast_i, aet_i, hst_i, het_i, bst_i, bet_i per customer, total 6 pairs per line, 12 numbers per line
        # So above is wrong, input line has 12 integers: ast_i h_ast_i aet_i h_aet_i ... No, problem states "start and end time" means 2 ints per time: h m
        # So each customer line has 6 pairs: ast_i( h m ), aet_i( h m ), hst_i(h m), het_i(h m), bst_i(h m), bet_i(h m)
        # So a line of 12 integers: h m h m h m h m h m h m
        # So pattern: ast_h ast_m aet_h aet_m hst_h hst_m het_h het_m bst_h bst_m bet_h bet_m
        # Let's reparse:
    customers=[]
    import sys
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    idx = 1
    for _ in range(N):
        ast_h, ast_m = int(data[idx]), int(data[idx+1])
        aet_h, aet_m = int(data[idx+2]), int(data[idx+3])
        hst_h, hst_m = int(data[idx+4]), int(data[idx+5])
        het_h, het_m = int(data[idx+6]), int(data[idx+7])
        bst_h, bst_m = int(data[idx+8]), int(data[idx+9])
        bet_h, bet_m = int(data[idx+10]), int(data[idx+11])
        idx += 12
        b_start, b_end = to_minutes(ast_h, ast_m), to_minutes(aet_h, aet_m)
        l_start, l_end = to_minutes(hst_h, hst_m), to_minutes(het_h, het_m)
        s_start, s_end = to_minutes(bst_h, bst_m), to_minutes(bet_h, bet_m)
        customers.append((b_start, b_end, l_start, l_end, s_start, s_end))

    max_count = 0
    # For each meal, serving time can be chosen as any start or end time of the respective meal intervals among all customers.
    breakfast_times = []
    lunch_times = []
    supper_times = []

    for b_start, b_end, l_start, l_end, s_start, s_end in customers:
        breakfast_times.append(b_start)
        breakfast_times.append(b_end)
        lunch_times.append(l_start)
        lunch_times.append(l_end)
        supper_times.append(s_start)
        supper_times.append(s_end)

    breakfast_times = sorted(set(breakfast_times))
    lunch_times = sorted(set(lunch_times))
    supper_times = sorted(set(supper_times))

    for bt in breakfast_times:
        for lt in lunch_times:
            if lt <= bt:  # lunch must be after breakfast
                continue
            for st in supper_times:
                if st <= lt:  # supper must be after lunch
                    continue
                count = 0
                for b_start, b_end, l_start, l_end, s_start, s_end in customers:
                    if b_start <= bt <= b_end and l_start <= lt <= l_end and s_start <= st <= s_end:
                        count += 1
                if count > max_count:
                    max_count = count

    print(max_count)

if __name__ == '__main__':
    main()