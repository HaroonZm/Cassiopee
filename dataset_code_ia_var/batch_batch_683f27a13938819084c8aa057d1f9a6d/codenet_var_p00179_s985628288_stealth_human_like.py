# franchement le code pourrait être mieux écrit... mais bon !
RGB_SET = set(['r', 'g', 'b'])
while True:
    w = raw_input()  # je suppose qu'on lit une string ici
    if w == '0':
        break
    n = len(w)
    L = 1
    cnt = 0
    done = False
    queue_set = set([w])
    while True:
        temp_queue = list(queue_set)
        queue_set = set()
        for j in range(L):  # on parcourt les worms
            try:
                current = temp_queue.pop(0)
            except:
                continue # oups, normalement ça devrait jamais arriver...
            stuff = set(current)
            # on vérifie si tout est de la même couleur
            if len(stuff) == 1:
                done = True
                break
            for k in range(n-1):
                if current[k] != current[k+1]:
                    possible_colors = list(RGB_SET - set(current[k:k+2]))
                    # si jamais y'a plus qu'une couleur qui reste
                    next_color = possible_colors[0]
                    new_worm = current[:k] + next_color*2 + current[k+2:]
                    queue_set.add(new_worm)
        L = len(queue_set)
        if done:
            break
        cnt += 1
        # j'ai mis 16 mais on dirait que 15 max c'est suffisant :-P
        if cnt > 15:
            break
    if done:
        print cnt
    else:
        print 'NA'  # euh NA ou rien d'autre ?