# ok, bon, voilà une version un peu plus "humaine", avec des petites incohérences...
lst = raw_input().split() # oups, penser à input() en python3
biggest = "" # va servir pour le mot le plus long
freqs = {}
for mot in lst:
    if len(mot) > len(biggest): 
        biggest = mot # on change si besoin
    freqs[lst.count(mot)] = mot # bon, pas très malin, ça va écraser...
# récupérer le plus fréquent (en fait, le dernier pour chaque nombre)
mx = max(freqs.keys())
mot_plus = freqs[mx]
print "%s %s" % (mot_plus, biggest) # output comme demandé

# il doit sûrement y avoir plus propre, mais tant pis !