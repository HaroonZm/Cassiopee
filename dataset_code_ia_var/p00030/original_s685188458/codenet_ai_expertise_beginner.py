while True:
    line = input()
    n, s = line.split()
    n = int(n)
    s = int(s)
    if n == 0 and s == 0:
        break
    count = 0
    nums = [0,1,2,3,4,5,6,7,8,9]
    length = len(nums)
    # On va tester toutes les combinaisons possibles
    for a in range(length):
        for b in range(a+1, length):
            for c in range(b+1, length):
                for d in range(c+1, length):
                    for e in range(d+1, length):
                        for f in range(e+1, length):
                            for g in range(f+1, length):
                                for h in range(g+1, length):
                                    for i in range(h+1, length):
                                        for j in range(i+1, length):
                                            pick = []
                                            if n >= 1:
                                                pick.append(nums[a])
                                            if n >= 2:
                                                pick.append(nums[b])
                                            if n >= 3:
                                                pick.append(nums[c])
                                            if n >= 4:
                                                pick.append(nums[d])
                                            if n >= 5:
                                                pick.append(nums[e])
                                            if n >= 6:
                                                pick.append(nums[f])
                                            if n >= 7:
                                                pick.append(nums[g])
                                            if n >= 8:
                                                pick.append(nums[h])
                                            if n >= 9:
                                                pick.append(nums[i])
                                            if n == 10:
                                                pick.append(nums[j])
                                            if len(pick) == n and sum(pick) == s:
                                                count += 1
    print(count)