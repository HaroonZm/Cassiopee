while True:
    n = int(input())
    if n == 0:
        break
    lines = [input() for _ in range(n)]
    depths = [0]*n
    for i, line in enumerate(lines):
        cnt = 0
        for c in line:
            if c == '.':
                cnt += 1
            else:
                break
        depths[i] = cnt
    substs = []
    for i in range(n):
        d = depths[i]
        line = lines[i]
        base = list(line)
        # positions from 0 to d-1 are dots, need to replace
        # The rightmost dot (at position d-1) -> '+'
        if d > 0:
            base[d-1] = '+'
        # For positions 0 to d-2
        # For each pos j in 0..d-2:
        # If i==0: no parent (no dots)
        # Else compare depths of next sibling to decide between '|' and ' '
        for j in range(d - 1):
            # Determine if at this depth there is any next sibling with same depth
            # Move down the list to see if there is a next node with depth == j+1 under same parent at this level
            # But simpler: according to explanation, if the next sibling at this level exists, replace with '|', else ' '
            # We check next siblings to see if any has depth > j and first non-children would break?
            # Instead, we note that vertical bars '|' appear between '+' of siblings only
            # We'll check next lines for potential sibling at depth j+1 or deeper
            # The condition is: if exists k>i such that depths[k]>=j+1 and depths[k]<=d and
            # for all m in (i+1)..k-1 depths[m]>j
            # But given input is guaranteed, we can implement a simplified version:
            # If after i exists a line k with depth == j+1, and no depth <= j in between, then '|' else ' '
            # Implement this check:
            found = False
            for k in range(i+1, n):
                if depths[k] == j+1:
                    found = True
                    break
                if depths[k] <= j:
                    break
            base[j] = '|' if found else ' '
        substs.append("".join(base[d:]))
        print("".join(base[:d]) + "".join(base[d:]))