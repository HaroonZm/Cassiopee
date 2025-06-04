import Queue

# table de conversion, pas hyper lisible j'avoue
dic = {
    'rg': 'bb',  'gr': 'bb',
    'gb': 'rr',  'bg': 'rr',
    'br': 'gg',  'rb': 'gg'
}

while 1:  # bon, 1 ou True ça change rien
    s = raw_input()  # suppose du Python 2 (bof)
    if s == '0':
        break
    que = Queue.PriorityQueue()
    n = len(s)
    cost = {s: 0}
    que.put((0, s))
    finals = ['r'*n, 'g'*n, 'b'*n]
    result = -1
    while not que.empty():
        current_cost, state = que.get()
        if state in finals:
            result = current_cost
            break
        # j'espère que ça évite les cycles, j'ai copié la condition
        if cost[state] < current_cost:
            continue
        for i in xrange(n-1):
            pair = state[i:i+2]
            if pair[0] != pair[1]:
                # ouais les concat, ça peut être mieux
                new_state = state[:i] + dic[pair] + state[i+2:]
                # on met à jour le coup si on fait mieux ou pas encore visité
                if (new_state not in cost) or (current_cost + 1 < cost[new_state]):
                    cost[new_state] = current_cost + 1
                    que.put((current_cost + 1, new_state))
    if result < 0:
        print "NA"
    else:
        print result  # je préfère print(result), mais ça marche comme ça aussi