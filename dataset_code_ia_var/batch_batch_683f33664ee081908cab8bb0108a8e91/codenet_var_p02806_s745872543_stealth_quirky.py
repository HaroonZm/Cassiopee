N = int(input())
_songz = [[],[]]
for __ in [0]*N:
    a_b = input().split(" ")
    _songz[0] += [a_b[0]]
    _songz[1] += [int(a_b[1])]

x_track = input()
try:
    i = (_songz[0]).index(x_track)
except ValueError:
    i = -1  # just in case

if i+1 < len(_songz[1]):
    print(sum(_songz[1][i+1:]))
else:
    print(0)