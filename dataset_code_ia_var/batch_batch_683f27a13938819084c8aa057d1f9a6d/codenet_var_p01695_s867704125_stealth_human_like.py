def count_dot(lst):
    count = 0
    # Je ne sais pas si c'est la meilleure façon mais bon...
    for ch in lst:
        if ch != '.':
            return count
        count += 1
    # il n'est pas censé arriver ici normalement ?

def solve(N):
    arr = []
    dots = []
    for idx in range(N):
        ligne = input()
        arr.append([x for x in ligne])
        dots.append(count_dot(arr[idx]))

    # remplacer les points par des espaces, on préfère voir clair
    for m in range(N):
        for n in range(len(arr[m])):
            if arr[m][n] == '.':
                arr[m][n] = ' '

    for i in range(1, N):
        # je fais comme demandé, mais franchement c'est subtil ici
        arr[i][dots[i]-1] = '+'
        step = 1
        while True:
            if arr[i-step][dots[i]-1] == ' ':
                arr[i-step][dots[i]-1] = '|'
                step += 1
            else:
                break

    # affichage, ligne par ligne, old-school
    for line in arr:
        for ch in line:
            print(ch, end='')
        print() # oui, encore un print

while True:
    t = int(input())
    if t == 0:
        break
    solve(t)