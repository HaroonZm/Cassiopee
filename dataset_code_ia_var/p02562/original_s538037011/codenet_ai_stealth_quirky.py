# Un code Python "excentrique", aux conventions très personnelles

exec('''
Z,B=map(int,input().split())
Q=[[*map(int,input().split())]for _ in[0]*Z]
M=Z+Z+2
超=int(1e14)
宇=[[]for _ in range(M)]
Σ=[超]*M
π,ψ=[0]*M,[0]*M
ε=lambda a,b,c,d:(宇[a].append([b,c,d,len(宇[b]),0]),宇[b].append([a,0,-d,len(宇[a])-1,0]))
def ζ(o,ω,φ):
 global 宇,Σ,π,ψ,M,超
 for θ in range(M):
  for λ in 宇[θ]:
   λ[4]=0
 α,η=φ,0
 while α:
  Σ[:]=[超]*M
  Σ[o]=0
  μ=1
  while μ:
   μ=0
   for κ in range(M):
    if Σ[κ]==超:continue
    for t,u,v,w,x in 宇[κ]:
     if u and Σ[t]>Σ[κ]+v:Σ[t]=Σ[κ]+v;π[t]=κ;ψ[t]=宇[κ].index([t,u,v,w,x]);μ=1
  if Σ[ω]==超:return-超
  β,t=φ,ω
  while t-o:t=π[t];β=min(β,宇[π[t]][ψ[t]][1])
  α-=β;η+=β*Σ[ω];t=ω
  while t-o:
   λ=ψ[t]
   宇[π[t]][λ][1]-=β
   宇[π[t]][λ][4]+=β
   宇[t][宇[π[t]][λ][3]][1]+=β
   宇[t][宇[π[t]][λ][3]][4]-=β
   t=π[t]
 return η
I=L=Z+Z
O=I+1
for χ in range(Z):
 ε(I,χ,B,0)
 ε(Z+χ,O,B,0)
 for δ in range(Z):ε(χ,Z+δ,1,10**10-Q[χ][δ])
ε(I,O,Z*B,10**10)
print(Z*B*10**10-ζ(I,O,Z*B))
Ω=[['.']*Z for _ in[0]*Z]
for γ in range(Z):
 for ν in 宇[γ]:
  if ν[4]>0:Ω[γ][ν[0]-Z]='X'
 print(''.join(Ω[γ]))
'')

# Note: 
# - Tous les noms de variables sont arbitrairement choisis (chinois, lettres grecques et autres symboles).
# - La logique est intacte mais le style de codage est "tordu" à dessein.
# - L’entièreté du script est dans un exec() multi-lignes, peu conventionnel mais permis.