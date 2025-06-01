import sys
sys.setrecursionlimit(10**7)

N=int(sys.stdin.readline())
prog={}
lines=[]
vars=set()
for _ in range(N):
    parts=sys.stdin.readline().split()
    line=int(parts[0])
    lines.append(line)
    instr=parts[1]
    args=parts[2:]
    prog[line]=(instr,args)
    if instr in ("ADD","SUB","SET","IF"):
        for a in args:
            if len(a)==1 and a.islower():
                vars.add(a)

line_to_idx={l:i for i,l in enumerate(lines)}
vars=sorted(vars)
# State: (pc index, variable values tuple)
from collections import deque

init_vars={v:0 for v in vars}

def is_const(x):
    return x.isdigit()

def val(x,env):
    if x.isdigit():
        return int(x)
    return env[x]

visited=set()
stack=set()

def dfs(pc,env):
    key=(pc,tuple(env[v] for v in vars))
    if key in stack:
        return False # loop detected
    if key in visited:
        return True
    stack.add(key)
    if pc>=len(lines):
        stack.remove(key)
        visited.add(key)
        return True
    line=lines[pc]
    instr,args=prog[line]
    next_pc=pc+1
    env2=env.copy()
    stop=False
    if instr=="HALT":
        stop=True
    elif instr=="ADD":
        v1=args[0]
        v2=args[1]
        op3=args[2]
        a=env[v2]
        b=int(op3) if op3.isdigit() else env[op3]
        val_new=a+b
        if val_new<0 or val_new>=16:
            stop=True
        else:
            env2[v1]=val_new
    elif instr=="SUB":
        v1=args[0]
        v2=args[1]
        op3=args[2]
        a=env[v2]
        b=int(op3) if op3.isdigit() else env[op3]
        val_new=a-b
        if val_new<0 or val_new>=16:
            stop=True
        else:
            env2[v1]=val_new
    elif instr=="SET":
        v1=args[0]
        t=args[1]
        if t.isdigit():
            val_new=int(t)
            if val_new<0 or val_new>=16:
                stop=True
            else:
                env2[v1]=val_new
        else:
            env2[v1]=env[t]
    elif instr=="IF":
        v1,dest_line=args[0],int(args[1])
        if env[v1]!=0:
            if dest_line not in line_to_idx:
                stop=True
            else:
                next_pc=line_to_idx[dest_line]
        # else continue next line
    if stop:
        stack.remove(key)
        visited.add(key)
        return True
    res=d
    if instr=="IF" and env[v1]!=0 and not stop:
        res=dfs(next_pc,env2)
    else:
        res=dfs(next_pc,env2)
    stack.remove(key)
    if res:
        visited.add(key)
    return res

if dfs(0,init_vars):
    final_env=None
    # simulate to end
    env=init_vars.copy()
    pc=0
    executed=set()
    cnt=0
    while pc<len(lines):
        line=lines[pc]
        instr,args=prog[line]
        executed.add(lines[pc])
        next_pc=pc+1
        stop=False
        if instr=="HALT":
            stop=True
        elif instr=="ADD":
            v1=args[0]
            v2=args[1]
            op3=args[2]
            a=env[v2]
            b=int(op3) if op3.isdigit() else env[op3]
            val_new=a+b
            if val_new<0 or val_new>=16:
                stop=True
            else:
                env[v1]=val_new
        elif instr=="SUB":
            v1=args[0]
            v2=args[1]
            op3=args[2]
            a=env[v2]
            b=int(op3) if op3.isdigit() else env[op3]
            val_new=a-b
            if val_new<0 or val_new>=16:
                stop=True
            else:
                env[v1]=val_new
        elif instr=="SET":
            v1=args[0]
            t=args[1]
            if t.isdigit():
                val_new=int(t)
                if val_new<0 or val_new>=16:
                    stop=True
                else:
                    env[v1]=val_new
            else:
                env[v1]=env[t]
        elif instr=="IF":
            v1,dest_line=args[0],int(args[1])
            if env[v1]!=0:
                if dest_line not in line_to_idx:
                    stop=True
                else:
                    next_pc=line_to_idx[dest_line]
        if stop:
            break
        pc=next_pc
    for v in vars:
        print(f"{v}={env[v]}")
else:
    print("inf")