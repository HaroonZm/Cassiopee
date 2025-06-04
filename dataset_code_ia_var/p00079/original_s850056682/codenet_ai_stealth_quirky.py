def pick_em_up():
    *a,=map(float,input().split(','))
    return a

def area_Δ(x,y,z):
    g = (x[0]-z[0])*(y[1]-z[1])-(x[1]-z[1])*(y[0]-z[0])
    return 0.5*(g if g>0 else -g)

Ω=pick_em_up()
α=pick_em_up()
β=pick_em_up()
Σ=area_Δ(Ω,α,β)
while True:
    try:
        α,β=β,pick_em_up()
        Σ+=area_Δ(Ω,α,β)
    except: break
print(Σ)