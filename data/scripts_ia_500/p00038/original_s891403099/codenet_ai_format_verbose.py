while True:

    try:
    
        raw_cards_input = input().split(",")
        
        card_counts_by_rank = [0] * 14
        
        for card in raw_cards_input:
            if card == "A":
                card_counts_by_rank[1] += 1
            elif card == "J":
                card_counts_by_rank[11] += 1
            elif card == "Q":
                card_counts_by_rank[12] += 1
            elif card == "K":
                card_counts_by_rank[13] += 1
            else:
                card_counts_by_rank[int(card)] += 1
        
        number_of_pairs = 0
        has_three_of_a_kind = False
        has_four_of_a_kind = False
        first_single_card_rank = 0
        
        for rank in range(14):
            count_for_rank = card_counts_by_rank[rank]
            
            if count_for_rank == 1 and first_single_card_rank == 0:
                first_single_card_rank = rank
            elif count_for_rank == 2:
                number_of_pairs += 1
            elif count_for_rank == 3:
                has_three_of_a_kind = True
            elif count_for_rank == 4:
                has_four_of_a_kind = True
                break
        
        is_straight = (
            card_counts_by_rank[first_single_card_rank] == 1 and
            card_counts_by_rank[first_single_card_rank + 1] == 1 and
            card_counts_by_rank[first_single_card_rank + 2] == 1 and
            card_counts_by_rank[first_single_card_rank + 3] == 1 and
            card_counts_by_rank[first_single_card_rank + 4] == 1
        )
        
        is_ace_high_straight = (
            card_counts_by_rank[1] == 1 and
            card_counts_by_rank[10] == 1 and
            card_counts_by_rank[11] == 1 and
            card_counts_by_rank[12] == 1 and
            card_counts_by_rank[13] == 1
        )
        
        is_straight = is_straight or is_ace_high_straight
        
        if has_four_of_a_kind:
            print("four card")
        elif has_three_of_a_kind and number_of_pairs == 1:
            print("full house")
        elif is_straight:
            print("straight")
        elif has_three_of_a_kind:
            print("three card")
        elif number_of_pairs == 2:
            print("two pair")
        elif number_of_pairs == 1:
            print("one pair")
        else:
            print("null")

    except EOFError:
    
        break