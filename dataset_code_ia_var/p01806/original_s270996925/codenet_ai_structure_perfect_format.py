def main():
    while True:
        n = int(input())
        if n == 0:
            break

        def spin(dice, direct):
            l, r, f, b, d, u = dice
            if direct == "R":
                return [d, u, f, b, r, l]
            if direct == "L":
                return [u, d, f, b, l, r]
            if direct == "B":
                return [l, r, d, u, b, f]
            if direct == "F":
                return [l, r, u, d, f, b]

        def move(x, y, direct):
            if direct == "R":
                return x + 1, y
            if direct == "L":
                return x - 1, y
            if direct == "B":
                return x, y + 1
            if direct == "F":
                return x, y - 1

        update_lst = []
        for _ in range(n):
            x, y = map(int, input().split())
            dice = list(map(int, input().split()))
            rot = input()
            update_point = {}
            update_point[(x, y)] = dice[-2]
            for direct in rot:
                dice = spin(dice, direct)
                x, y = move(x, y, direct)
                update_point[(x, y)] = dice[-2]
            update_lst.append(update_point)

        used_lst = [set() for _ in range(2 ** n)]
        mask = 1
        for i in range(n):
            keys = set(update_lst[i].keys())
            for j in range(2 ** n):
                if not (mask & j):
                    continue
                used_lst[j] |= keys
            mask <<= 1

        add_score = {}
        mask = 1
        for i in range(n):
            update_point = update_lst[i]
            for j in range(2 ** n):
                if mask & j:
                    continue
                used_point = used_lst[j]
                add = 0
                for k, v in update_point.items():
                    if k not in used_point:
                        add += v
                add_score[(j, mask)] = add
            mask <<= 1

        dic = {}
        end = 2 ** n - 1

        def max_score(stat):
            if stat in dic:
                return dic[stat]
            if stat == end:
                return 0
            ret = 0
            mask = 1
            for i in range(n):
                if stat & mask:
                    mask <<= 1
                    continue
                ret = max(ret, add_score[(stat, mask)] + max_score(stat | mask))
                mask <<= 1
            dic[stat] = ret
            return ret

        print(max_score(0))

main()