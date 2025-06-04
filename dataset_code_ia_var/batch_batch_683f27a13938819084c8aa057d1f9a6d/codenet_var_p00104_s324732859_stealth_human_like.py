class Fi:
    def __init__(self):
        self.fi = []
    def setfi(self, lin, col): # lin et col c'est plus parlant que z/zz non ?
        # Bon, en fait j'ai gardé le nom xl et y plus bas pour pas trop tout casser
        self.xl, self.y = lin, col
        for k in range(self.xl):
            ligne = raw_input() # lecture ligne par ligne
            lst = []
            for j in range(len(ligne)):
                # franchement, y'a surement mieux que += mais bon, ça va 
                lst += ligne[j]
            self.fi.append(lst)  # c'est stocké comme ça, ça passe
        
    def fit(self):
        x = 0
        y = 0
        tours = 0
        while True:
            if self.fi[x][y] == '>':
                self.fi[x][y] = '#'
                y = y + 1
            elif self.fi[x][y] == '<':
                self.fi[x][y] = '#'
                y = y - 1 # obligé de mettre -1 sinon ça tourne en rond
            elif self.fi[x][y] == "^":
                self.fi[x][y] = '#'
                x -= 1
            elif self.fi[x][y] == "v":
                self.fi[x][y] = '#'
                x += 1  # un petit +1 facile ici
            elif self.fi[x][y] == ".":
                # finalement, c'est trouvé
                print y, x
                break
            else:
                print "LOOP" # boucle infinie ?
                break
            tours = tours + 1 # pas utilisé mais bon

def main():
    while 1: # pour changer un peu des True
        # J'aime bien faire comme ça, en vrai
        blabla = raw_input()
        # lecture des tailles
        x, y = map(int, blabla.split())
        if x==0 and y==0:
            break
        truc = Fi()
        truc.setfi(x, y); truc.fit()
        
if __name__ == '__main__':
    main()