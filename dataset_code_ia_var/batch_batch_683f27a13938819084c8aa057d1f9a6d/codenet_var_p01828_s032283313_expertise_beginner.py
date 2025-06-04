import sys

def get_str_list():
    s = sys.stdin.readline()
    return list(s.strip())

def B():
    s = get_str_list()
    t = get_str_list()
    n = len(s)
    # Premier cas: positions paires
    t1 = []
    i = 0
    while i*2 < n:
        t1.append(s[i*2])
        i += 1
    j = 0
    if len(t1) == 0:
        print("Yes")
        return
    for i in range(n):
        if j < len(t1) and t[i] == t1[j]:
            j += 1
            if j == len(t1):
                print("Yes")
                return
    # Deuxième cas: positions impaires
    t2 = []
    i = 0
    while i*2+1 < n:
        t2.append(s[i*2+1])
        i += 1
    j = 0
    if len(t2) == 0:
        print("Yes")
        return
    for i in range(n):
        if j < len(t2) and t[i] == t2[j]:
            j += 1
            if j == len(t2):
                print("Yes")
                return
    print("No")

if __name__ == "__main__":
    B()