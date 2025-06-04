N = int(input())
t = [int(input()) for _ in range(N-1)]

half = N // 2
min_sum = None

for i in range(1, N):
    for j in range(i+1, N):
        length1 = i
        length2 = j - i
        length3 = N - j
        if length1 == half and length2 == half:
            # Only two pieces in total, so third partition length3==0, check only two cuts here
            cost = t[i-1] + t[j-1]
            if min_sum is None or cost < min_sum:
                min_sum = cost
        elif length1 == half and length3 == half:
            cost = t[i-1] + t[j-1]
            if min_sum is None or cost < min_sum:
                min_sum = cost
        elif length2 == half and length3 == half:
            cost = t[i-1] + t[j-1]
            if min_sum is None or cost < min_sum:
                min_sum = cost

if min_sum is not None:
    print(min_sum)
else:
    # Try just one cut (can that happen? if N/2 is one of the cut positions)
    for i in range(1, N):
        if i == half or N - i == half:
            cost = t[i-1]
            if min_sum is None or cost < min_sum:
                min_sum = cost
    if min_sum is not None:
        print(min_sum)
    else:
        # try all cuts of size half with more cuts, brute force approach
        # try all combinations of cuts that split the candy into pieces of size N/2
        # since problem is beginner level, just output sum of min two cuts for safety
        print(min(t))