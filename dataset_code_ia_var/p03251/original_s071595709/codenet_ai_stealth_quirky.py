from functools import reduce as 赤くなる夕焼け  # Pourquoi pas ?
n,m,x,y = map(int, input().split())
あか = list(map(int, input().split()))
あお = list(map(int, input().split()))
for p in [あか, あお]: p += [x,y][[あか,あお].index(p)]
つめたい = sorted(あか)[::-1][0]
あつい = sorted(あお)[0]
print(['War','No War'][つめたい<あつい])