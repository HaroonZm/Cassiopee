def check_bingo(card, marks, M):
    # Check rows
    for i in range(M):
        if all(marks[i][j] for j in range(M)):
            return True
    # Check columns
    for j in range(M):
        if all(marks[i][j] for i in range(M)):
            return True
    # Check diagonals
    if all(marks[i][i] for i in range(M)):
        return True
    if all(marks[i][M - 1 - i] for i in range(M)):
        return True
    return False

def main():
    while True:
        line = input()
        if line == '':
            break
        P, M = map(int, line.split())
        if P == 0 and M == 0:
            break
        cards = []
        numbers_positions = []
        for _ in range(P):
            nums = list(map(int, input().split()))
            card = []
            pos_map = {}
            for i in range(M):
                row = nums[i*M:(i+1)*M]
                card.append(row)
                for j in range(M):
                    pos_map[row[j]] = (i,j)
            cards.append(card)
            numbers_positions.append(pos_map)
        # All unique numbers across all cards
        all_numbers = set()
        for card in cards:
            for row in card:
                for num in row:
                    all_numbers.add(num)
        all_numbers = list(all_numbers)

        # Precompute the bingo sequences of positions for the cards
        # Actually using check_bingo function later is enough

        # We'll try all sequences of numbers in order that respect the condition
        # The gamemaster controls the order of numbers announced
        # The sequence length at least max over cards of number at which card achieves bingo
        # We want minimal such length that the bingo order is in ascending order of card indices

        # Because P <= 4 and M <=4, total numbers <= 4 * 16 = 64 max
        # Try all permutations would be too large
        # We will do a BFS over states of announced numbers, keeping track of which cards have bingo

        from collections import deque

        # For optimization, store for each card the set of numbers that achieve bingo earliest per card
        # but for now, we try BFS over states represented by bitmask of numbers announced

        # Because numbers are unique per card but may overlap across cards,
        # so need to track announced numbers as a set

        # We can encode state as frozenset of announced numbers
        # But set is large, we can use bitmask for the numbers in all_numbers
        number_index = {num:i for i,num in enumerate(all_numbers)}
        total_nums = len(all_numbers)

        # Precompute for each card when it has bingo given a set of numbers announced
        # As we do BFS, we can compute incrementally

        # BFS queue stores (current announced numbers bitmask, bingo order list)
        # bingo order list stores (card index, step at which card got bingo)
        # We want the bingo order to be sorted by card index ascending (card0 then card1 then card2 etc)
        # That means card i achieves bingo no later than card j if i<j

        # We want minimal length of such sequence

        from collections import deque

        # Start from empty set of announced numbers
        # Keep track visited states to avoid redundancy
        visited = set()
        queue = deque()
        # State: (announced bitmask, bingo status list for each card (-1 if no bingo yet, else step))
        start_bingo = [-1]*P
        queue.append( (0, tuple(start_bingo)) )
        visited.add((0, tuple(start_bingo)))
        answer = 0

        while queue:
            announced_mask, bingo_status = queue.popleft()
            step = bin(announced_mask).count('1')
            # If all cards have bingo, check condition (*)
            if all(status != -1 for status in bingo_status):
                # Check condition (*): For all i<j, bingo_status[i] <= bingo_status[j]
                ok = True
                for i in range(P):
                    for j in range(i+1,P):
                        if bingo_status[i] > bingo_status[j]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    answer = step
                    break
            # Try to announce next number among those not announced
            for ni in range(total_nums):
                if not (announced_mask & (1 << ni)):
                    new_mask = announced_mask | (1 << ni)
                    new_bingo_status = list(bingo_status)
                    number = all_numbers[ni]
                    # Check for each card if bingo achieved at new step by adding this number
                    for cidx in range(P):
                        if new_bingo_status[cidx] == -1:
                            pos_map = numbers_positions[cidx]
                            card = cards[cidx]
                            if number in pos_map:
                                i,j = pos_map[number]
                                # Build marks for this card based on new_mask
                                # Check all numbers announced so far for this card
                                marks = [ [False]*M for _ in range(M)]
                                for num2 in all_numbers:
                                    if new_mask & (1 << number_index[num2]):
                                        if num2 in numbers_positions[cidx]:
                                            x,y= numbers_positions[cidx][num2]
                                            marks[x][y] = True
                                if check_bingo(card, marks, M):
                                    new_bingo_status[cidx] = step + 1
                    new_bingo_status_t = tuple(new_bingo_status)
                    if (new_mask, new_bingo_status_t) not in visited:
                        visited.add((new_mask, new_bingo_status_t))
                        queue.append( (new_mask, new_bingo_status_t) )
        print(answer)

if __name__ == '__main__':
    main()