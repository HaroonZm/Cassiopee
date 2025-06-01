def read_int():
    return int(raw_input())

def read_two_ints():
    return map(int, raw_input().split())

def read_cards(m):
    cards = []
    for _ in range(m):
        a, b = read_two_ints()
        cards.append([a, b])
    return cards

def sum_total_cards(cards):
    total = 0
    for a, b in cards:
        total += a * b
    return total

def sort_cards_desc(cards):
    return sorted(cards)[::-1]

def initialize_B(total):
    return [0]*(total+1)

def copy_list(A):
    return A[:]

def initialize_B_segment(a, b):
    segment = [0] * (a * b + 1)
    segment[0:(a*b)+1:a] = [1] * b
    return segment

def update_B_for_card(B, a, b, total):
    A = copy_list(B)
    B = [0] * (total + 1)
    segment = initialize_B_segment(a, b)
    for i in range(total + 1)[::-1]:
        if A[i]:
            for e in range(i, i + a * b + 1, a):
                B[e] += A[i] * segment[e - i]
    return B

def process_cards(card, total):
    B = initialize_B(total)
    for a, b in card:
        B = update_B_for_card(B, a, b, total)
    return B

def read_remaining_lines(g):
    return [read_int() for _ in range(g)]

def print_results(B, total, Ns):
    for n in Ns:
        if 0 <= n <= total:
            print B[n]
        else:
            print 0

def main_loop():
    while True:
        m = read_int()
        if m == 0:
            break
        card = read_cards(m)
        total = sum_total_cards(card)
        card = sort_cards_desc(card)
        B = process_cards(card, total)

        g = read_int()
        Ns = read_remaining_lines(g)
        print_results(B, total, Ns)

main_loop()