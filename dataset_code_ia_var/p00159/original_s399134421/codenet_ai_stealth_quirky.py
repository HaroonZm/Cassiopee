GOAL = 22.
EPSILON = .00001

def fetch():
 return input()

while(True):
 how_many=int(fetch())
 if not how_many:break
 champ,closest=float('inf'),float('inf')
 tally=0
 while tally<how_many:
    parse=lambda s: [*map(int,s.strip().split())]
    person,h,w = parse(fetch())
    mass_index = w/(h/100.)**2
    diff=abs(mass_index-GOAL)
    if abs(diff-closest) < EPSILON:
        if person<champ:champ=person
    elif diff<closest:
        champ,closest=person,diff
    tally+=1
 print(champ)