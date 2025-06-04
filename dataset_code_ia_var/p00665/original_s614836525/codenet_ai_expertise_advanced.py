import sys
from operator import itemgetter

input = sys.stdin.readline

while True:
    nmk = input()
    if not nmk:
        break
    n, m, k, l = map(int, nmk.split())
    if n == 0:
        break

    ranking = [tuple(input().split()) for _ in range(n)]
    ranking = [(int(x), name) for name, x in ranking]
    ranking.sort(key=lambda t: (-t[0], t[1]))

    favs = {input().strip() for _ in range(m)}

    favs_ranking = [(x, name) for x, name in ranking if name in favs]
    not_favs_ranking = [(x, name) for x, name in ranking if name not in favs]

    favs_ranking.sort(key=lambda t: (-t[0], t[1]))
    not_favs_ranking.sort(key=lambda t: (-t[0], t[1]))

    favs_names = [name for _, name in favs_ranking]
    favs_dict = dict(favs_ranking)
    not_favs_dict = dict(not_favs_ranking)
    favs_length = len(favs_ranking)
    not_favs_length = len(not_favs_ranking)

    def check(num):
        not_favs_num = k - num
        if num > favs_length:
            return False
        if not_favs_num >= not_favs_length:
            return True
        target_x, target_name = not_favs_ranking[not_favs_num]
        need = 0
        for x, name in favs_ranking[:num]:
            if target_name > name:
                if target_x <= x:
                    continue
                need += target_x - x
            else:
                if target_x < x:
                    continue
                need += target_x - x + 1
        return need <= l

    left, right = 0, min(k, favs_length) + 1
    while right - left > 1:
        center = (left + right) >> 1
        if check(center):
            left = center
        else:
            right = center
    print(left)