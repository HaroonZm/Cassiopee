N = int(input())
program = []
line_to_index = {}
variables = set()

for i in range(N):
    parts = input().split()
    line_num = int(parts[0])
    instr = parts[1]
    args = parts[2:]
    program.append((line_num, instr, args))
    line_to_index[line_num] = i
    # Collect variables
    if instr in ('ADD', 'SUB', 'SET', 'IF'):
        for a in args:
            if a.isalpha() and len(a) == 1:
                variables.add(a)

variables = sorted(variables)
vars_values = {v: 0 for v in variables}

def is_var(s):
    return s.isalpha() and len(s) == 1

def get_val(s):
    if is_var(s):
        return vars_values[s]
    else:
        return int(s)

visited = set()
pc = 0

while True:
    if pc < 0 or pc >= N:
        # Jumped outside the program, stop
        break
    state = (pc, tuple(vars_values[v] for v in variables))
    # To detect infinite loops more efficiently,
    # we track visited as (pc, variable values)
    # If revisit same state -> infinite loop
    if state in visited:
        print("inf")
        exit()
    visited.add(state)

    line_num, instr, args = program[pc]

    if instr == 'ADD':
        # ADD var1 var2 var3 or ADD var1 var2 con
        var1 = args[0]
        var2 = args[1]
        var3_or_con = args[2]
        val2 = vars_values[var2]
        if is_var(var3_or_con):
            val3 = vars_values[var3_or_con]
        else:
            val3 = int(var3_or_con)
        val = val2 + val3
        if val < 0 or val >= 16:
            # Stop before updating
            break
        vars_values[var1] = val
        pc += 1

    elif instr == 'SUB':
        # SUB var1 var2 var3 or SUB var1 var2 con
        var1 = args[0]
        var2 = args[1]
        var3_or_con = args[2]
        val2 = vars_values[var2]
        if is_var(var3_or_con):
            val3 = vars_values[var3_or_con]
        else:
            val3 = int(var3_or_con)
        val = val2 - val3
        if val < 0 or val >= 16:
            break
        vars_values[var1] = val
        pc += 1

    elif instr == 'SET':
        # SET var1 var2 or SET var1 con
        var1 = args[0]
        src = args[1]
        if is_var(src):
            val = vars_values[src]
        else:
            val = int(src)
        if val < 0 or val >= 16:
            break
        vars_values[var1] = val
        pc += 1

    elif instr == 'IF':
        # IF var dest
        var1 = args[0]
        dest = int(args[1])
        val = vars_values[var1]
        if val != 0:
            if dest not in line_to_index:
                # jump to non-existent line number
                break
            pc = line_to_index[dest]
        else:
            pc += 1

    elif instr == 'HALT':
        # Stop program
        break

    else:
        # Unknown instruction, just stop
        break

# If finished loop without break, print vars
# but if loop interrupted by break, print vars or "inf" already printed
for v in variables:
    print(f"{v}={vars_values[v]}")