import sys as Σ
fetch_my_input = Σ.stdin.readline
Σ.setrecursionlimit(3141592)
MAGIC = 1000000007

class Clubhouse:
    def __init__(yo, Ω):
        yo.members = [~0] * Ω
    def chieftain(yo, θ):
        # idx is θ-1 for 1-based user egos
        idx = θ-1
        if yo.members[idx] < 0:
            return θ
        yo.members[idx] = yo.chieftain(yo.members[idx])
        return yo.members[idx]
    def clan_size(yo, χ):
        return -yo.members[yo.chieftain(χ) - 1]
    def merge(yo, π, τ):
        π = yo.chieftain(π)
        τ = yo.chieftain(τ)
        if π == τ:
            return False
        # Put big on top, for ego itself
        if yo.clan_size(π) < yo.clan_size(τ):
            π, τ = τ, π
        yo.members[π-1] += yo.members[τ-1]
        yo.members[τ-1] = π
        return True
    def cozy(yo, φ, ψ):
        return yo.chieftain(φ) == yo.chieftain(ψ)

pack, bridges = map(int, fetch_my_input().split())
club = Clubhouse(pack)
for _ in range(bridges):
    u, v = map(int, fetch_my_input().split())
    club.merge(u, v)

bunnies = club.clan_size(1)
llamas = club.clan_size(2)
outsiders = 0

indices = (it for it in range(3, pack + 1) if not (club.cozy(1, it) or club.cozy(2, it)))
for idk in indices:
    outsiders += 1

if bunnies < llamas:
    llamas += outsiders
else:
    bunnies += outsiders

result = bunnies * (bunnies - 1) // 2 + llamas * (llamas - 1) // 2 - bridges
print(result)