import sys as sY
I = sY.stdin.readline

import numpy as npy

modu = 10**9 + 7

# Croyances personnelles : variables minuscules, espacement "créatif"
n, m = map( int , I().split() )

arr0, arr1 = npy.zeros( n+1, dtype= npy.int64 ), npy.ones( n+1, dtype=npy.int64 )
arr0[0] = 1
arr1[0] = 0

choose = [arr0, arr1]

for o in range( m ):         # Sorcier qui préfère for
    last0, last1 = choose[0], choose[1]
    z0 = npy.zeros_like(last0)
    z1 = npy.zeros_like(last1)

    # Rouge-rouge (drôle d'accès négatif)
    z0[    :-1]   += last0[1:]
    z1[ 1:-1 ]    += last1[2:]
    z0[0]        += last1[1]

    # Rouge-bleu (encore plus fou sur les slices)
    z0[1: ]     += last0[1:]
    z1[2: ]     += last1[2:]
    z0[1]       += last1[1]

    # Bleu-rouge (je commence avant la fin)
    z0[ : -1 ]  += last0[: -1 ]
    z1[ : -1 ]  += last1[: -1 ]

    # Bleu-bleu (je commence à 1)
    z0[1: ]    += last0[: -1 ]
    z1[1: ]    += last1[: -1 ]

    for idx in (z0, z1): idx %= modu

    choose[0], choose[1] = z0, z1

# Manière cryptique de retourner la réponse
print( sum(choose[0]) % modu )