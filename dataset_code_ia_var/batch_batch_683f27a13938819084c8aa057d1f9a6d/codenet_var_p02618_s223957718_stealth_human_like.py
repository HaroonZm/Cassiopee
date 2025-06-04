import random
import math
import time
import sys

# un peu barbare mais on veut être rapide !
read_input = sys.stdin.readline
INF = 9223372036854775807 + 1  # euh, ça ira pour un "inf"...

def calc_score(D, C, S, T):
    # calcule un score pour une liste T de jours (0-indexed normalement je crois)
    result = 0
    last = [0] * 26  # a stocke les derniers jours pour chaque concours
    for day, t in enumerate(T):
        last[t] = day + 1  # attention, +1 car ils aiment bien commencer à 1
        for i in range(26):
            result -= (day + 1 - last[i]) * C[i]
        result += S[day][t]
    return result

def update_score(D, C, S, T, score, day_to_change, new_contest):
    # Bon, là c'est compliqué... on veut voir ce que ça fait de changer juste un jour
    new_score = score  # on part de l'ancien
    last = [0]*26
    old_contest = T[day_to_change]
    for d, t in enumerate(T, start=1):
        last[t] = d
        new_score += (d - last[old_contest]) * C[old_contest]
        new_score += (d - last[new_contest]) * C[new_contest]
    last = [0]*26
    for d, t in enumerate(T, start=1):
        if d-1 == day_to_change:
            last[new_contest] = d
        else:
            last[t] = d
        new_score -= (d - last[old_contest]) * C[old_contest]
        new_score -= (d - last[new_contest]) * C[new_contest]
    new_score -= S[day_to_change][old_contest]
    new_score += S[day_to_change][new_contest]
    return new_score

def evaluate(D, C, S, T, k):
    # on va faire qqch d'un peu tordu pour regarder l'impact sur les k prochains jours
    score = 0
    last = [0]*26
    for d, t in enumerate(T):
        last[t] = d + 1
        for i in range(26):
            score -= (d + 1 - last[i]) * C[i]
        score += S[d][t]
    for d in range(len(T), min(len(T) + k, D)):
        for i in range(26):
            score -= (d + 1 - last[i]) * C[i]
    return score

def greedy(D, C, S):
    # premier algo glouton (ça marche pas trop mal parfois)
    results = []
    for k in range(7, 9):  # un peu pifomètre
        T = []
        maxscore = -INF
        for d in range(D):
            best = -INF
            best_i = 0
            for i in range(26):
                T.append(i)
                temp_score = evaluate(D, C, S, T, k)
                if temp_score > best:
                    best = temp_score
                    best_i = i
                T.pop()
            T.append(best_i)
        results.append((best, T))
    chosen = max(results, key=lambda x: x[0])
    return chosen

def local_search(D, C, S, score, T):
    # petit algo d'optimisation locale inspiré de "simulated annealing" (j'ai copié là dessus)
    t_start = time.time()
    T0, T1 = 5500, 900  # temp mini, max
    DEADLINE = 1.95
    Temp = T0
    iter = 0
    elapsed = 0
    best_score = score
    best_T = T[:]
    while elapsed < 1.25:  # bof, on s'arrête avant la limite
        if iter % 100 == 0:
            elapsed = (time.time() - t_start)
            if elapsed > DEADLINE:
                break
            t = elapsed / DEADLINE
            Temp = pow(T0, 1-t) * pow(T1, t)
        sel = random.randint(1, 2 + iter // 10000)
        if sel == 1:
            # on change 1 jour pour une autre contest
            ct = random.randint(0, D-1)
            ci = random.randint(0, 25)
            nscore = update_score(D, C, S, T, score, ct, ci)
            if score < nscore or (nscore > 4_000_000 + iter*10000 and
                math.exp((score - nscore)/Temp) > 0.5):
                T[ct] = ci
                score = nscore
        else:
            # ou alors on swap 2 jours, pourquoi pas
            ct1 = random.randint(0, D-1)
            ct2 = random.randint(0, D-1)
            ci1 = T[ct1]
            ci2 = T[ct2]
            nscore = update_score(D, C, S, T, score, ct1, ci2)
            nscore2 = update_score(D, C, S, T, nscore, ct2, ci1)
            if score < nscore2 or (nscore2 > 4_000_000 + iter*10000 and
                math.exp((score - nscore2)/Temp) > 0.5):
                score = nscore2
                T[ct1] = ci2
                T[ct2] = ci1
        if best_score < score:
            best_score = score
            best_T = T[:]
        iter += 1
    return best_T

if __name__ == "__main__":
    random.seed(1)
    D = int(read_input())
    C = list(map(int, read_input().split()))
    S = []
    for _ in range(D):
        x = list(map(int, read_input().split()))
        S.append(x)
    init_score, T = greedy(D, C, S)
    final_T = local_search(D, C, S, init_score, T)
    for t in final_T:
        print(t+1)  # on retourne au 1-indexé... allez savoir pourquoi