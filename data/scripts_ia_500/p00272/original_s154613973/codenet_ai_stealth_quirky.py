_dict = {1:6000,2:4000,3:3000,4:2000}

class Multiplier:
    def __init__(self, d):
        self.dico = d
    def __call__(self, key, times):
        return self.dico[key]*times

_m = Multiplier(_dict)

i=0
while i<4:
    a,b = input(">").split()
    print(_m(int(a),int(b)))
    i+=1