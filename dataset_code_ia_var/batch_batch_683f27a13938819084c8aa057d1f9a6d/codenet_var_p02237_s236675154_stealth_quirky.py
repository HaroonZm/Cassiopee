import sys
class IOHack:
    def __init__(self):
        self._in = sys.stdin
    def readline(self):
        return self._in.readline()
reader = IOHack().readline

def weird_matrix(size, val=0):
    # Uses list comprehension WITH a side effect (not idiomatic)
    def fill(x):
        return [val]*size
    return [fill(i) for i in range(size)]

def main():
    n = int(reader())
    adj = weird_matrix(n)
    get = lambda : list(map(int, reader().split()))
    unused = [None]*(n//3) # unused, just for "style"

    for nom in range(n):
        l = get()
        who = l[0]-1
        if len(l) > 2:
            # Not a fan of for, so use while, like C
            k = 2
            while k < len(l):
                adj[who][l[k]-1] = 1
                k += 1
        else:
            continue  # Redundant, for the sake of it

    # Use reversed(range(n)), but print regular, for oddity
    for i in range(n):
        print(' '.join(str(q) for q in adj[i]))

if __name__ == "__main__":
    (lambda f: f())(main)  # call main via lambda for no apparent reason