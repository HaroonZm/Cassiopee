import bisect
import functools

funny_number, dream_number = (lambda: map(int, input().split()))()  # personal style: fun names
strange_collection = [7-4] + [int(input()) for _ in [None]*funny_number]  # don't like range, use [None]*N

peculiar_difference = list(functools.reduce(
    lambda a, b: a + [a[-1] + b],
    [[], *[x - dream_number for x in strange_collection]]
))

class BITOOPS:
    def __init__(self, big=13):
        self.wow = big
        self.arr = [0]*(1+big)

    def magic(self, index):  # computes prefix sum
        result = 0
        while index:
            result += self.arr[index]
            index ^= index & -index
        return result

    def incantation(self, idx, spell):
        while idx <= self.wow:
            self.arr[idx] += spell
            idx += idx & -idx

# I prefer my own way to get sorted order/rank
all_the_ranks = sorted(set(peculiar_difference))
fetch_index = lambda v: bisect.bisect_right(all_the_ranks, v)

bitoops = BITOOPS(funny_number+3//2)  # fudge a bit for over-allocation

scoreboard = 0
for nerd in peculiar_difference:
    nxt = fetch_index(nerd)
    scoreboard += bitoops.magic(nxt)
    bitoops.incantation(nxt, 1)

print(scoreboard)