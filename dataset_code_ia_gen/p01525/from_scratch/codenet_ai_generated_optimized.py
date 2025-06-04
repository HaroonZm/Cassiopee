import sys
import bisect
input=sys.stdin.readline

N,Q= map(int,input().split())
w,t,x=[],[],[]
for _ in range(N):
    W,T,X= map(int,input().split())
    w.append(W)
    t.append(T)
    x.append(X)
y=[int(input()) for _ in range(Q)]

limit=3652425
INF=1<<60

# Recherche du jour de rétablissement pour chaque service
# On simule la progression de la restauration, compte tenu de l'accélération progressive due aux services déjà restaurés.

# Pour accélération : on va stocker le cumul des accélérations jusqu'à un jour donné.
# On va trouver la journée j pour laquelle la restauration atteint w[i].
# La restauration quotidienne est 1 base + somme des accélérations.

# Vu que x[i] peut être jusqu'à 10^4 mais la somme N*xi max 1e5*1e4=1e9 trop grand de simuler jour par jour.
# On va calculer pour chaque service la contribution de son accélération sous forme de polynômes (t_i=0=>1,len=x_i), etc.
# On va faire une simulation binaire sur le jour de fin pour trouver la date de restauration de chaque service.

# Calcul des accélérations par jour:
# Chaque service i produit une accélération de jours 1..x[i]
# Par type: 0=>1 chaque jour, somme = x[i]
#          1=>d (jour), somme = x[i]*(x[i]+1)/2
#          2=>d^2 (jour²), somme = x[i]*(x[i]+1)*(2x[i]+1)/6

# On cherche la restauration à jour d:
# restauration(d) = d + sum_sur_services_deja_retablis acceleration_sur_jours_actuels
# mais le calcul exact est complexe, on note que le nombre de services est 1e5 max, x[i]<=1e4.

# Approche solution:
# - On trouvera la date de rétablissement de chaque service i par un bsearch sur les jours.
# - On trie par w[i] croissants.
# - La restauration est croissante, on simule par recherche.

# Implémentation détaillée :

# Pré-calcul des sommes partielles des accélérations pour chaque type
def sum_acc(ti, di):
    if di <=0:
        return 0
    if ti==0:
        return di
    elif ti==1:
        return di*(di+1)//2
    else:
        return di*(di+1)*(2*di+1)//6

# On va stocker accumulée l'influence de tous les services déjà rétablis sur un jour d donné:
# pour un jour D, la contribution de la période d'accélération est:
#  - pour chaque service i restauré au jour r_i, la contribution sur jour D est sum_acc(t_i , min(x_i, D - (r_i+1) +1))
#          = sum_acc(t_i, max(0, D - r_i -1))

# On peut modéliser ça comme:
# resta(d) = d + sum_{i} sum_acc(t_i, max(0,d - r_i -1))   avec r_i le jour de restauration de i

# On commence par trouver les jours de restauration:

day_retab = [INF]*N

def total_restore(d, rests):
    # rests: liste (r_i,t_i,x_i) pour les services déjà rétablis (r_i <= d)
    base = d
    add = 0
    for r_i, t_i, x_i in rests:
        if d <= r_i:
            continue
        di = d - r_i -1
        if di > x_i:
            di = x_i
        if di <=0:
            continue
        add += sum_acc(t_i, di)
    return base + add

# Recherche de la date de restauration d'un service i:
# on fait un bsearch sur d: on cherche minimal d tq restauration(d) >= w[i]

# Comme la restauration est start au minimum day = w[i] (sans accél), max est très grand (INF ou plus)

# Pour accélérations, chaque service accélère, donc plus on attend, plus restauration augmente, donc fonction monotone croissante sur d.

# On va chercher r_i avec binaire.

# Pour la recherche, on a besoin de connaitre les services restaurés avant i pour calculer la restauration.

# Comme w est trié, on peut aller en ordre.

rests=[] #(r_i,t_i,x_i) services restaurés précédemment

for i in range(N):
    wi, ti, xi = w[i], t[i], x[i]
    # Recherche binaire entre low et high
    low = 0
    # Upper bound: max de 3,652,425 ou plus, on prend max(wi, limit)+ max(x)
    high = max(wi, limit)+100000
    while low<high:
        mid=(low+high)//2
        val = mid # base
        add = 0
        for rj, tj, xj in rests:
            if mid <= rj:
                continue
            di = mid - rj -1
            if di > xj:
                di = xj
            if di <=0:
                continue
            add += sum_acc(tj, di)
        val += add
        if val >= wi:
            high = mid
        else:
            low = mid+1
    day_retab[i] = low
    if low > limit:
        # Ne plus stocker dans rests car ça ne contribue pas dans limite
        continue
    rests.append( (low, ti, xi) )

# Affichage jours de restauration
for d in day_retab:
    if d > limit:
        print("Many years later")
    else:
        print(d)

# Maintenant on doit répondre aux Q questions, pour y_j jours, déterminer la restauration de ce jour.

# Ici la restauration est:
# restauration(d)= d + sum_i sum_acc(t_i, max(0, d - r_i -1)) 
# avec i tel que day_retab[i] <= limit

# On a en rests uniquement stratégies d'accélération pour services installés à <= limit
# Pour optimisation, on va prefix-sum d'accélérations utiles

# Comme Q peut être 1e5, et N up to 1e5, simuler direct est trop lent O(NQ)

# On remodèle :

# restauration(d) = d + sum_{i=0}^{N-1} accel_i(d) 

# avec accel_i(d) = sum_acc(t_i, max(0, d - r_i -1)) si d >= r_i+1 else 0

