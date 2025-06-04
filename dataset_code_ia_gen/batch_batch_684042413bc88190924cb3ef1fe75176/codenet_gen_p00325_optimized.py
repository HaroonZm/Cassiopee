import sys
sys.setrecursionlimit(10**7)

N=int(sys.stdin.readline())
prog=[]
lines=[]
vars_set=set()
for _ in range(N):
    parts=sys.stdin.readline().rstrip().split()
    line_no=int(parts[0])
    cmd=parts[1]
    args=parts[2:]
    prog.append((line_no,cmd,args))
    lines.append(line_no)
    for a in args:
        if len(a)==1 and a.isalpha():
            vars_set.add(a)

line_to_idx={line:i for i,line in enumerate(lines)}
variables=sorted(vars_set)

# Initialize variables to zero
init_vars={v:0 for v in variables}

# Each instruction type and args:
# ADD var1 var2 var3 or ADD var1 var2 con
# SUB var1 var2 var3 or SUB var1 var2 con
# SET var1 var2 or SET var1 con
# IF var1 dest
# HALT

# We'll simulate the execution with cycle detection.

# state: (pc, tuple(var_values)) to detect loops
# But var values max 0..15 or else stops early
# Actually variable values limited to 0..15 inclusive, but can become <0 or >=16 during operation (then stops)
# via assignment check: if assigned value <0 or >=16 then stops (does not update)
# So value possible in 0..15 inclusive.

# But variables can be max 5 distinct, each in 0..15 => 16^5=1_048_576 max states -> feasible to memoize for loop detection

def encode_vars(vars_dict):
    # pack vars in dict to tuple of values in order of variables
    return tuple(vars_dict[v] for v in variables)

visited=set()

def run():
    vars_val=init_vars.copy()
    pc=0
    stack=set()
    # We'll do iterative DFS with memo and stack to detect infinite loop

    # But since program runs single path, we can simulate step by step keeping set of visited states (pc + vars)
    # If we visit same pc+vars again => inf

    while True:
        state=(pc,encode_vars(vars_val))
        if state in visited:
            return None # inf loop
        visited.add(state)

        if pc<0 or pc>=N:
            # Jumped to non-existent line number? Actually handled below jump
            # but if pc out of range, means out of program, stop
            # According to problem: jumping to line number not in program stops program.
            # pc is index in prog list
            return vars_val

        line_no,cmd,args=prog[pc]
        if cmd=='HALT':
            return vars_val

        jump_to_next=True

        def get_val(x):
            if x.isalpha():
                return vars_val[x]
            else:
                return int(x)

        if cmd=='ADD':
            var1=args[0]
            var2=args[1]
            op3=args[2]
            v2=vars_val[var2]
            v3=get_val(op3)
            val=v2+v3
            if val<0 or val>=16:
                # stop immediately, do not update
                return vars_val
            vars_val[var1]=val
        elif cmd=='SUB':
            var1=args[0]
            var2=args[1]
            op3=args[2]
            v2=vars_val[var2]
            v3=get_val(op3)
            val=v2 - v3
            if val<0 or val>=16:
                return vars_val
            vars_val[var1]=val
        elif cmd=='SET':
            var1=args[0]
            op2=args[1]
            if op2.isalpha():
                val=vars_val[op2]
            else:
                val=int(op2)
            if val<0 or val>=16:
                return vars_val
            vars_val[var1]=val
        elif cmd=='IF':
            var1=args[0]
            dest=int(args[1])
            if vars_val[var1]!=0:
                if dest not in line_to_idx:
                    # Jump to non-existent line no, stop immediately
                    return vars_val
                pc=line_to_idx[dest]
                jump_to_next=False
        if jump_to_next:
            pc+=1
            if pc==N:
                # end of program after executing
                return vars_val

def main():
    res=run()
    if res is None:
        print('inf')
    else:
        for v in variables:
            print(f'{v}={res[v]}')

main()