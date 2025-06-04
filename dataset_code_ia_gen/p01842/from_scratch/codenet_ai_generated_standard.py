import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

from functools import lru_cache

"""
State: 
p: player to move (0 or 1)
i, j: indices for top of decks a and b
stack: two lists: cards and which player played each card
last_pass: bool - True if last turn was pass
"""

@lru_cache(None)
def dfs(p, i, j, stack_cards, stack_owners, last_pass):
    # If both players passed consecutively with empty stack, game ends
    if last_pass and p == 0:  # last was pass, p=0 means both passed consecutively since 0 starts game
        if len(stack_cards) == 0:
            return 0

    # Scores for current player difference (p1-p2)
    # The current player tries to maximize (p1 - p2)
    # Next player tries to minimize it

    # Generate moves
    moves = []

    # Option 1: Play top card of own deck
    if p == 0 and i < n:
        # Add own card a[i] on stack
        new_stack_cards = stack_cards + (a[i],)
        new_stack_owners = stack_owners + (0,)
        val = dfs(1, i+1, j, new_stack_cards, new_stack_owners, False)
        moves.append(val)
    elif p == 1 and j < m:
        new_stack_cards = stack_cards + (b[j],)
        new_stack_owners = stack_owners + (1,)
        val = dfs(0, i, j+1, new_stack_cards, new_stack_owners, False)
        moves.append(val)

    # Option 2: Pass
    # When pass, calculate points and remove cards from stack
    if last_pass and len(stack_cards) == 0:
        # Both passed consecutively on empty stack: end
        val = 0
    else:
        # Calculate points for p player
        # For each player separately: but here p passed, now to compute
        # Actually, at pass, both players take points simultaneously
        # For both players do the calculation, get their scores
        # Then add difference of scores to current score

        def get_score(player):
            # Find the positions of opponent's interference cards in stack
            # interference cards are -1 cards placed by opponent that are below the player's scoring cards
            opp = 1 - player
            # Find highest idx of interference card of opponent
            pos = -1
            for idx in reversed(range(len(stack_cards))):
                if stack_owners[idx] == opp and stack_cards[idx] == -1:
                    pos = idx
                    break
            res = 0
            for idx in range(len(stack_cards)):
                if stack_owners[idx] == player and stack_cards[idx] > 0:
                    # scoring card by player
                    if pos == -1 or idx > pos:
                        res += stack_cards[idx]
            return res

        p1_score = get_score(0)
        p2_score = get_score(1)
        # Remove all cards from stack after scoring
        val = p1_score - p2_score
        # Switch player
        val += dfs(1 - p, i, j, tuple(), tuple(), True)

    moves.append(val)

    if p == 0:
        return max(moves)
    else:
        return min(moves)

print(dfs(0,0,0,tuple(),tuple(),False))