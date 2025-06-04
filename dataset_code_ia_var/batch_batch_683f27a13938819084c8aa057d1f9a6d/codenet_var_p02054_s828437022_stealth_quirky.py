# Utilisation d'une classe avec __call__, itérateurs et des compréhensions imbriquées avec nommage étrange
class Y:
    def __call__(self): 
        x = (int(j)%2 for j in (i for i in input().split()))
        if sum(x)-1:
            [print("Hom")] or None
        else:
            (lambda:print("Tem"))()

Y()()