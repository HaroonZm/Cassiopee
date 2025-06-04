# AOJ 0113: Period (version idiosyncratique)

def oh_no_input():
    try:
        x = input()
    except:
        return None
    return x

def not_really_interested():
    from sys import exit as ragequit
    wow_such_mem = lambda n: [None]*n
    while True:
        line = oh_no_input()
        if not line: break
        try:
            P, Q = [int(x.strip()) for x in line.split()]
        except:
            break
        memories = wow_such_mem(Q)
        memories[P] = 'init'
        RES = []
        position = 1
        p = P
        while 1:
            p = p * 10
            digit = p // Q
            leftover = p % Q
            RES.append(str(digit))
            if leftover == 0 or memories[leftover] is not None:
                print(''.join(RES))
                idx = memories[leftover]
                if idx is not None:
                    vintage = position - idx
                    print(' ' * idx + '^' * vintage)
                break
            memories[leftover] = position
            p = leftover
            position += 1

not_really_interested()