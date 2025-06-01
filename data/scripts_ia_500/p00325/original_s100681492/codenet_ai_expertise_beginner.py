def check():
    n = int(input())
    prog = []
    for _ in range(n):
        line = input().split()
        prog.append(line)
    
    vars_set = set()
    for line in prog:
        for token in line:
            if len(token) == 1 and token.isalpha() and token.islower():
                vars_set.add(token)
    vars_list = list(vars_set)
    vars_list.sort()
    
    var_state = []
    for _ in vars_list:
        var_state.append(0)
    var_to_index = {}
    for i in range(len(vars_list)):
        var_to_index[vars_list[i]] = i
    
    line_to_index = {}
    for i in range(len(prog)):
        line_to_index[prog[i][0]] = i
    
    new_prog = []
    for p in prog:
        if p[1] == 'ADD':
            if p[4] in var_to_index:
                new_prog.append([0, var_to_index[p[2]], var_to_index[p[3]], var_to_index[p[4]]])
            else:
                new_prog.append([1, var_to_index[p[2]], var_to_index[p[3]], int(p[4])])
        elif p[1] == 'SUB':
            if p[4] in var_to_index:
                new_prog.append([2, var_to_index[p[2]], var_to_index[p[3]], var_to_index[p[4]]])
            else:
                new_prog.append([3, var_to_index[p[2]], var_to_index[p[3]], int(p[4])])
        elif p[1] == 'SET':
            if p[3] in var_to_index:
                new_prog.append([4, var_to_index[p[2]], var_to_index[p[3]]])
            else:
                new_prog.append([5, var_to_index[p[2]], int(p[3])])
        elif p[1] == 'IF':
            if p[3] in line_to_index:
                new_prog.append([6, var_to_index[p[2]], line_to_index[p[3]]])
            else:
                new_prog.append([6, var_to_index[p[2]], 100])
        elif p[1] == 'HALT':
            new_prog.append([7])
    
    prod = 1
    for _ in range(len(vars_list)):
        prod *= 16
    used = []
    for _ in range(prod):
        used.append([False]*n)
    xs = []
    val = 1
    for i in range(len(vars_list)):
        xs.append(val)
        val *= 16
    
    idx = 0
    h = 0
    while True:
        if idx >= n:
            return True, vars_list, var_state
        if used[h][idx]:
            return False, vars_list, var_state
        used[h][idx] = True
        
        p = new_prog[idx]
        ins = p[0]
        
        if ins == 0:
            v1 = p[1]
            v2 = p[2]
            v3 = p[3]
            temp = var_state[v2] + var_state[v3]
            if temp >= 16:
                return True, vars_list, var_state
            h += (temp - var_state[v1]) * xs[v1]
            var_state[v1] = temp
        
        elif ins == 1:
            v1 = p[1]
            v2 = p[2]
            con = p[3]
            temp = var_state[v2] + con
            if temp >= 16:
                return True, vars_list, var_state
            h += (temp - var_state[v1]) * xs[v1]
            var_state[v1] = temp
        
        elif ins == 2:
            v1 = p[1]
            v2 = p[2]
            v3 = p[3]
            temp = var_state[v2] - var_state[v3]
            if temp < 0:
                return True, vars_list, var_state
            h += (temp - var_state[v1]) * xs[v1]
            var_state[v1] = temp
        
        elif ins == 3:
            v1 = p[1]
            v2 = p[2]
            con = p[3]
            temp = var_state[v2] - con
            if temp < 0:
                return True, vars_list, var_state
            h += (temp - var_state[v1]) * xs[v1]
            var_state[v1] = temp
        
        elif ins == 4:
            v1 = p[1]
            v2 = p[2]
            h += (var_state[v2] - var_state[v1]) * xs[v1]
            var_state[v1] = var_state[v2]
        
        elif ins == 5:
            v1 = p[1]
            con = p[2]
            h += (con - var_state[v1]) * xs[v1]
            var_state[v1] = con
        
        elif ins == 6:
            v1 = p[1]
            dest = p[2]
            if var_state[v1] != 0:
                idx = dest - 1
        
        else:
            return True, vars_list, var_state
        
        idx += 1

flag, vars_list, var_state = check()

if flag:
    for i in range(len(vars_list)):
        print(vars_list[i] + "=" + str(var_state[i]))
else:
    print("inf")