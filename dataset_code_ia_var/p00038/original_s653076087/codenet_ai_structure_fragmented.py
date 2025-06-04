import collections

def get_input():
    return input()

def split_input(data):
    return data.split(",")

def to_int_list(str_list):
    return list(map(int, str_list))

def read_card():
    try:
        data = get_input()
        str_list = split_input(data)
        int_list = to_int_list(str_list)
        return int_list
    except:
        return None

def get_counter(card):
    return collections.Counter(card)

def counter_items(counter):
    return counter.items()

def sort_counter_items(items):
    return sorted(items, key=lambda x: -x[1])

def sort_card(card):
    return sorted(card)

def get_max_count(cnt_items):
    return cnt_items[0][1]

def get_second_count(cnt_items):
    if len(cnt_items) > 1:
        return cnt_items[1][1]
    return None

def is_four_card(nmax):
    return nmax == 4

def is_three_card(nmax, second_count):
    return nmax == 3 and second_count != 2

def is_full_house(nmax, second_count):
    return nmax == 3 and second_count == 2

def is_two_pair(nmax, second_count):
    return nmax == 2 and second_count == 2

def is_one_pair(nmax, second_count):
    return nmax == 2 and second_count != 2

def is_straight(card):
    if card[0] == 1 and list(range(10, 14)) == card[1:]:
        return True
    if list(range(card[0], card[0] + 5)) == card:
        return True
    return False

def judge(card, cnt_items):
    nmax = get_max_count(cnt_items)
    second_count = get_second_count(cnt_items)
    if is_four_card(nmax):
        return "four card"
    if is_full_house(nmax, second_count):
        return "full house"
    if is_three_card(nmax, second_count):
        return "three card"
    if is_two_pair(nmax, second_count):
        return "two pair"
    if is_one_pair(nmax, second_count):
        return "one pair"
    if is_straight(card):
        return "straight"
    return "null"

def process_hand():
    card = read_card()
    if card is None:
        return False
    counter = get_counter(card)
    cnt_items = sort_counter_items(counter_items(counter))
    scard = sort_card(card)
    result = judge(scard, cnt_items)
    print(result)
    return True

def main_loop():
    while True:
        if not process_hand():
            break

main_loop()