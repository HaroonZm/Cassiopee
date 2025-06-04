while True:
    line = input()
    if line == '':
        continue
    n,m = map(int, line.split())
    if n == 0 and m == 0:
        break
    seats = ['#'] * n
    persons = []
    for _ in range(m):
        persons.append(input().strip())

    for p in persons:
        if p == 'A':
            # A国人：左端から空いている椅子に座る
            for i in range(n):
                if seats[i] == '#':
                    seats[i] = 'A'
                    break

        elif p == 'B':
            # B国人：Aの隣以外で右端から空いてる椅子に座る
            # Aの隣だけ空いてるなら左端から座る
            def is_adjacent_to_A(i):
                if i-1 >= 0 and seats[i-1] == 'A':
                    return True
                if i+1 < n and seats[i+1] == 'A':
                    return True
                return False

            candidates = []
            for i in range(n-1,-1,-1):
                if seats[i] == '#' and not is_adjacent_to_A(i):
                    candidates.append(i)
            if candidates:
                seats[candidates[0]] = 'B'
            else:
                for i in range(n):
                    if seats[i] == '#':
                        seats[i] = 'B'
                        break

        elif p == 'C':
            # C国人：隣に座りたい。左から座ってる人をみる。
            # 一番左の人の右隣に座る、空いてなければ左隣に、どちらも埋まってたら次の人に
            # 想定空いてなければ椅子の数が奇数(n+1)/2 偶数 n/2+1に座る
            seated = [i for i,x in enumerate(seats) if x != '#']
            seated.sort()
            placed = False
            for idx in seated:
                right = idx +1
                left = idx -1
                if right < n and seats[right] == '#':
                    seats[right] = 'C'
                    placed = True
                    break
                elif left >=0 and seats[left] == '#':
                    seats[left] = 'C'
                    placed = True
                    break
            if not placed:
                if len(seated) == 0:
                    if n %2 ==1:
                        mid = (n+1)//2 -1
                    else:
                        mid = n//2
                    seats[mid] = 'C'
                else:
                    # 周囲に空きがなければ左端から座る（問題文には出てないが）
                    for i in range(n):
                        if seats[i] == '#':
                            seats[i] = 'C'
                            break

        elif p == 'D':
            # D国人：隣に座りたくない。
            # 一番近い人との距離が最大になる椅子に座る
            # 同条件複数あれば左の椅子に座る
            # 誰も座っていなければ左端に座る
            seated = [i for i,x in enumerate(seats) if x != '#']
            if len(seated) ==0:
                seats[0] = 'D'
            else:
                max_dist = -1
                candidate = -1
                for i in range(n):
                    if seats[i] != '#':
                        continue
                    # i番の椅子から一番近い人までの距離を計算
                    d = n+1
                    for s in seated:
                        dist = abs(s - i)
                        if dist < d:
                            d = dist
                    if d > max_dist:
                        max_dist = d
                        candidate = i
                seats[candidate] = 'D'

    print(''.join(seats))