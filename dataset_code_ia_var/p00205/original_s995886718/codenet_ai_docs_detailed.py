def main():
    """
    Main loop for a 5-player Rock-Paper-Scissors game.  
    For each round, prompts the user to input the hand (1: Rock, 2: Scissors, 3: Paper) for each of the 5 players,  
    determines the results (1: Win, 2: Lose, 3: Draw) for each player, and outputs the outcome.
    The game continues until invalid input or interruption (e.g., EOF or KeyboardInterrupt).
    """
    # Repeat the game until an exception occurs (end of input or invalid input)
    while True:
        try:
            # datas will store the hand of each player (length 5)
            datas = [0] * 5
            # lens counts how many times each hand type was played [Rock, Scissors, Paper]
            lens = [0] * 3
            # status will record the result mapping for the current round:
            # status[0]: outcome for Rock, status[1]: outcome for Scissors, status[2]: outcome for Paper
            status = [0] * 3

            # Input section: Read hands for each of the 5 players
            for i in range(5):
                hand = int(input())
                datas[i] = hand  # Store the hand
                lens[hand - 1] += 1  # Count appearance of each hand

            # Check for draw (あいこ), i.e., all hands are present or everyone chose the same hand
            if (lens[0] > 0 and lens[1] > 0 and lens[2] > 0) or (lens[0] == 5 or lens[1] == 5 or lens[2] == 5):
                # All players get draw
                for _ in range(5):
                    print(3)
            else:
                # Determine who wins and who loses based on hand distribution
                # If at least one Rock is played
                if lens[0] > 0:
                    # For Scissors: loses to Rock
                    status[1] = 2
                    # For Paper: wins against Rock
                    status[2] = 1
                # If at least one Scissors is played
                if lens[1] > 0:
                    # For Rock: wins against Scissors
                    status[0] = 1
                    # For Paper: loses to Scissors
                    status[2] = 2
                # If at least one Paper is played
                if lens[2] > 0:
                    # For Rock: loses to Paper
                    status[0] = 2
                    # For Scissors: wins against Paper
                    status[1] = 1
                # Output the result for each player
                for i in range(5):
                    print(status[datas[i] - 1])
        except Exception:
            # Exit the loop on invalid input or user interruption
            break

if __name__ == "__main__":
    main()