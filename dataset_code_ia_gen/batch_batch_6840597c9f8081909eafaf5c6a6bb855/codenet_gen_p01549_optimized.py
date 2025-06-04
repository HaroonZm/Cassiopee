import sys
sys.setrecursionlimit(10**7)

m = int(sys.stdin.readline())
vars_bounds = {}
for _ in range(m):
    line = sys.stdin.readline().split()
    vars_bounds[line[0]] = (int(line[1]), int(line[2]))
n = int(sys.stdin.readline())
expr = sys.stdin.readline().split()

# 1. On encountering a number: range = [val,val]
# 2. On encountering a variable: range from vars_bounds
# 3. On operator, pop two ranges, compute resulting range

# Since values wrap mod 256 after each op, results are always in [0,255]
# But we want to check if division by zero is possible:
# That means check if divisor's range includes zero.

def add_range(r1, r2):
    res_min = (r1[0]+r2[0])%256
    res_max = (r1[1]+r2[1])%256
    # Because of mod, the range is actually entire [0,255] if overflow
    # So, conservatively treat as full range if wrapping occurs
    if r1[0]+r2[0] > 255 or r1[1]+r2[1] > 255:
        return (0,255)
    return (res_min, res_max) if res_min <= res_max else (0,255)

def sub_range(r1,r2):
    diffs = [(r1[0]-r2[0])%256,(r1[0]-r2[1])%256,(r1[1]-r2[0])%256,(r1[1]-r2[1])%256]
    mn, mx = min(diffs), max(diffs)
    # If wrap, range is whole
    if (mx - mn) % 256 < 0:
        return (0,255)
    # It's possible range is wrapped, so to be safe use full range if wrap
    if mn > mx:
        return (0,255)
    return (mn,mx)

def mul_range(r1,r2):
    candidates = []
    for a in (r1[0], r1[1]):
        for b in (r2[0], r2[1]):
            candidates.append((a*b)%256)
    mn, mx = min(candidates), max(candidates)
    # multiplication mod wraps, to be safe use full range if wrap around occurs
    if mx < mn:
        return (0,255)
    # If range not continuous, can't represent precisely, so full range
    if mx - mn < 0:
        return (0,255)
    return (mn,mx)

def div_range(r1,r2):
    # division is integer division (floor) modulo 256.
    # zero division possible if 0 in r2's range
    # So main check is done outside this function
    # But we still must compute possible range
    res = set()
    low, high = r2
    # We want to consider all divisors in [low,high]
    # including wrapping issues: so if low<=high straightforward,
    # else [low..255]+[0..high]
    divisors = []
    if low <= high:
        for d in range(low, high+1):
            if d != 0:
                divisors.append(d)
    else:
        for d in range(low,256):
            if d != 0:
                divisors.append(d)
        for d in range(0,high+1):
            if d != 0:
                divisors.append(d)
    if not divisors:
        # divisor must not be zero, but all are zero here? => division undefined
        return (0,0)  # dummy
    
    # Because dividend range can wrap, consider all possible dividends a in [r1[0], r1[1]] modulo 256
    dividends = []
    if r1[0] <= r1[1]:
        dividends = range(r1[0], r1[1]+1)
    else:
        dividends = list(range(r1[0],256)) + list(range(0,r1[1]+1))
    for a in dividends:
        for d in divisors:
            res.add((a//d)%256)
    mn, mx = min(res), max(res)
    # range may wrap
    # We conservatively treat the actual range as [mn,mx]
    return (mn,mx)

# Actually more direct logic: since all vars and intermediate are in [0,255]
# We can represent ranges more simply with tuples (min,max)
# But to handle modular wrap effectively and conservatively, better to use
# sets would be costly. Instead, use earliest and latest values.

# Simpler: use sets but since max 100 elements, and up to 256 values,
# do intervals carefully to be safe.

# Let's implement with intervals and if wrap occurs, use full range.

def range_add(r1,r2):
    a_min,a_max = r1
    b_min,b_max = r2
    s_min = (a_min + b_min)%256
    s_max = (a_max + b_max)%256
    if a_min + b_min > 255 or a_max + b_max > 255:
        return (0,255)
    if s_min <= s_max:
        return (s_min, s_max)
    return (0,255)

def range_sub(r1,r2):
    a_min,a_max = r1
    b_min,b_max = r2
    candidates = [(a_min - b_min)%256,(a_min - b_max)%256,(a_max - b_min)%256,(a_max - b_max)%256]
    mn = min(candidates)
    mx = max(candidates)
    if mn <= mx:
        return (mn,mx)
    return (0,255)

def range_mul(r1,r2):
    a_min,a_max = r1
    b_min,b_max = r2
    candidates = [(a_min*b_min)%256,(a_min*b_max)%256,(a_max*b_min)%256,(a_max*b_max)%256]
    mn = min(candidates)
    mx = max(candidates)
    if mn <= mx:
        return (mn,mx)
    return (0,255)

def range_div(r1,r2):
    a_min,a_max = r1
    b_min,b_max = r2
    # If divisor range includes zero, division by zero is possible, but handled outside.
    # Gather all divisors excluding zero
    divisors = []
    if b_min <= b_max:
        for d in range(b_min, b_max+1):
            if d != 0:
                divisors.append(d)
    else:
        for d in range(b_min,256):
            if d != 0:
                divisors.append(d)
        for d in range(0,b_max+1):
            if d != 0:
                divisors.append(d)
    if not divisors:
        # no valid divisors
        return (0,0)
    # All dividends
    dividends = []
    if a_min <= a_max:
        dividends = range(a_min,a_max+1)
    else:
        dividends = list(range(a_min,256))+list(range(0,a_max+1))
    results = set()
    for a in dividends:
        for d in divisors:
            results.add( (a//d)%256 )
    mn = min(results)
    mx = max(results)
    if mn <= mx:
        return (mn,mx)
    return (0,255)

stack = []
# Push ranges onto stack; each element is (min,max)
for token in expr:
    if token in '+-*/':
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            stack.append(range_add(a,b))
        elif token == '-':
            stack.append(range_sub(a,b))
        elif token == '*':
            stack.append(range_mul(a,b))
        else:
            # division
            # check if divisor can be zero
            b_min,b_max = b
            if b_min <= b_max:
                if 0 >= b_min and 0 <= b_max:
                    print("error")
                    sys.exit()
            else:
                # wrapped range
                # divisor range includes zero if zero >= b_min or zero <= b_max
                if 0 >= b_min or 0 <= b_max:
                    print("error")
                    sys.exit()
            stack.append(range_div(a,b))
    else:
        # number or variable
        if token.isdigit():
            v=int(token)
            stack.append((v,v))
        else:
            stack.append(vars_bounds[token])
print("correct")