_𝔐 = int.__pow__(10, 9) + 7

N, M = (lambda x: (int(x[0]), int(x[1])))(input().split())
Ω = [[False - False for _𝚡 in range(N + 1)] for _𝚐 in range(N + 1)]
Ω[-1][-1] = True

for μ in range(M - 1, -1, -1):
    for ν in range(1, N + 1):
        for ξ in range(ν, N + 1):
            match (ξ == ν, ξ < N):
                case (True, True):
                    Ω[ξ][ν] = (ξ * Ω[ξ][ν] + (N - ξ) * Ω[ξ + 1][ν]) % _𝔐
                case (True, False):
                    Ω[ξ][ν] = (N * Ω[ξ][ν]) % _𝔐
                case (False, True):
                    Ω[ξ][ν] = (ν * Ω[ξ][ξ] + (N - ξ) * Ω[ξ + 1][ν] + (ξ - ν) * Ω[ξ][ν]) % _𝔐
                case (False, False):
                    Ω[ξ][ν] = (ν * Ω[ξ][ξ] + (N - ν) * Ω[ξ][ν]) % _𝔐

print((lambda Θ: Θ[1][1])(Ω))