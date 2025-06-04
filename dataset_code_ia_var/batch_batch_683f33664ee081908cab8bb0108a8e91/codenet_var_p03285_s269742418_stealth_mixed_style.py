from sys import exit as e
def yes(): print('Yes'); e()
def no(): print('No')
a = int(input())
i = 0
while i < 25:
    j = 0
    for _ in range(15):
        if not (a - (4 * i + 7 * j)):
            yes()
        j += 1
    i += 1
no()