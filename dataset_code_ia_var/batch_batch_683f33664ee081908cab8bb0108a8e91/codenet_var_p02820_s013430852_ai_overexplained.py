def run(N, K, R, S, P, T):
    # Initialize the total score variable to 0.
    # This variable will be used to store the sum of points obtained.
    ans = 0
    
    # Initialize an empty string 'main'.
    # This string will be used to keep track of your chosen moves so far.
    # Its ith character will represent the hand the player used in the ith round.
    main = ''
    
    # Start a for loop to iterate through each character in the string 'T'.
    # 'T' is a string representing the opponent's moves, consisting of 'r', 's', or 'p'.
    for i in range(len(T)):
        # Get the character at position 'i' of the string 'T'.
        # This represents the opponent's move for this round.
        t = T[i]
        
        # For the first K rounds, there is no restriction about repeating your own moves.
        if i < K:
            # If the opponent played 'r' (rock):
            if t == 'r':
                # Add P points, because playing 'p' (paper) beats 'r' (rock).
                ans += P
                # Record your move as 'p' to the 'main' string.
                main += 'p'
            # If the opponent played 's' (scissors):
            elif t == 's':
                # Add R points, because playing 'r' (rock) beats 's' (scissors).
                ans += R
                # Record your move as 'r'.
                main += 'r'
            # If the opponent played 'p' (paper):
            elif t == 'p':
                # Add S points, because playing 's' (scissors) beats 'p' (paper).
                ans += S
                # Record your move as 's'.
                main += 's'
        # For rounds after the first K rounds:
        else:
            # Retrieve your move played K rounds ago.
            # The restriction is that you cannot play the same move as in the round K rounds before if you won at that time.
            pre_t = main[i - K]
            
            # If the opponent plays 'r' (rock), 
            # and your move K turns ago was NOT 'p' (paper):
            if t == 'r' and pre_t != 'p':
                # You can safely play 'p' (paper) to win and get P points.
                ans += P
                main += 'p'  # Record your move.
            # If the opponent plays 's' (scissors), 
            # and your move K turns ago was NOT 'r' (rock):
            elif t == 's' and pre_t != 'r':
                # Play 'r' (rock) to win and get R points.
                ans += R
                main += 'r'
            # If the opponent plays 'p' (paper), 
            # and your move K turns ago was NOT 's' (scissors):
            elif t == 'p' and pre_t != 's':
                # Play 's' (scissors) to win and get S points.
                ans += S
                main += 's'
            # Otherwise (meaning playing the best move would repeat your move K rounds ago),
            # so you cannot play the same move, just add a space as a placeholder.
            else:
                main += ' '
    # After processing all rounds, return the total score accumulated.
    return ans

def main():
    # Take input from the user.
    # The first line contains two integers, N (number of rounds) and K (distance for the restriction).
    N, K = map(int, input().split())
    # The second line contains three integers: R (points for playing rock), S (points for playing scissors), and P (points for playing paper).
    R, S, P = map(int, input().split())
    # The third line is the opponent's moves, represented as a string.
    T = input()
    # Call the 'run' function to calculate the result and print the result to the standard output.
    print(run(N, K, R, S, P, T))

# The entry point of the program.
# This checks if this file is being run as a script, and not being imported as a module.
if __name__ == '__main__':
    # Call the main function.
    main()