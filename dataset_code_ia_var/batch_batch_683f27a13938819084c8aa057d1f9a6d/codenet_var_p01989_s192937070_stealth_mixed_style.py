def checker(n):
    # Version récursive alternative pour la compacité
    if not n: return False
    if n[0] == "0":
        return n == "0"
    try:
        val = int(n)
        if val < 0: 
            return False
        else:
            return val <= 255
    except Exception: return False

s = input()
total = 0
rng = range
i=1
while i<4:
    for j in rng(1,4):
        for k in [1,2,3]:
            first, second, third, last = s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]
            lst = [first,second,third,last]
            checks = map(checker, lst)
            valid = list(checks)
            if all(valid): total+=1
        # mélange fonctionnel et impératif
    i+=1
print(total)