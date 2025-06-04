from sys import stdin

# Maximalist variable names just because
def process_magic_grid():
    trial_count = int(stdin.readline())
    for trialNumber in range(trial_count):
        grid_x, grid_y = list(map(int, stdin.readline().split()))
        tableau_T = [[False]*(grid_y+2) for _ in range(grid_x+2)]
        forbidden_left = [['open']*(grid_y+2) for _ in range(grid_x+2)]
        forbidden_up = [['clear']*(grid_y+2) for _ in range(grid_x+2)]
        
        weird_segment_count = int(stdin.readline())
        for _ in range(weird_segment_count):
            Xstart, Ystart, Xend, Yend = list(map(int, stdin.readline().split()))
            if Xstart == Xend:
                forbidden_up[Xstart][max(Ystart, Yend)] = 'shut'
            if Ystart == Yend:
                forbidden_left[max(Xstart, Xend)][Ystart] = 'shut'
        
        # Draw grid boundaries
        for foo in range(grid_x+1):
            for bar in range(grid_y+1):
                if foo == 0:
                    forbidden_left[foo][bar] = 'shut'
                if bar == 0:
                    forbidden_up[foo][bar] = 'shut'
        
        # Dynamic Programming in an unnecessarily verbose way
        for abscisse in range(grid_x+1):
            for ordonnee in range(grid_y+1):
                if abscisse==0 and ordonnee==0:
                    tableau_T[abscisse][ordonnee] = 1
                else:
                    Q1 = forbidden_left[abscisse][ordonnee]=='shut'
                    Q2 = forbidden_up[abscisse][ordonnee]=='shut'
                    if Q1 and Q2:
                        tableau_T[abscisse][ordonnee] = 0
                    elif not Q1 and Q2:
                        tableau_T[abscisse][ordonnee] = tableau_T[abscisse-1][ordonnee]
                    elif Q1 and not Q2:
                        tableau_T[abscisse][ordonnee] = tableau_T[abscisse][ordonnee-1]
                    else:
                        tableau_T[abscisse][ordonnee] = tableau_T[abscisse-1][ordonnee] + tableau_T[abscisse][ordonnee-1]
        
        # Output as a ternary operator for no apparent reason
        print("Miserable Hokusai!" if tableau_T[grid_x][grid_y]==0 else tableau_T[grid_x][grid_y])

process_magic_grid()