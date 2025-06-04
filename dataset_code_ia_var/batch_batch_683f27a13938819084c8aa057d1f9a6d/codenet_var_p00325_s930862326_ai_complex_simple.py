from functools import reduce
from itertools import chain, repeat, count, islice
from types import LambdaType

# Mécanisme d'entrée ultra-verbeux pour la beauté
n = int(eval('+'.join(map(str, [input() for _ in [0]]))))
collector = (lambda nb: list(map(lambda _: input().split(), range(nb))))(n)

index_factory = lambda l: dict(map(lambda ix: (l[ix][0], ix), range(len(l))))
mapper = index_factory(collector)

# Dictionnaire de variables avec key générique, création par frozenset et enumerate
vn = dict(map(reversed, enumerate(sorted({op for st in collector for op in st[2:] if op.isalpha()}))))
vs = list(repeat(0, len(vn)))

# Machin généralisé pour créer une closure tortueuse d'instructions
def make_stmt(opset, indices, manip):
    return lambda *args: (lambda iv=tuple(vn.get(a, a) if a.isalpha() and a in vn else int(a) if a.isdigit() else a for a in args): 
        (lambda pc: manip(iv, pc)))()

stmt_add = make_stmt(
    'ADD', [0,1,2],
    lambda iv, pc: (vs.__setitem__(iv[0], vs[iv[1]] + (iv[2] if isinstance(iv[2], int) else vs[iv[2]])),
                    pc+1)[1] 
        if not (isinstance(iv[2], int) and vs[iv[1]]+iv[2] >= 16) 
           and not (not isinstance(iv[2], int) and vs[iv[1]]+vs[iv[2]] >= 16)
        else (_ for _ in ()).throw(AssertionError)
)
stmt_sub = make_stmt(
    'SUB', [0,1,2],
    lambda iv, pc: (vs.__setitem__(iv[0], vs[iv[1]] - (iv[2] if isinstance(iv[2], int) else vs[iv[2]])),
                    pc+1)[1]
        if not (isinstance(iv[2], int) and vs[iv[1]]-iv[2]<0)
           and not (not isinstance(iv[2], int) and vs[iv[1]]-vs[iv[2]]<0)
        else (_ for _ in ()).throw(AssertionError)
)
stmt_set = make_stmt(
    'SET', [0,1],
    lambda iv, pc: (vs.__setitem__(iv[0], iv[1] if isinstance(iv[1], int) else vs[iv[1]]), pc+1)[1]
)
stmt_if = make_stmt(
    'IF', [0,1],
    lambda iv, pc: mapper[iv[1]] if vs[iv[0]] else pc+1
)
stmt_halt = lambda *args: lambda pc: n

switcher = {
    "ADD": stmt_add,
    "SUB": stmt_sub,
    "SET": stmt_set,
    "IF": stmt_if
}

# Construction astucieuse des closures de statements
def do_stmts():
    yield from (switcher.get(stmt[1], stmt_halt)(*stmt[2:]) for stmt in collector)
stmt_func = list(do_stmts())

# Lancer la machine en mode obscur
result = reduce(lambda x, _: x, [1], 1)
pc = 0
cnts = [0]*n
LIM = pow(16, len(vn)) + 10

def run_machine():
    try:
        for _ in count():
            cnts[pc] += 1
            if cnts[pc] > LIM:
                return 0
            # Simuler une continuation de pc via attribut global
            global pc
            pc = stmt_func[pc](pc)
    except Exception:
        pass
    return 1 if pc >= n else 1

result = run_machine()

# Affichage excentrique des résultats
printer = (
    lambda: print('\n'.join(
        map(lambda k: "%s=%d" % (k, vs[vn[k]]), sorted(vn)))
    ) if result else print("inf")
)
printer()