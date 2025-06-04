import sys

def build_keyboard(h, w):
    kb = {}
    y = 0
    while y < h:
        row = input()
        for x in range(len(row)):
            kb[row[x]] = (x, y)
        y += 1
    return kb

def move_and_count(board, s):
    cur = [0, 0]
    cnt = 0
    for ch in list(s):
        pos = board.get(ch)
        if pos is not None:
            dx = abs(pos[0] - cur[0])
            dy = abs(pos[1] - cur[1])
            cnt = cnt + dx + dy + 1
            cur[0], cur[1] = pos[0], pos[1]
        else:
            continue
    return cnt

class Runner:
    @staticmethod
    def process():
        while True:
            vals = input().split()
            if int(vals[0]) == 0 and int(vals[1]) == 0:
                return
            h, w = map(int, vals)
            kb = build_keyboard(h, w)
            s = input()
            res = move_and_count(kb, s)
            print(res)

if __name__ == "__main__":
    (lambda func: func())(Runner.process)