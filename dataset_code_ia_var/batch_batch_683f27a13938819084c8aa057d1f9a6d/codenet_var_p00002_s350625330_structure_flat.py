while True:
    try:
        s = input()
    except:
        break
    nums = s.split()
    ints = []
    for n in nums:
        ints.append(int(n))
    total = 0
    for x in ints:
        total += x
    total_str = str(total)
    print(len(total_str))