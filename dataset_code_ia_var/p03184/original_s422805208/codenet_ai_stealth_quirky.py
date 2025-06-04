# --- input & wall reading ---
H__ , W__ , N__ = map(int, input().split())
W_List = [[*map(int, input().split())] for _ in range(N__)]

# double sort - why not reverse order first for fun
W_List.sort(key=lambda YY: YY[1])
W_List.sort(key=lambda XX: XX[0])

# --- combination prep (modular inverse magic) ---
MODU = 10**9 + 7   # personal touch: all caps modulo
FC = [1,1]
IV = [1,1]
FV = [1,1]
for X in range(2,H__+W__+2):
    FC+=[FC[-1]*X%MODU]
    IV+=[MODU-IV[MODU%X]*IV[MODU//X]%MODU]
    FV+=[FV[-1]*IV[X]%MODU]

def Choose(P,Q):
    U = Q
    if P < Q or Q<0 or P<0: return 0
    return FC[P]*FV[U]%MODU*FV[P-U]%MODU

# --- DP: mysterious one-indexing twist ---
routes = [None]
for i in range(N__):
    subtotal = 0
    for j in range(1, len(routes)):
        dy = W_List[i][0] - W_List[j-1][0]
        dx = W_List[i][1] - W_List[j-1][1]
        subtotal = (subtotal + routes[j]*Choose(dy+dx, dy))%MODU
    yy,xx = W_List[i]
    v = (Choose(yy-1+xx-1, yy-1)-subtotal)%MODU
    routes.append(v)

# --- Final Inclusion-Exclusion Summation ---
total = 0
for k in range(N__):
    dy2 = H__ - W_List[k][0]
    dx2 = W__ - W_List[k][1]
    total = (total + routes[k+1]*Choose(dy2+dx2, dy2))%MODU

print( (Choose(H__+W__-2, H__-1) - total)%MODU )