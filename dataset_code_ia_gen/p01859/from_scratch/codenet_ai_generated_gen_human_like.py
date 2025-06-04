import sys
sys.setrecursionlimit(10**7)

def normalize(hands):
    # Sort the counts of fingers on two hands (order doesn't matter)
    return tuple(sorted(hands))

def game_result(current, opponent, memo):
    # current, opponent: tuples (left_fingers, right_fingers)
    # memo: dictionary for memoization
    # Returns True if current player can force a win, False otherwise

    # If current player lost both hands, they lose
    if current == (0,0):
        return False
    # If opponent lost both hands, current player wins
    if opponent == (0,0):
        return True

    key = (current, opponent)
    if key in memo:
        return memo[key]

    # Try all moves
    # current player chooses one of their live hands,
    # and taps one of opponent's live hands

    curr_hands = [h for h in current if h > 0]
    opp_hands = [h for h in opponent if h > 0]

    # To preserve hand positions, but since we normalize state,
    # keep hands as tuple sorted for memo but when iterating, know index
    # We'll keep original structure of hands (left, right) to identify which hand updated

    # enumerate possible moves
    for i_cur in [0,1]:
        if current[i_cur] == 0:
            continue
        for i_opp in [0,1]:
            if opponent[i_opp] == 0:
                continue
            # tapping opponent's hand:
            new_opp = list(opponent)
            new_value = new_opp[i_opp] + current[i_cur]
            if new_value >= 5:
                new_opp[i_opp] = 0
            else:
                new_opp[i_opp] = new_value

            # Normalize states for recursive call
            new_current = normalize(current)
            new_opponent = normalize(tuple(new_opp))

            # Next turn: opponent becomes current, current becomes opponent
            # We check if opponent (now next player) has a winning move
            if not game_result(new_opponent, new_current, memo):
                # current player can force a win
                memo[key] = True
                return True

    # No winning moves
    memo[key] = False
    return False

def main():
    L_i, R_i = map(int, input().split())
    L_n, R_n = map(int, input().split())

    start_current = normalize((L_i, R_i))
    start_opponent = normalize((L_n, R_n))

    memo = dict()
    if game_result(start_current, start_opponent, memo):
        print("ISONO")
    else:
        print("NAKAJIMA")

if __name__ == "__main__":
    main()