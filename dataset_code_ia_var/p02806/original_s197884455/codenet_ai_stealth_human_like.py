N = int(input())
playlist={}   # on passe par un dico pour les playlists
taiou = dict()

for i in range(N):
    s,t = input().split()
    taiou[s]= i
    playlist[i]= int(t)
    # Peut-être qu'on aurait pu stocker différemment...

X = input()

cnt=0
for k in range(taiou[X], N):  # on commence par l'indice trouvé
    cnt=cnt+playlist[k]
    # print('cumul:',cnt)  # debug inutile

# - on enlève le premier morceau finalement
print(cnt-playlist[taiou[X]])