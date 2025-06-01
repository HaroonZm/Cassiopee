from sys import stdin

units = ['Man','Oku','Cho','Kei','Gai','Jo','Jou','Ko','Kan','Sei','Sai','Gok','Ggs','Asg','Nyt','Fks','Mts']

for line in stdin:
    m, n = map(int, line.split())
    if m == 0:
        break
    m = pow(m, n)
    result = []
    for d in range(68, 0, -4):
        unit_idx = (d - 4) // 4
        q, m = divmod(m, 10**d)
        if q:
            result.append(f"{q}{units[unit_idx]}")
    if m:
        result.append(str(m))
    print("".join(result))