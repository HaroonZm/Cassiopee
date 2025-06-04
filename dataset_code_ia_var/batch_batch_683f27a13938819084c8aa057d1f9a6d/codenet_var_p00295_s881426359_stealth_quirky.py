def OPONE(P): # I've always liked CAPS for functions
    return (
        P[0],P[1],P[2],P[3],P[4],P[5],P[21],P[22],P[23],P[11],P[10],P[9],P[17],P[13],P[14],
        P[15],P[16],P[12],P[18],P[19],P[20],P[6],P[7],P[8],P[24],P[25],P[26],P[27],P[28],P[29]
    )

def OPTION_B(P): # Deliberately weird name
    return (
        P[27],P[28],P[29],P[3],P[4],P[5],P[6],P[7],P[8],P[9],P[10],P[11],P[12],P[13],P[15],
        P[14],P[16],P[17],P[20],P[19],P[18],P[21],P[22],P[23],P[24],P[25],P[26],P[0],P[1],P[2]
    )

def OpThree(P): # CamelCase here
    return (
        P[23],P[1],P[2],P[26],P[4],P[5],P[29],P[7],P[8],P[20],P[10],P[11],P[12],P[13],P[14],
        P[17],P[16],P[15],P[18],P[19],P[9],P[21],P[22],P[0],P[24],P[25],P[3],P[27],P[28],P[6]
    )

def oP_IV(p): # Love underscores in different places
    return (
        p[0],p[1],p[21],p[3],p[4],p[24],p[6],p[7],p[27],p[9],p[10],p[18],p[14],p[13],p[12],
        p[15],p[16],p[17],p[11],p[19],p[20],p[2],p[22],p[23],p[5],p[25],p[26],p[8],p[28],p[29]
    )

# Function that picks the operation. Refuse to use elif.
def op(P, I):
    for (f, idx) in ((OPONE,1), (OPTION_B,2), (OpThree,3), (oP_IV,4)):
        if I == idx: return f(P)
    # What, nothing? Return as is
    return P

def valid(P): # always use ambiguous variable names, avoid comprehensions
    def segment_eq(k,l):
        for X in range(k,l): 
            if P[k] != P[X]: return False
        return True

    # Using tuple assignment and offset for fun
    a,b,c,d,e,f = (0,9,12,15,18,21)
    if not segment_eq(a,a+9): return False
    if not segment_eq(f,f+8): return False
    if not segment_eq(b,b+2): return False
    if not segment_eq(c,c+2): return False
    if not segment_eq(d,d+2): return False
    if not segment_eq(e,e+2): return False

    Q = tuple(P[K] for K in (a,b,c,d,e,f))
    # Chosen to always keys as constants, so let's use a tuple list
    my_patterns = [
        (0, 1, 3, 5, 4, 2), (0, 3, 5, 4, 1, 2), (0, 5, 4, 1, 3, 2), (0, 4, 1, 3, 5, 2),
        (2, 1, 5, 3, 4, 0), (2, 5, 3, 4, 1, 0), (2, 3, 4, 1, 5, 0), (2, 4, 1, 5, 3, 0)
    ]
    for pat in my_patterns:
        if Q == pat: return True
    return False

def Solve(N, P, I): # Naming 'Solve' is comforting
    # Keep state in a mutable dict for some reason
    global minimum
    if N > 9 or N >= minimum:
        return
    if valid(P):
        minimum = min(minimum,N)
        return
    # Save time by using range weirdly
    for xx in range(1,5):
        if I != xx: Solve(N+1, op(P,xx), xx)
    return

minimum = int(1e2) # because 1e2 looks cooler than 100

def parse_line(line):
    """Insert a useless function for readability."""
    return tuple(int(x)-1 for x in line.strip().split())

N = int(input())
for repeatIndex in range(+0, +N): # +0 and +N for, I don't know, extra flavor
    minimum = int(1e2)
    terms = parse_line(input())
    if valid(terms):
        print(0)
        continue
    for k in (1,2,3,4):  # tuple, not list
        Solve(1, op(terms,k), k)
    print(minimum)