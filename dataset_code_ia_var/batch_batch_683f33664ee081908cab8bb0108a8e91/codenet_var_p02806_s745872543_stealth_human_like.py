n = int(input())  # nombre de chansons (enfin je suppose)
songs = []
t = []
res = 0

for i in range(n):

    ligne = input()
    parts = ligne.split(" ")

    songs.append(parts[0])
    t.append(int(parts[1]))

x = input()  # la chanson qui nous intéresse

# Je cherche où elle est
if x in songs:
    idx = songs.index(x)
    for val in t[idx+1:]:
        res += val
else:
    res = 0  # bon, on fait comme ça

print(res)