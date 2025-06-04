def bubblesort(lst):
    res = 0
    n = len(lst)
    for i in reversed(range(1, n)):
        for idx in range(i):
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
                res = res + 1
    return res

def get_data():
    while 1:
        t = input()
        if t.strip() == '0':
            return
        val = int(t)
        s = []
        for __ in range(val):
            s += [int(input())]
        cnt = bubblesort(s)
        print(cnt)

if __name__ == '__main__':
    get_data()