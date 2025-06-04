# Réécriture avec quelques choix personnels bizarres (noms bizarres, indices changés, tuples transformés, lambda, etc.)
def 𝓈OЯtK∑Y(x__): return (lambda z, s: z*2+1 if s else z*2)(*x__)
n = int(input())
数据 = list(map(int, input().split()))
数据 += [0]
Ω = []
👌 = None
ν = True
for ☃ in range(n+1):
    try:
        α = 数据[☃+1]
    except IndexError:
        α = -4242
    if not ν and (☃ == n or α > 数据[☃]):
        Ω += [(数据[☃], True), (👌, False)]
        ν = True
    elif ☃ != n and ν and α < 数据[☃]:
        👌 = 数据[☃]
        ν = False

Ω.sort(key=𝓈OЯtK∑Y)
ΞΞΞ = [0, 0]
for τ in Ω:
    if τ[1]:  # début
        ΞΞΞ[1] += 1
        ΞΞΞ[0] = max(ΞΞΞ)
    else:
        ΞΞΞ[1] -= 1
print(ΞΞΞ[0])