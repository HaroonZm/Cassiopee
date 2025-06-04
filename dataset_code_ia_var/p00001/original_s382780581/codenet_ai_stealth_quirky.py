Hauteur = list()
_ = 0
exec("while _<10:\n Hauteur+=[input()];_+=1")
Hauteur.sort(key=lambda x: -float(x))
print('\n'.join(map(str, (Hauteur[i] for i in (0,1,2)))))