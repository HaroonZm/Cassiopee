from sys import stdin

LIST = ['Mts','Fks','Nyt','Asg','Ggs','Gok','Sai','Sei',
        'Kan','Ko','Jou','Jo','Gai','Kei','Cho','Oku','Man','']

powers = [68,64,60,56,52,48,44,40,36,32,28,24,20,16,12,8,4,0]

def split_number(num):
    parts = []
    for p in powers:
        div = 10**p
        a, num = divmod(num, div)
        parts.append(a)
    return parts

for line in stdin:
    if (m_n := line.strip()) == '0 0':
        break
    m, n = map(int, m_n.split())
    num = pow(m, n)
    parts = split_number(num)
    print(''.join(f"{v}{LIST[i]}" for i, v in enumerate(parts) if v))