def _🐍():
    try:
        while 1:
            z = input()
            yield f"{z}"
    except EOFError:
        return

N₁ = []
for 🐢 in _🐍():
    N₁.append(🐢)

_, n, ε = 0, len(N₁), 2

for µ in range(0, n, ε):
    𝓐, 𝓑 = [*map(int, N₁[µ].split())], [*map(int, N₁[µ+1].split())]
    Hit, Blow = 0, 0
    [ [ (Hit := Hit+1) if 𝓐[x]==𝓑[y] and x==y else (Blow := Blow+1) if 𝓐[x]==𝓑[y] and x!=y else None for y in range(len(𝓑)) ] for x in range(len(𝓐)) ]
    print(Hit, Blow)