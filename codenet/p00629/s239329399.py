def team_sort(teams, n):
    for i in range(n - 1):
        #print(i)
        for j in range(n - i - 1):
            #print(i, j, teams[j][2], teams[j+1][2])
            if (teams[j][2] < teams[j + 1][2]):
                tmp = teams[j]
                teams[j] = teams[j+1]
                teams[j+1] = tmp
            elif (teams[j][2] == teams[j + 1][2]):
                if (teams[j][3] > teams[j + 1][3]):
                    tmp = teams[j]
                    teams[j] = teams[j+1]
                    teams[j+1] = tmp
                elif (teams[j][3] == teams[j + 1][3]) and (teams[j][0] > teams[j + 1][0]):
                    tmp = teams[j]
                    teams[j] = teams[j+1]
                    teams[j+1] = tmp

def select(teams):
    selection = []
    count = {}
    for t in teams:
        g = str(t[1])
        count.setdefault(g, 0)
        #print(t)
            
        if len(selection) < 10:
            if (count[g] < 3):
                selection.append(t)
                count[g] += 1
        
        elif len(selection) < 20:
            if (count[g] < 2):
                selection.append(t)
                count[g] += 1
        
        elif len(selection) < 26:
            if (count[g] < 1):
                selection.append(t)
                count[g] += 1
    #print('selection', selection)
    
    for t in selection:
        print(t[0])

while True:
    n = int(input())
    
    if (n == 0):
        break
    
    teams = []
    
    for i in range(n):
         t = [int(x) for x in input().split()]
         teams.append(t)
    #print(teams)
    team_sort(teams, n)
    #print('sorted', teams)
    select(teams)