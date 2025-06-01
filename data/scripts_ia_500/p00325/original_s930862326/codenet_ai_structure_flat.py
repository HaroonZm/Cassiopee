n = int(input())
stmts = [input().split() for _ in range(n)]
mapper = {}
vn = {}
vs = []
for i, stmt in enumerate(stmts):
    mapper[stmt[0]] = i
    for ope in stmt[2:]:
        if ope.isalpha() and ope not in vn:
            vn[ope] = len(vn)
vs = [0]*len(vn)
stmt_func = []
for stmt in stmts:
    op = stmt[1]
    if op == 'ADD':
        v1 = vn[stmt[2]]
        if stmt[4].isdigit():
            v2 = vn[stmt[3]]
            const = int(stmt[4])
            def run(pc, v1=v1, v2=v2, const=const):
                assert vs[v2] + const < 16
                vs[v1] = vs[v2] + const
                return pc+1
        else:
            v2 = vn[stmt[3]]
            v3 = vn[stmt[4]]
            def run(pc, v1=v1, v2=v2, v3=v3):
                assert vs[v2] + vs[v3] < 16
                vs[v1] = vs[v2] + vs[v3]
                return pc+1
        stmt_func.append(run)
    elif op == 'SUB':
        v1 = vn[stmt[2]]
        if stmt[4].isdigit():
            v2 = vn[stmt[3]]
            const = int(stmt[4])
            def run(pc, v1=v1, v2=v2, const=const):
                assert 0 <= vs[v2] - const
                vs[v1] = vs[v2] - const
                return pc+1
        else:
            v2 = vn[stmt[3]]
            v3 = vn[stmt[4]]
            def run(pc, v1=v1, v2=v2, v3=v3):
                assert 0 <= vs[v2] - vs[v3]
                vs[v1] = vs[v2] - vs[v3]
                return pc+1
        stmt_func.append(run)
    elif op == 'SET':
        v1 = vn[stmt[2]]
        if stmt[3].isdigit():
            v2 = int(stmt[3])
            def run(pc, v1=v1, v2=v2):
                vs[v1] = v2
                return pc+1
        else:
            v2 = vn[stmt[3]]
            def run(pc, v1=v1, v2=v2):
                vs[v1] = vs[v2]
                return pc+1
        stmt_func.append(run)
    elif op == 'IF':
        v1 = vn[stmt[2]]
        dest = stmt[3]
        def run(pc, v1=v1, dest=dest):
            return mapper[dest] if vs[v1] else pc+1
        stmt_func.append(run)
    else:
        def run(pc):
            return n
        stmt_func.append(run)
result = 1
pc = 0
cnts = [0]*n
LIM = 16**len(vn) + 10
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
if result:
    for k in sorted(vn):
        print("%s=%d" % (k, vs[vn[k]]))
else:
    print("inf")