M, rD, rR, cD, cR = map(int, input().split())

def floor_div(a, b):
    return a // b

def check(x):
    # x: amount of yen exchanged to D-currency
    # M - x: amount of yen exchanged to R-currency
    if x < 0 or x > M:
        return -1
    d = (rD * x) // 100
    r = (rR * (M - x)) // 100
    if d < cD or r < cR:
        return -1
    # leftover in D and R currency after spending
    leftD = d - cD
    leftR = r - cR
    # convert leftovers back to yen
    yen_left = (100 * leftD) // rD + (100 * leftR) // rR
    # total yen returned
    total = x + (M - x) - ( (x - (100 * (d)) // rD) + ((M - x) - (100 * (r)) // rR)) + yen_left
    # But (x - floor(100*d/rD)) and ((M-x) - floor(100*r/rR)) represent lost yen in conversion, which do not add to total yen returned,
    # so total yen returned is simply yen_left + cD and cR consumed don't reduce total yen held at start.
    # Correct is to consider only yen_left + cD_coverted + cR_coverted to yen? But problem only wants final yen returned: leftover yen from conversion.
    # The problem states maximum final yen: leftover converted to yen + non-spent money.
    # Initial yen M is fully converted into D and R currencies, so leftover yen is yen_left only.
    return yen_left

# cD and cR minimum requirements in currency units correspond to minimum yen required for each currency:
min_x = (100 * cD + rD - 1) // rD  # minimal yen to get at least cD D
max_x = M - ((100 * cR + rR - 1) // rR)  # maximum yen left for D if R must get at least cR

if min_x > M or max_x < 0 or min_x > max_x:
    print(-1)
    exit()

low = min_x
high = max_x
ans = -1
while low <= high:
    mid = (low + high) // 2
    val = check(mid)
    if val == -1:
        if mid < min_x:
            low = mid + 1
        else:
            # if not valid at mid, try right side if mid < min_x else left side
            # but since val == -1 means not sufficient money, try moving accordingly

            # To be safe, we check both sides:
            # Since line is unimodal, try accordingly
            # But here we do binary search in valid range only
            # We'll move low up to find valid solution
            low = mid + 1
    else:
        ans = val
        # try to find bigger
        low = mid + 1

print(ans)