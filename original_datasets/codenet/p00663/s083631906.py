while True:
    s = input().strip()
    if s == '#': break

    clauses = s.split('|')
    for clause in clauses:
        literals = clause[1:-1].split('&')
        ntil = clause.count('~')
        if ntil == 0 or ntil == 3:
            print('yes')
            break
        if ntil == 1:
            x = [v[1] for v in literals if v[0] == '~'][0]
            if clause.count(x) == 1:
                print('yes')
                break
        if ntil == 2:
            x = [v for v in literals if len(v) == 1][0]
            if clause.count(x) == 1:
                print('yes')
                break
    else:
        print('no')