def main():
    import sys
    lines = sys.stdin.read().strip('\n ').split('\n')
    idx = 0
    first = True
    while True:
        if idx >= len(lines):
            break
        line = lines[idx].strip()
        if line == '0':
            break
        if not line:
            idx += 1
            continue
        p, s = map(int, line.split())
        idx += 1
        table = []
        for _ in range(p):
            row = lines[idx].split()
            idx += 1
            table.append(row)
        totals_row = lines[idx].split()
        idx += 1

        # Parse table: store known values as int, unknown as None
        # Also record the unknown positions in order
        data = []
        unknowns = []
        for i in range(p):
            row_data = []
            for j in range(s):
                if table[i][j] == '?':
                    row_data.append(None)
                    unknowns.append((i,j))
                else:
                    row_data.append(int(table[i][j]))
            row_data.append(int(table[i][s]))  # product total
            data.append(row_data)
        # Parse totals row, last element is grand total but can be ignored
        totals = list(map(int, totals_row[:s]))
        grand_total = int(totals_row[s])

        # We have p*s unknowns with some known and unknown entries
        # We can use the equations:
        # sum over stores of product i = product total[i]
        # sum over products of store j = totals[j]
        #
        # Variables: unknowns
        # Equations: p (product totals) + s (store totals) = p + s equations
        # Unknowns count can be more than equations => no unique solution.
        # We try to solve by substitution repeatedly.

        values = [[data[i][j] for j in range(s)] for i in range(p)]
        # Initially known values in values, unknown are None

        changed = True
        while changed:
            changed = False
            # Try to solve rows (product totals)
            for i in range(p):
                row = values[i]
                total = data[i][s]
                unknown_indices = [j for j in range(s) if row[j] is None]
                if len(unknown_indices) == 1:
                    j = unknown_indices[0]
                    s_known = 0
                    for k in range(s):
                        if k != j and row[k] is not None:
                            s_known += row[k]
                    val = total - s_known
                    if values[i][j] is None:
                        values[i][j] = val
                        changed = True
            # Try to solve columns (store totals)
            for j in range(s):
                col_vals = [values[i][j] for i in range(p)]
                total = totals[j]
                unknown_indices = [i for i in range(p) if col_vals[i] is None]
                if len(unknown_indices) == 1:
                    i = unknown_indices[0]
                    s_known = 0
                    for k in range(p):
                        if k != i and values[k][j] is not None:
                            s_known += values[k][j]
                    val = total - s_known
                    if values[i][j] is None:
                        values[i][j] = val
                        changed = True

        # Check if all unknowns are filled
        no_solution = False
        for i,j in unknowns:
            if values[i][j] is None:
                no_solution = True
                break

        # Check consistency: recompute row and column sums to match given totals
        if not no_solution:
            # Check rows
            for i in range(p):
                ssum = 0
                for j in range(s):
                    if values[i][j] is None:
                        no_solution = True
                        break
                    ssum += values[i][j]
                if no_solution:
                    break
                if ssum != data[i][s]:
                    no_solution = True
                    break
            # Check columns
            if not no_solution:
                for j in range(s):
                    ssum = 0
                    for i in range(p):
                        if values[i][j] is None:
                            no_solution = True
                            break
                        ssum += values[i][j]
                    if no_solution:
                        break
                    if ssum != totals[j]:
                        no_solution = True
                        break

        # If all unknown filled and consistent, print answers in order
        if no_solution:
            if not first:
                print()
            print("NO")
            first = False
        else:
            if not first:
                print()
            for i,j in unknowns:
                print(values[i][j])
            first = False

if __name__ == "__main__":
    main()