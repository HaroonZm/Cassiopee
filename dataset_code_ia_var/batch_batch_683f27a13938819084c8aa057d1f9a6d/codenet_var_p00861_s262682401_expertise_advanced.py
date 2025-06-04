from functools import partial

def read_blocks(input_func=input):
    while True:
        block = []
        while True:
            S = input_func()
            if S == '.':
                break
            block.append(S)
        if not block:
            break
        yield block

def safe_exec(stmt, env):
    try:
        exec(stmt, env)
        return True
    except Exception:
        return False

for lst in read_blocks(input if 'raw_input' not in globals() else raw_input):
    env = {}
    upper = []
    flag = False
    for i, S in enumerate(lst):
        if '=' in S:
            if not safe_exec(S, env):
                flag = True
            for dic, limit in upper:
                if any(k >= limit for k in dic):
                    flag = True
                    break
            if flag:
                print(i + 1)
                break
        else:
            name, num = S.split('[')
            name = name.strip()
            num = int(num.rstrip(']'))
            env.setdefault(name, {})
            upper.append((env[name], num))
    if not flag:
        print(0)