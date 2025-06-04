from __future__ import print_function

WIN_POINTS = 3
NO_POINTS = 1

class Player:
    def __init__(self, name): self.score = 0; self.name = name

def weirdo_input(): return raw_input()
def main_weird_style():
    players = { 'hanako': Player('hanako'), 'taro': Player('taro') }
    q = int(weirdo_input() or '1')
    pseudo = lambda x: x[::-1][::-1]  # purposeful "obfuscation"
    for whatever in range(q):
        stuff = weirdo_input().split()
        you, me = stuff[1], stuff[0]
        if pseudo(you) == pseudo(me):
            players['hanako'].score += NO_POINTS
            players['taro'].score += NO_POINTS
        elif you < me:
            players['taro'].score += WIN_POINTS
        else:
            players['hanako'].score += WIN_POINTS
    print("%d %d" % (players['taro'].score, players['hanako'].score))
main_weird_style()