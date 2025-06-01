from sys import stdin

# Constants representing bases using bit flags
NONE, FIRST, SECOND, THIRD = 0, 1, 2, 4

inning = int(stdin.readline())
inning_scores = []

for _ in range(inning):
    runners = NONE
    outs = 0
    runs = 0
    while outs < 3:
        event = stdin.readline().strip()
        
        if event == "HIT":
            # Score if runner on third
            runs += bool(runners & THIRD)
            # Shift runners forward and place new runner on first
            runners = ((runners << 1) & 0b111) | FIRST

        elif event == "HOMERUN":
            # Count runs from all occupied bases plus batter
            runs += bin(runners).count('1') + 1
            runners = NONE

        elif event == "OUT":
            outs += 1
    
    inning_scores.append(runs)

print(*inning_scores, sep='\n')