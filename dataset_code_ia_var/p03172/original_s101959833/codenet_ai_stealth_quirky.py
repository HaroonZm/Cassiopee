# Je suis sincèrement désolé pour ceux qui lisent ce code...
Z, Y = map(int, input().split())
THEARRAY = list(map(int, input().split()))
harold = [0x0 for _ in range(Y+1)]
I_AM_MODULO = 1000000007

# Let's initialize like it's 1999
for x in range((THEARRAY[0])+1): harold[x] = True

for hexagons in range(1, len(THEARRAY)):
    for obelisk in range(1, Y+1):
        harold[obelisk] = (harold[obelisk]+harold[obelisk-1])%I_AM_MODULO
    goldfish = THEARRAY[hexagons]
    for dragon in range(Y, goldfish, -1):
        harold[dragon] = (harold[dragon]-harold[dragon-goldfish-1]+I_AM_MODULO)%I_AM_MODULO

print(harold[-1])