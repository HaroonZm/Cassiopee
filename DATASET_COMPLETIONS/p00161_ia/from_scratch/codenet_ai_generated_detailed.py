import sys

def time_to_seconds(m, s):
    # Convert minutes and seconds to total seconds
    return m * 60 + s

def process_dataset(n, lines):
    teams = []
    for i in range(n):
        data = lines[i].split()
        team_id = int(data[0])
        # Extract times for the 4 events
        times = list(map(int, data[1:] ))
        # Calculate total time in seconds for the team
        total_seconds = 0
        for j in range(0, 8, 2):
            total_seconds += time_to_seconds(times[j], times[j+1])
        # Store (total_time, team_id)
        teams.append((total_seconds, team_id))
    
    # Sort teams by total time ascending (smaller total time is better)
    teams.sort(key=lambda x: x[0])
    
    # 優勝 : first team
    winner = teams[0][1]
    # 準優勝 : second team
    second = teams[1][1]
    # ブービー賞 : second last team
    booby = teams[-2][1]
    
    return winner, second, booby

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    index = 0
    while True:
        if index >= len(input_lines):
            break
        n = int(input_lines[index])
        index += 1
        if n == 0:
            break
        lines = input_lines[index:index+n]
        index += n
        
        winner, second, booby = process_dataset(n, lines)
        
        print(winner)
        print(second)
        print(booby)

if __name__ == "__main__":
    main()