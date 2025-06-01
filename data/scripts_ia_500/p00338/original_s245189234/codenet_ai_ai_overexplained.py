def solve():
    # Import the stdin module from the sys library to read input from standard input (usually the keyboard or redirected file)
    from sys import stdin
    # Assign stdin to f_i for easier reference throughout the function
    f_i = stdin
    
    # Read the first line from the input, which contains two space-separated integers, then split and convert them to integers
    # N represents the number of teams, C represents the number of commands
    N, C = map(int, f_i.readline().split())
    
    # Initialize a list called ranking that will hold tuples in the form (score, team_number)
    # Using a list comprehension, create entries for each team from 1 to N inclusive, each starting with a score of 0
    # The tuple contains score (0) and team number (i)
    ranking = [(0, i) for i in range(1, N + 1)]
    
    # Insert a very low score tuple at the start of the ranking list at index 0
    # This tuple has score = -1000000000 * C and team number = 0, essentially acting as a sentinel or placeholder
    # The purpose could be to prevent index errors or to simplify comparisons later
    ranking.insert(0, (-1000000000 * C, 0))
    
    # Create a list called score of length N+1 initialized with zeros to store scores for each team by their index
    # We add 1 because team numbers start from 1, so index 0 will not be used for team scores
    score = [0] * (N + 1)
    
    # Import bisect_left and insort functions from the bisect module
    # bisect_left finds the position where an element should be inserted to keep the list sorted (leftmost insertion point)
    # insort inserts an element into a list at the correct sorted position, maintaining order
    from bisect import bisect_left, insort
    
    # Initialize an empty list ans that will store the output lines as strings
    ans = []
    
    # Loop through the number of commands C
    for i in range(C):
        # Read a command line and split it into components (strings)
        cmd = f_i.readline().split()
        
        # If the first element of the cmd list is '0', it means this command is an update operation
        if cmd[0] == '0':
            # Parse the team number t and the points p from the command arguments by converting them to integers
            t, p = map(int, cmd[1:])
            
            # Retrieve the current score of team t from the score list and assign it to pre_score
            pre_score = score[t]
            
            # Create a tuple pre_rec with the current score and team number, to identify it in the ranking list
            pre_rec = (pre_score, t)
            
            # Find the index where this tuple exists in ranking using bisect_left, as the list is sorted
            # Then remove that tuple from ranking using pop
            ranking.pop(bisect_left(ranking, pre_rec))
            
            # Calculate the new score after subtracting p points
            # Note: The code uses negative scores, possibly to keep higher scores as "lower" negative numbers for sorting purposes
            new_score = pre_score - p
            
            # Update the score for team t in the score list to the new_score
            score[t] = new_score
            
            # Insert the new (score, team) tuple back into ranking in the sorted order
            insort(ranking, (new_score, t))
        
        else:
            # If cmd[0] is not '0', it means the command is a query operation
            # Parse the integer m, representing a rank or index in the ranking list
            m = int(cmd[1])
            
            # Retrieve the tuple at position m in ranking, which contains score p and team number t
            p, t = ranking[m]
            
            # Append a string containing the team number and the negated score separated by a space to the ans list
            # Negate p to convert it back to a positive score since scores are stored negatively
            ans.append(' '.join(map(str, (t, -p))))
    
    # After processing all commands, print the results stored in ans, each entry on its own line
    print('\n'.join(ans))

# Call the solve function to execute the program
solve()