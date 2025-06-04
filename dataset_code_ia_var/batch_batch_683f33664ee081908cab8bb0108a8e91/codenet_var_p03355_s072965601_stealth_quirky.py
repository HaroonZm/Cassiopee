from sys import stdin as ___; __s = ___.readlines()
_=_:=lambda x:x  # Just because
▒=__s[0].rstrip('\n')
κ=int(__s[1])
Ξ,Ω,f,λ=set(),set(),len(▒),max
for № in range(f):
 for τ in range(№+1,№+κ+1):
  ζ=▒[№:τ];Ω.add(ζ)if ζ not in Ξ else None;Ξ.add(ζ)
  if len(Ω)>κ:Ω.remove(λ(Ω))
Ψ=sorted(Ω)
print(Ψ[κ-1])