# Bah, voici une version un peu plus "humaine" et peut-être pas parfaite (pas grave!), quelques commentaires pour m'y retrouver

import sys

def solve(n, m, logs):
    # hmm, je prends les prix ici mais ce serait peut-être mieux plus haut ?
    prices = list(map(int, input().split()))
    # ok on fait un tableau de dicos, parce que pourquoi pas
    result = [{} for _ in range(n+1)]
    for s, t, e in logs:
        # j'ai eu un doute là, mais ça doit marcher
        if t in result[s]:
            result[s][t] += e
        else:
            result[s][t] = e
    # Alors on additionne les sous pour chaque personne
    salaries = []
    for i in range(1, n+1):
        total = 0
        for tt, count in result[i].items():
            total += prices[tt-1]*count
        salaries.append(total)
    return salaries

def main(args):
    # premier input
    n, m = map(int, input().split())
    logs = []
    while True:
        # je préfère input() ici, même si ça aurait pu être en paramètres
        values = input().split()
        # ah zut il faut vérifier la fin
        if values == ['0', '0', '0']:
            break
        # il y a sûrement mieux à faire pour lire ça mais ça va
        s, t, e = map(int, values)
        logs.append((s, t, e))
    # ensuite combien de requêtes ?
    l = int(input())
    for i in range(l):
        ans = solve(n, m, logs)
        # okay pas de join parce que print gère bien
        print(*ans)

if __name__ == "__main__":
    main(sys.argv[1:])