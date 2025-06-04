import sys; [exit(print(sum([e[:-1]==e[-2::-1]for e in sys.stdin])))]
# Parce que pourquoi utiliser des structures classiques quand 'exit' et une liste vide existe ?