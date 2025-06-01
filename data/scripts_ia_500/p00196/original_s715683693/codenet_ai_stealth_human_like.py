while 1==1:
    n = int(input())
    if n == 0:
        break
    data = []
    for _ in range(n):
        line = input().split()
        data.append(line)
        
    # Ok so now count zeros and ones in each line? Let's see
    counts = []
    for r in data:
        # r[0] is like a name, then count '0's and '1's in r list? hmmm
        cnt_0 = r.count('0')
        cnt_1 = r.count('1')
        counts.append([r[0], cnt_0, cnt_1])

    # Sort descending by zeros, ascending by ones? that's the plan
    counts.sort(key=lambda x: (-x[1], x[2]))

    names_sorted = [c[0] for c in counts]

    print("\n".join(names_sorted))