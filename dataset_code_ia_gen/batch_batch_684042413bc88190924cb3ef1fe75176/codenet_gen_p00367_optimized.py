def time_to_min(h, m):
    return h * 60 + m

def max_customers():
    N = int(input())
    breakfast_times = []
    lunch_times = []
    supper_times = []
    for _ in range(N):
        ast, aet, hst, het, bst, bet = map(int, input().split())
        breakfast_times.append((time_to_min(ast, aet), time_to_min(aet, 0)))
        lunch_times.append((time_to_min(hst, het), time_to_min(het, 0)))
        supper_times.append((time_to_min(bst, bet), time_to_min(bet, 0)))

    # Correction: The above code incorrectly uses time_to_min with 2 arguments, must fix input parsing.

def max_customers():
    N = int(input())
    breakfast = []
    lunch = []
    supper = []
    for _ in range(N):
        ast_h, ast_m, aet_h, aet_m, hst_h, hst_m, het_h, het_m, bst_h, bst_m, bet_h, bet_m = map(int, input().split())
        breakfast.append((time_to_min(ast_h, ast_m), time_to_min(aet_h, aet_m)))
        lunch.append((time_to_min(hst_h, hst_m), time_to_min(het_h, het_m)))
        supper.append((time_to_min(bst_h, bst_m), time_to_min(bet_h, bet_m)))

    # Candidate serving times must be selected from customers' time zone edges
    breakfast_candidates = set()
    lunch_candidates = set()
    supper_candidates = set()

    for i in range(N):
        breakfast_candidates.add(breakfast[i][0])
        breakfast_candidates.add(breakfast[i][1])
        lunch_candidates.add(lunch[i][0])
        lunch_candidates.add(lunch[i][1])
        supper_candidates.add(supper[i][0])
        supper_candidates.add(supper[i][1])

    max_count = 0
    # For each combination of breakfast, lunch, supper serving times, count how many customers fit all three
    for b in breakfast_candidates:
        for l in lunch_candidates:
            if l <= b:
                continue
            for s in supper_candidates:
                if s <= l:
                    continue
                count = 0
                for i in range(N):
                    if breakfast[i][0] <= b <= breakfast[i][1] and lunch[i][0] <= l <= lunch[i][1] and supper[i][0] <= s <= supper[i][1]:
                        count += 1
                if count > max_count:
                    max_count = count
    print(max_count)

max_customers()