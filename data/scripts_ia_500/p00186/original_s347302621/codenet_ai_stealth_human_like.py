import sys
# Set recursion limit high enough for deep recursions if needed
sys.setrecursionlimit(100000)

BIG_NUM = 2_000_000_000  # just a big number, probably unused here
HUGE_NUM = 99999999999999999  # way huge number, not really used below
MOD = 10**9 + 7  # common mod value, but not applied here
EPS = 1e-9  # epsilon for floating point comparisons, also not really used

while True:
    line = input()
    if line == "0":   # if input line is only "0", stop processing
        break

    need, budget, aizu_cost, normal_cost, limit = map(int, line.split())
    
    # Binary search boundaries for how many 'aizu' items can be bought
    low, high = 1, limit
    best_aizu = 0
    best_normal = 0
    
    while low <= high:
        mid = (low + high) // 2
        remaining_budget = budget - mid * aizu_cost
        if remaining_budget < 0:
            # can't afford mid number of aizu items
            high = mid - 1
            continue
        
        can_buy_normal = remaining_budget // normal_cost
        
        # Check if the total items meet the need
        if mid + can_buy_normal >= need:
            best_aizu = mid
            best_normal = can_buy_normal
            low = mid + 1  # try to buy more aizu if possible
        else:
            high = mid - 1  # too many aizu, can't reach need with normal
    
    if best_aizu == 0:
        print("NA")
    else:
        print(f"{best_aizu} {best_normal}")