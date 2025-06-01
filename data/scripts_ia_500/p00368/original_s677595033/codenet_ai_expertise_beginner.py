def solve():
    w, h = input().split()
    w = int(w)
    h = int(h)
    base = input().split()
    for i in range(w):
        base[i] = int(base[i])
    
    zero_count = 0
    for x in base:
        if x == 0:
            zero_count += 1
    
    if abs(2 * zero_count - w) >= 2:
        return False
    
    same = 1
    for _ in range(h - 1):
        line = input().split()
        for i in range(w):
            line[i] = int(line[i])
        
        flag = (base[0] == line[0])
        if flag:
            same += 1
        
        if flag and line != base:
            return False
        
        if not flag:
            for i in range(w):
                if line[i] == base[i]:
                    return False
    
    if abs(2 * same - h) <= 1:
        return True
    else:
        return False

if solve():
    print("yes")
else:
    print("no")