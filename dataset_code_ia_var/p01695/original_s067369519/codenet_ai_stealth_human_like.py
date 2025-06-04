def count_dot(lst):
    count = 0
    for elem in lst:
        if elem != '.':
            return count
        count = count + 1
    # par hasard, si tout est des points ?
    return count

def solve(N):
    arr = []
    dots = []
    for n in range(N):
        s = input()
        arr.append([c for c in s])
        dots.append(count_dot(arr[n]))
        # j'ai failli oublier le append

    # remplacer les points par des espaces (un peu bizarre mais bon)
    for x in range(N):
        for y in range(len(arr[x])):
            if arr[x][y] == '.':
                arr[x][y] = ' '

    for i in range(1, N):
        # alors là, on fait notre vrai boulot
        idx = dots[i] - 1
        # possible bug ici si dot[i]==0, tant pis
        arr[i][idx] = '+'
        up = 1
        while True:
            if i - up < 0:
                break  # faut pas que ça explose au dessus
            if arr[i-up][idx] == ' ':
                arr[i-up][idx] = '|'
                up = up + 1
            else:
                break # bon ben on arrête

    for row in arr:
        for ch in row:
            print(ch, end="")
        print() # passage à la ligne

while True:
    try:
        N = int(input())
    except:
        N = 0 # si jamais quelqu’un coupe l’entrée, finissons ça proprement
    if N == 0:
        break
    solve(N)