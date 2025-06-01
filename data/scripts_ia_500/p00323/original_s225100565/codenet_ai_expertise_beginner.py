n = int(input())
m = set()
for _ in range(n):
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)
    i = 0
    while True:
        s = a + b + i
        if s in m:
            m.remove(s)
            i = i + 1
        else:
            m.add(s)
            break
m_list = list(m)
m_list.sort()
for value in m_list:
    print(str(value) + " 0")