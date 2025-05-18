n = int(input())
stmts = [input().split() for i in range(n)]

mapper = {}
for i, stmt in enumerate(stmts):
    mapper[stmt[0]] = i

vn = {}
for stmt in stmts:
    for ope in stmt[2:]:
        if ope.isalpha() and ope not in vn:
            vn[ope] = len(vn)
vs = [0]*len(vn)
def stmt_add(v1, v2, v3):
    v1 = vn[v1]
    if v3.isdigit():
        v2 = vn[v2]
        const = int(v3)
        def run(pc):
            assert vs[v2] + const < 16
            vs[v1] = vs[v2] + const
            return pc+1
    else:
        v2 = vn[v2]
        v3 = vn[v3]
        def run(pc):
            assert vs[v2] + vs[v3] < 16
            vs[v1] = vs[v2] + vs[v3]
            return pc+1
    return run
def stmt_sub(v1, v2, v3):
    v1 = vn[v1]
    if v3.isdigit():
        v2 = vn[v2]
        const = int(v3)
        def run(pc):
            assert 0 <= vs[v2] - const
            vs[v1] = vs[v2] - const
            return pc+1
    else:
        v2 = vn[v2]
        v3 = vn[v3]
        def run(pc):
            assert 0 <= vs[v2] - vs[v3]
            vs[v1] = vs[v2] - vs[v3]
            return pc+1
    return run
def stmt_set(v1, v2):
    v1 = vn[v1]
    if v2.isdigit():
        v2 = int(v2)
        def run(pc):
            vs[v1] = v2
            return pc+1
    else:
        v2 = vn[v2]
        def run(pc):
            vs[v1] = vs[v2]
            return pc+1
    return run
def stmt_if(v1, dest):
    v1 = vn[v1]
    def run(pc):
        return mapper[dest] if vs[v1] else pc+1
    return run
def stmt_halt():
    def run(pc):
        return n
    return run
stmt_func = []
for i, stmt in enumerate(stmts):
    op = stmt[1]
    if op == 'ADD':
        stmt_func.append(stmt_add(*stmt[2:]))
    elif op == 'SUB':
        stmt_func.append(stmt_sub(*stmt[2:]))
    elif op == 'SET':
        stmt_func.append(stmt_set(*stmt[2:]))
    elif op == 'IF':
        stmt_func.append(stmt_if(*stmt[2:]))
    else:
        stmt_func.append(stmt_halt())

result = 1
pc = 0
cnts = [0]*n
LIM = 16**len(vn) + 10
try:
    while 1:
        run = stmt_func[pc]
        cnts[pc] += 1
        if cnts[pc] > LIM:
            result = 0
            break
        pc = run(pc)
except:...
if result:
    for k in sorted(vn):
        print("%s=%d" % (k, vs[vn[k]]))
else:
    print("inf")