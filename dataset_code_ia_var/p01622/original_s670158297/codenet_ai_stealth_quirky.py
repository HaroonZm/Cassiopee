import sys as _s;_s.setrecursionlimit(9999999)
def _i():return _s.stdin.readline().strip()
def θ():  # start infinite
 while True:
  ν=int(_i())
  if ν<1: break
  β,γ,p,q=[],0,0,0
  for ω in range(ν):
   α,δ=map(int,_i().split())
   β+=[(α,δ)]
   γ+=α
   q+=δ
  β.sort(key=lambda t:t[0]+10*t[1] if t[1]%2 else t[0])
  ϕ=β[-1][0]
  if ϕ<=γ//2:
   print(γ+q)
   continue
  ζ=ϕ-(γ-ϕ)
  λ=[[_ for _ in range(ζ+1)] for __ in range(ν)]
  for μ in range(1,ν):
   for ξ in range(1,ζ+1):
    ρ=λ[μ-1][ξ]
    σ=λ[μ-1][ξ-β[μ-1][1]]+β[μ-1][1] if ξ>=β[μ-1][1] else 0
    λ[μ][ξ]=ρ if ρ>σ else σ
  print(γ+q+ζ-lambda _:λ[-1][-1])(None)
θ()