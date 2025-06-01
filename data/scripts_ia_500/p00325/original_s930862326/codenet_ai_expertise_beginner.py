n = int(input())
stmts = []
for i in range(n):
    stmts.append(input().split())

mapper = {}
for i in range(n):
    mapper[stmts[i][0]] = i

vn = {}
for stmt in stmts:
    for ope in stmt[2:]:
        if ope.isalpha() and ope not in vn:
            vn[ope] = len(vn)

vs = [0] * len(vn)

def stmt_add(v1, v2, v3):
    v1_index = vn[v1]
    if v3.isdigit():
        v2_index = vn[v2]
        const = int(v3)
        def run(pc):
            if vs[v2_index] + const >= 16:
                raise Exception()
            vs[v1_index] = vs[v2_index] + const
            return pc + 1
    else:
        v2_index = vn[v2]
        v3_index = vn[v3]
        def run(pc):
            if vs[v2_index] + vs[v3_index] >= 16:
                raise Exception()
            vs[v1_index] = vs[v2_index] + vs[v3_index]
            return pc + 1
    return run

def stmt_sub(v1, v2, v3):
    v1_index = vn[v1]
    if v3.isdigit():
        v2_index = vn[v2]
        const = int(v3)
        def run(pc):
            if vs[v2_index] - const < 0:
                raise Exception()
            vs[v1_index] = vs[v2_index] - const
            return pc + 1
    else:
        v2_index = vn[v2]
        v3_index = vn[v3]
        def run(pc):
            if vs[v2_index] - vs[v3_index] < 0:
                raise Exception()
            vs[v1_index] = vs[v2_index] - vs[v3_index]
            return pc + 1
    return run

def stmt_set(v1, v2):
    v1_index = vn[v1]
    if v2.isdigit():
        val = int(v2)
        def run(pc):
            vs[v1_index] = val
            return pc + 1
    else:
        v2_index = vn[v2]
        def run(pc):
            vs[v1_index] = vs[v2_index]
            return pc + 1
    return run

def stmt_if(v1, dest):
    v1_index = vn[v1]
    def run(pc):
        if vs[v1_index] != 0:
            return mapper[dest]
        else:
            return pc + 1
    return run

def stmt_halt():
    def run(pc):
        return n
    return run

stmt_func = []
for stmt in stmts:
    op = stmt[1]
    if op == 'ADD':
        stmt_func.append(stmt_add(stmt[2], stmt[3], stmt[4]))
    elif op == 'SUB':
        stmt_func.append(stmt_sub(stmt[2], stmt[3], stmt[4]))
    elif op == 'SET':
        stmt_func.append(stmt_set(stmt[2], stmt[3]))
    elif op == 'IF':
        stmt_func.append(stmt_if(stmt[2], stmt[3]))
    else:
        stmt_func.append(stmt_halt())

result = 1
pc = 0
cnts = [0] * n
LIM = 16 ** len(vn) + 10

try:
    while True:
        run = stmt_func[pc]
        cnts[pc] += 1
        if cnts[pc] > LIM:
            result = 0
            break
        pc = run(pc)
except:
    pass

if result == 1:
    keys = list(vn.keys())
    keys.sort()
    for k in keys:
        print(k + "=" + str(vs[vn[k]]))
else:
    print("inf")