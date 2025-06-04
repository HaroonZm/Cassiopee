teams = []
while True:
    line = input()
    if line == '':
        break
    p_s = line.split(',')
    p = int(p_s[0])
    s = int(p_s[1])
    if p == 0 and s == 0:
        break
    teams.append((p, s))

# extraire les scores pour calculer les rangs
scores = [score for (p, score) in teams]
scores_sorted = sorted(list(set(scores)), reverse=True)

# dictionnaire score -> rang (1, 2, 3 ...)
rank_dict = {}
rank = 1
for sc in scores_sorted:
    rank_dict[sc] = rank
    rank += 1

# dictionnaire p -> score pour recherche facile
team_score = {}
for (p, s) in teams:
    team_score[p] = s

try:
    while True:
        query = input()
        if query == '':
            break
        q = int(query)
        if q in team_score:
            print(rank_dict[team_score[q]])
        else:
            print("No data")
except EOFError:
    pass