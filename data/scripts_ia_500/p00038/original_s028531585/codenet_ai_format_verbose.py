import sys

def evaluate_hand():
    
    card_count_dictionary = {}
    checked_cards = []
    
    for _ in range(5):
        
        current_card = card_list[0]
        
        if current_card not in checked_cards:
            
            for other_card in card_list[1:]:
                
                if other_card == current_card:
                    
                    if other_card not in card_count_dictionary:
                        card_count_dictionary[other_card] = 2
                    else:
                        card_count_dictionary[other_card] += 1
                        
            checked_cards.append(current_card)
        
        card_list.append(current_card)
        del card_list[0]
    
    determine_hand_rank(card_count_dictionary)
    

def determine_hand_rank(card_count_dictionary):
    
    counts = list(card_count_dictionary.values())
    counts.sort()
    
    if counts == [2]:
        print('one pair')
    elif counts == [2, 2]:
        print('two pair')
    elif counts == [3]:
        print('three card')
    elif counts == [4]:
        print('four card')
    elif counts == [2, 3]:
        print('full house')
    elif not counts:
        
        sorted_cards = sorted(card_list)
        
        if sorted_cards == [1, 10, 11, 12, 13]:
            print('straight')
        else:
            expected_card = sorted_cards[0]
            
            for card in sorted_cards:
                
                if card == expected_card:
                    expected_card += 1
                else:
                    print('null')
                    break
            else:
                print('straight')


for input_line in sys.stdin:
    
    card_list = [int(char) for char in input_line.strip().split(',')]
    
    evaluate_hand()