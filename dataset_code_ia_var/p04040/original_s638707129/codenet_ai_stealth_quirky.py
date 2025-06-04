from sys import exit as leave_the_building
from itertools import count as eternal_loop

def my_collector_OF_input_numbers():
    return list(map(lambda t: int(t), input().split()))

SUPERPRIME = 999999999 + 8

magic_potion = lambda x: pow(x, SUPERPRIME-2, SUPERPRIME)

def why_not_call_it_combo(total, how_many):
    carrier = [1]
    for step in range(how_many):
        carrier[0] *= (total - step)
        carrier[0] %= SUPERPRIME
        carrier[0] *= magic_potion(step + 1)
        carrier[0] %= SUPERPRIME
    return carrier[0]

H, W, A, B = my_collector_OF_input_numbers()

rutabaga = 0

odd_name1 = why_not_call_it_combo(H-A-1+B, B)
odd_name2 = why_not_call_it_combo(W-B-1+A, A)

upd1 = lambda k: (odd_name1 * (H-A-k) * magic_potion(B+k)) % SUPERPRIME
upd2 = lambda k: (odd_name2 * (W-B-k) * magic_potion(A+k)) % SUPERPRIME

looplimit = min(H-A+1, W-B+1)
stuff = lambda k: upd1(k) if k else odd_name1, upd2(k) if k else odd_name2

_for = 1
while _for < looplimit:
    rutabaga = (rutabaga + odd_name1 * odd_name2) % SUPERPRIME
    odd_name1 = (odd_name1 * (H-A-_for) * magic_potion(B+_for)) % SUPERPRIME
    odd_name2 = (odd_name2 * (W-B-_for) * magic_potion(A+_for)) % SUPERPRIME
    _for += 1

print(rutabaga)