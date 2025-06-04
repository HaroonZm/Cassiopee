from collections import deque

m_and_n = input().split()
while True:
    m, n = map(int, m_and_n)
    if m == 0:
        break

    length = m
    max_space = length * 2
    space = max_space
    body = []
    for i in range(length):
        # Each Part
        part = {}
        part['ind'] = i
        part['top'] = None
        part['und'] = None
        part['sta'] = 0
        part['rem'] = -1
        body.append(part)

    que = deque()
    ans = []

    for t in range(n * 120 - 1):
        # prog
        for part in body:
            if part['top'] is not None:
                part['top']['rem'] -= 1
            if part['und'] is not None:
                part['und']['rem'] -= 1
            if part['sta'] != 0:
                part['rem'] -= 1

        # out: collect all outs into ans
        outs = []
        for part in body:
            if part['sta'] >= 1 and part['rem'] <= 0:
                if part['sta'] == 2:
                    if part['und']['rem'] <= 0 and part['top']['rem'] <= 0:
                        outs.append([part['und']['ind'], part['top']['ind']])
                        part['und'] = None
                        part['top'] = None
                        part['sta'] = 0
                        part['rem'] = -1
                        continue
                    if part['und']['rem'] <= 0:
                        outs.append([part['und']['ind']])
                        part['und'] = None
                        part['sta'] = 1
                        part['rem'] = part['top']['rem']
                        continue
                if part['sta'] == 1:
                    if part['top']['rem'] <= 0:
                        outs.append([part['top']['ind']])
                        part['top'] = None
                        part['sta'] = 0
                        part['rem'] = -1
                        continue
        ret = []
        for out in outs:
            ret += out
        ans += ret
        space += len(ret)

        # input chaque 10 ticks
        if t <= (n - 1) * 10 and t % 10 == 0:
            r_in = int(input())
            que.append((r_in, t // 10 + 1))

        # try to push from que as many as we can fill
        k = min(space, len(que))
        for _ in range(k):
            rem, ind = que.popleft()
            space -= 1

            placed = False
            for part in body:
                if part['sta'] == 0:
                    part['top'] = {'rem': rem, 'ind': ind}
                    part['sta'] = 1
                    part['rem'] = rem
                    placed = True
                    break
            if placed:
                continue

            rem_lst = []
            for part in body:
                if part['sta'] == 1:
                    rem_lst.append((part['rem'], part['ind']))
            rem_lst.sort()

            inserted = False
            for r, i in rem_lst:
                if r >= rem:
                    tar = body[i]
                    tar['und'] = {'rem': rem, 'ind': ind}
                    tar['sta'] = 2
                    tar['rem'] = rem
                    inserted = True
                    break
            if inserted:
                continue
            if rem_lst:
                max_r = rem_lst[-1][0]
                for r, i in rem_lst:
                    if r == max_r:
                        tar = body[i]
                        tar['und'] = {'rem': rem, 'ind': ind}
                        tar['sta'] = 2
                        tar['rem'] = rem
                        break

    print(*ans)
    m_and_n = input().split()