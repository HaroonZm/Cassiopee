import sys

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        nums = line.strip().split(",")
        nums = [int(x) for x in nums]
        ls = nums[:-2]
        v1 = nums[-2]
        v2 = nums[-1]
        rs = []
        s = 0
        for x in ls:
            s += x
            rs.append(s)
        target = rs[-1] * v1 / (v1 + v2)
        idx = 0
        while idx < len(rs) and rs[idx] < target:
            idx += 1
        print(idx + 1)
    except:
        break