# On peut trier les services par r_i (day_retab), et pour chaque d_j (les jours interrogés), 

# Il suffit de cumuler pour toutes services i avec r_i <= d_j

# On peut préparer une liste des events (r_i+1, service i) triée sur les jours

# Pour chaque query d_j, on va traiter tous les services avec r_i+1 <= d_j (accélérations commencées), from the left

# L'accélération pour un service i vaut sum_acc(t_i, min(x_i, d_j - r_i -1)) = sum_acc(t_i, min(x_i, d_j - (r_i+1) +1))

# Donc on doit pouvoir répondre à Q queries en O(Q log N)

# Plan:

# - Trier acceleration_starts = sorted list of (r_i+1, i) pour les i avec r_i<=limit

# - Pour chaque query d_j dans l'ordre croissant (d_j est croissant)

#   - On avance l'index de services dont r_i+1 <= d_j, on ajoute ces services dans une structure légère

#   - Pour tous les services activés, on calcule leur contribution accel_i(d_j)

#      - Cela peut etre O(NQ), trop lourd

# Donc il faut une autre idée:

# Observation: chacune des accélérations a un x_i ≤10^4, un fanion de jours contigus

# On peut construire une Fenwick / segment tree sur les jours avec:

# Pour tous services i, on ajoute leur accélération au segment [r_i+1, r_i+1+x_i]

# Pour chaque type t_i, les accélérations sur jours successifs sont: 1 (t=0), d (t=1), d² (t=2)

# Donc on peut modéliser la accélération comme des polynômes sur [L,R]

# Pour répondre à question d_j, on calcule:

# accel_sum(d_j) = somme sur services i actifs : accélération au jour d_j

# = somme de valeurs sur segment [0,d_j] des accelerations en lecture sur le jour d_j.

# Donc: On somme sur les x jours post r_i+1 les additions polynomiales

# On peut modéliser la somme des accélérations accumulées à la jour d_j comme la somme des valeurs des services activés à d_j

# On va représenter les accélérations cumulées sous forme de polynômes piecewise sur le temps, et répondre avec un prefix sum et précalculs.

# Méthode finale :

# On crée 3 fenwicks (BIT) pour gérer les composantes de polynômes d'ordre 2 (a*d² + b*d + c) pour tous les jours.

# Quand on active un service i de type t_i :
# - Si t=0, accélération constante : 1 sur x_i jours, 
#   ajouter +1 sur segment [L,R]: fenw_c +=1 sur intervalle
# - Si t=1, accélération linéaire : d sur x_i jours: 
#   accélération sur jour d est d-L+1
#   c'est une fonction affine sur les indices dans [L,R]:
#   on modélise: f(d) = d - L + 1 = d - (L-1)
#   d est variable -> fenw_b = 1, fenw_c = 1 - L
# - Si t=2, accélération quadratique : d² 
#   x_i elems : du jour L jusqu'à R=L + x_i -1
#   on ajoute polynôme : (d)^2
#    - on modélise a=1, b=0, c=0 sur [L,R]

# Fenwicks pour a,b,c coefficients, query d donne sum (a*d² + b*d + c)

class Fenw:
    def __init__(self,n):
        self.n=n+2
        self.f=[0]*(self.n+2)
    def add(self,i,x):
        i+=1
        while i<self.n:
            self.f[i]+=x
            i+=i&-i
    def sum(self,i):
        i+=1
        s=0
        while i>0:
            s+=self.f[i]
            i-=i&-i
        return s
    def range_add(self,l,r,x):
        self.add(l,x)
        self.add(r+1,-x)

fenw_a=Fenw(limit+100005)
fenw_b=Fenw(limit+100005)
fenw_c=Fenw(limit+100005)

def fenw_add_range_poly(L,R,a,b,c):
    # on ajoute a*x^2 + b*x + c sur [L,R] dans fenw
    # Fenw stores cumulative sums of coefficients
    # Since x is variable in query, lors de query on fera:
    # val = a*d² + b*d + c avec a,b,c = fenw sums à d
    fenw_a.range_add(L,R,a)
    fenw_b.range_add(L,R,b)
    fenw_c.range_add(L,R,c)

# On ajoute pour chaque service avec day_retab[i] <= limit son accélération sur [r_i+1, r_i+x_i]

for i in range(N):
    r=day_retab[i]
    if r>limit:
        continue
    L = r+1
    R = L + x[i] -1
    ti = t[i]
    xi = x[i]
    if ti==0:
        # constante 1 sur [L,R]
        fenw_a.range_add(L,R,0)
        fenw_b.range_add(L,R,0)
        fenw_c.range_add(L,R,1)
    elif ti==1:
        # valeur = d - (L-1) sur [L,R]
        # f(d) = d - (L-1) = 1*d + (1 - L)
        fenw_a.range_add(L,R,0)
        fenw_b.range_add(L,R,1)
        fenw_c.range_add(L,R,1 - L)
    else:
        # valeur = d^2
        # f(d) = 1*d^2 + 0*d + 0
        fenw_a.range_add(L,R,1)
        fenw_b.range_add(L,R,0)
        fenw_c.range_add(L,R,0)

def accel_val(d):
    # retourne la somme over i accelerations pour le jour d
    a = fenw_a.sum(d)
    b = fenw_b.sum(d)
    c = fenw_c.sum(d)
    return a*d*d + b*d + c

# Répondre aux requêtes y_j
# restauration(y_j) = y_j + accel_val(y_j)
for d in y:
    res= d + accel_val(d)
    print(res)