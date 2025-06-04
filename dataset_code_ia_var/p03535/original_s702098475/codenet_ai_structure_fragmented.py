def get_input():
    N = int(input())
    D = [int(d) for d in input().split()]
    return N, D

def count_distances(D):
    Dcount = [0] * 13
    for i in range(13):
        Dcount[i] = D.count(i)
    return Dcount

def has_zero_or_multiple_twelve(Dcount):
    return Dcount[0] > 0 or Dcount[12] > 1

def has_triplet_in_middle(Dcount):
    for i in Dcount[1:12]:
        if i >= 3:
            return True
    return False

def get_base_positions(Dcount):
    base = [0, 24]
    if Dcount[12] == 1:
        base.append(12)
    return base

def get_single_and_double(Dcount):
    Single = []
    Double = []
    for i in range(1, 12):
        if Dcount[i] == 2:
            Double.append(i)
        elif Dcount[i] == 1:
            Single.append(i)
    return Single, Double

def extend_base_with_doubles(base, Double):
    for i in Double:
        base.append(i)
        base.append(24 - i)
    return base

def generate_clock_positions(base, Single, bitmask):
    Clock = base.copy()
    bit = format(bitmask, "b").zfill(len(Single))
    for j in range(len(Single)):
        if bit[j] == "0":
            Clock.append(Single[j])
        else:
            Clock.append(24 - Single[j])
    return Clock

def get_minimum_subinterval(Clock):
    Clock.sort()
    minsub = 24
    for j in range(1, len(Clock)):
        minsub = min(minsub, Clock[j] - Clock[j-1])
    return minsub

def calculate_max_minimum_interval(base, Single):
    lensingle = len(Single)
    minmax = 0
    for i in range(2**lensingle):
        Clock = generate_clock_positions(base, Single, i)
        minsub = get_minimum_subinterval(Clock)
        minmax = max(minmax, minsub)
    return minmax

def main():
    N, D = get_input()
    Dcount = count_distances(D)
    if has_zero_or_multiple_twelve(Dcount):
        print(0)
        return
    if has_triplet_in_middle(Dcount):
        print(0)
        return
    base = get_base_positions(Dcount)
    Single, Double = get_single_and_double(Dcount)
    base = extend_base_with_doubles(base, Double)
    minmax = calculate_max_minimum_interval(base, Single)
    print(minmax)

main()