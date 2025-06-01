n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    if start == end:
        print(start)
        continue
    def left_path(s, e):
        path = []
        cur = s
        while cur != e:
            path.append(cur)
            if cur == 0:
                cur += 1
            else:
                cur -= 1
        path.append(e)
        return path
    def right_path(s, e):
        path = []
        cur = s
        while cur != e:
            path.append(cur)
            if cur == 0:
                cur += 1
            else:
                cur += 1
        path.append(e)
        return path
    def circ_left_path(s, e):
        path = []
        cur = s
        while cur != e:
            path.append(cur)
            cur = 5 + ( (cur - 6) % 5 )
        path.append(e)
        return path
    def circ_right_path(s, e):
        path = []
        cur = s
        while cur != e:
            path.append(cur)
            cur = 5 + ( (cur - 4) % 5 )
        path.append(e)
        return path
    def dist_left(s,e):
        if s >= e:
            return s - e
        else:
            return s + 10 - e
    def dist_right(s,e):
        if e >= s:
            return e - s
        else:
            return e + 10 - s
    if start == 0:
        # bus can only go right (0->1->...->4->5)
        # then circular loop
        if end <= 4:
            path = list(range(start,end+1))
        elif 5 <= end <=9:
            path = list(range(0,5))
            cur = 5
            path.append(cur)
            while cur != end:
                cur = 5 + ( (cur - 4) % 5 )
                path.append(cur)
        print(*path)
        continue
    if 1 <= start <= 4:
        # can go left or right
        # left means decreasing down to 0, right means increasing up to 5 and loop
        # but stops at 0 on left or at 5 on right
        # so left path: s->s-1->...->e if e<=s
        # right path: s->s+1->...->e (via circular after 5)
        # but circular only between 5-9
        # calculate left and right distances
        # For left path (decreasing), make path wrapping from 0 to 9 not possible because 0 is end
        # For right path (increasing), wrapping by circular route at 5-9
        def path_left(s,e):
            res = []
            cur = s
            while cur != e:
                res.append(cur)
                if cur == 0:
                    break
                cur -= 1
            res.append(e)
            return res
        def path_right(s,e):
            res = []
            cur = s
            while cur != e:
                res.append(cur)
                if cur == 9:
                    cur = 5
                else:
                    cur += 1
            res.append(e)
            return res
        dleft = dist_left(start,end)
        dright = dist_right(start,end)
        if dleft <= dright:
            path = path_left(start,end)
        else:
            path = path_right(start,end)
        print(*path)
        continue
    if start == 5:
        # can go two ways: 5->4->...->0 or 5->6->7->8->9->5 loop
        # For 5 to (1..4 or 0), left direction going down 4->3->...0
        # For 5 to (6..9), circular route
        # The problem says that 1-5 can take either direction choosing shorter path
        # so check left path as 5->4->3... down to end if end<=5
        # or circular path if end>=5
        
        def path_left_5(s,e):
            res = []
            cur = s
            while cur != e:
                res.append(cur)
                if cur <= 0:
                    break
                cur -= 1
            res.append(e)
            return res
        def path_circ_5(s,e):
            res = []
            cur = s
            while cur != e:
                res.append(cur)
                cur = 5 + ( (cur - 4) % 5 )
            res.append(e)
            return res
        dleft = dist_left(start,end)
        dright = dist_right(start,end)
        if dleft <= dright:
            path = path_left_5(start,end)
        else:
            path = path_circ_5(start,end)
        print(*path)
        continue
    if 6 <= start <= 9:
        # circular bus only, can only go forward 5->6->7->8->9->5
        # to go from start to end, do circular path increasing mod loop
        path = []
        cur = start
        while cur != end:
            path.append(cur)
            cur = 5 + ((cur - 4) % 5)
        path.append(end)
        print(*path)