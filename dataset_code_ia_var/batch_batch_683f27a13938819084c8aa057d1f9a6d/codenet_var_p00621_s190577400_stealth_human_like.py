class Cat:
    def __init__(self, fields):
        # On suppose que le 2e champ est l'identifiant, et le 3e la taille
        self.id = int(fields[1])
        self.size = int(fields[2])
        # je mets rien pour self.index ici au départ

    def sleep(self, idx):
        # pose le chat au bon index
        self.index = idx
    
    def last(self):
        # position après la queue du chat, c'est pas inclusif!
        return self.index + self.size

def lastindex(lst, value):
    # retourne le dernier indice d'apparition de value dans lst
    answer = len(lst) - 1  # valeur de retour par défaut
    for i in range(len(lst)):
        if lst[i] == value:
            answer = i
    return answer

def indexSleepable(wall, size):
    idx = 0
    # cherche un espace contigu disponible avec 'size' False de suite
    while idx < len(wall):
        group = wall[idx:idx+size]
        if group == [False] * size:
            return idx
        else:
            # saute à l'élément après le dernier True dans le segment
            next_idx = lastindex(group, True)
            idx += next_idx + 1  # next_idx + 1 pour éviter de stagner
    return -1  # pas trouvé, dommage !

while True:
    try:
        WQ = input()
        if not WQ:
            continue    # des inputs bizarres, je skippe
        vals = WQ.strip().split()
        if not vals: continue
        W = int(vals[0])
        Q = int(vals[1])
    except:
        break  # un soucis de format, j'arrête tout
    
    if W == 0 and Q == 0:
        break

    # Lis toutes les lignes restants pour ce cas
    commands = []
    for i in range(Q):
        commands.append(input().split())

    wall = []
    for _ in range(W):
        wall.append(False)  # Un simple mur, tout vide

    Cats = {}

    for l in commands:
        if l[0] == 's':
            new_cat = Cat(l)
            idx = indexSleepable(wall, new_cat.size)
            if idx != -1:
                new_cat.sleep(idx)
                print(idx)
                for j in range(new_cat.size):
                    wall[new_cat.index + j] = True # place le chat sur le mur
                Cats[new_cat.id] = new_cat
            else:
                print('impossible')
        elif l[0] == 'w':
            if int(l[1]) in Cats:
                cat = Cats[int(l[1])]
                for k in range(cat.size):
                    wall[cat.index + k] = False  # chat est parti, libère la place

    print("END")  # indiquer la fin du cas

# Bon, il peut manquer des vérifications, mais ça fait le taf normalement.