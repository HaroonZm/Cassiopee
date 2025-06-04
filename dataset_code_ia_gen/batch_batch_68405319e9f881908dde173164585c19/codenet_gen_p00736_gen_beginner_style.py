def eval_formula(formula, vals):
    # vals is a dict {'P':0/1/2, 'Q':0/1/2, 'R':0/1/2}
    if formula == '0':
        return 0
    if formula == '1':
        return 1
    if formula == '2':
        return 2
    if formula == 'P':
        return vals['P']
    if formula == 'Q':
        return vals['Q']
    if formula == 'R':
        return vals['R']
    if formula[0] == '-':
        val = eval_formula(formula[1:], vals)
        if val == 0:
            return 2
        if val == 1:
            return 1
        if val == 2:
            return 0
    if formula[0] == '(':
        # find operator position
        # formula is like (X*Y) or (X+Y)
        # find main operator that splits formula in two subformulas
        level = 0
        for i in range(1, len(formula)-1):
            if formula[i] == '(':
                level += 1
            elif formula[i] == ')':
                level -= 1
            elif (formula[i] == '*' or formula[i] == '+') and level == 0:
                op_pos = i
                break
        left = formula[1:op_pos]
        right = formula[op_pos+1:-1]
        valL = eval_formula(left, vals)
        valR = eval_formula(right, vals)
        if formula[op_pos] == '*':
            # and operation
            # 3-valued logic and:
            # 0*0=0,0*1=0,0*2=0
            # 1*0=0,1*1=1,1*2=1
            # 2*0=0,2*1=1,2*2=2
            if valL == 0 or valR == 0:
                return 0
            elif valL == 1 or valR == 1:
                return 1
            else:
                return 2
        else:
            # or operation '+'
            # 0+0=0,0+1=1,0+2=2
            # 1+0=1,1+1=1,1+2=2
            # 2+0=2,2+1=2,2+2=2
            if valL == 2 or valR == 2:
                return 2
            elif valL == 1 or valR == 1:
                return 1
            else:
                return 0

count_2 = []
while True:
    line = input()
    if line == '.':
        break
    count = 0
    for P in [0,1,2]:
        for Q in [0,1,2]:
            for R in [0,1,2]:
                vals = {'P':P,'Q':Q,'R':R}
                if eval_formula(line, vals) == 2:
                    count += 1
    print(count)