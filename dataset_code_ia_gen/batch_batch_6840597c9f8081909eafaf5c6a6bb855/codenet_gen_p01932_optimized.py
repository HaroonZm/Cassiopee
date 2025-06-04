import sys
input=sys.stdin.readline

N,D=map(int,input().split())
people=[tuple(map(int,input().split())) for _ in range(N)]

# Vérification si un étage est hors limite raisonnable (plus d'un million, à partir de la contrainte)
# Et pré-tri par étage pour traiter par groupes au même étage
people.sort(key=lambda x:x[1])

from collections import defaultdict
floor_groups=defaultdict(list)
for t,f in people:
    floor_groups[f].append(t)

# Le chariot commence à l'étage 1 à t=0.
# Plan: pour chaque étage f (croissant), on doit ramener tout le monde du groupe.
# On part du principe que l'ascenseur descend à 1 dès qu'un groupe est pris.
# On doit transporter par groupes de taille <= D.
# Pour chaque groupe, il faut:
#   - arriver à l'étage f au moment max du t_i des personnes qui embarquent (ou plus tard)
#   - si l'ascenseur arrive trop tôt, on attend.
# Le temps de transport pour cette sortie est: (f-1)*nombre_de_personnes_du_groupe (car c’est le temps que chaque personne passe dans l’ascenseur).

# On va simuler l’ascenseur étage par étage, groupe par groupe, sans retourner en arrière entre deux groupes d’un même étage.

current_time=0
current_floor=1
total_time=0

for f in sorted(floor_groups):
    times=floor_groups[f]
    # Diviser en groupes de taille D max
    for i in range(0,len(times),D):
        group=times[i:i+D]
        max_t=max(group)
        # Aller à l'étage f (depuis current_floor)
        arrive_time = current_time + abs(f - current_floor)
        # L'ascenseur doit être là au max entre arrive_time et max_t
        start_time=max(arrive_time,max_t)
        # Si on est trop tôt / tard on attend/part
        # S'il est impossible de charger quelqu'un (t_i > start_time), alors pas pris, donc volé en escalier: return -1
        for t_person in group:
            if t_person > start_time:
                print(-1)
                sys.exit()
        # cumuler le temps: (f-1) * nombre de personnes embarquées
        total_time+=(f-1)*len(group)
        # L'ascenseur revient forcément au 1er étage avant de reprendre cet itinéraire, on suppose qu'il revient à 1 avant le prochain groupe
        # Mais on devons mettre à jour current_floor et current_time pour le prochain groupe
        # Le temps de descente du groupe: (f-1)
        current_time=start_time + (f-1)  # descente du groupe à 1er étage
        current_floor=1

print(total_time)