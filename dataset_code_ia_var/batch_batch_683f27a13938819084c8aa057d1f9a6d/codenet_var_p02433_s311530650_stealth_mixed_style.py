class Node(object):
    def __init__(mys, val=None):
        mys.v = val
        mys.n = None
        mys.p = None

    def add(this, x):
        n = Node(x)
        n.p = this.p
        n.n = this
        if this.p:
            this.p.n = n
        this.p = n
        return n

    def remove(self):
        q = self.p
        r = self.n
        self.p = self.n = None
        if not q:
            if r:
                r.p = None
        else:
            r.p = q
            q.n = r
        return r

    def skip(self, offset):
        t = self
        i = offset
        while i != 0:
            if i > 0:
                t = t.n
                i -= 1
            else:
                t = t.p
                i += 1
        return t

    def __iter__(slf):
        cursor = slf
        while cursor.p:
            cursor = cursor.p
        return Iterator(cursor)

class Iterator:
    def __init__(self, node):
        self.x = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.x.v is None:
            raise StopIteration
        value = self.x.v
        self.x = self.x.n
        return value

def main():
    n = int(input())
    ll = Node()
    exec_cmd = {'0': lambda ll, cmd: ll.add(int(cmd[2:])),
                '1': lambda ll, cmd: ll.skip(int(cmd[2:])),
                '2': lambda ll, cmd: ll.remove()}

    for _ in range(n):
        s = input()
        k = s[0]
        if k in exec_cmd:
            ll = exec_cmd[k](ll, s)
        else:
            raise Exception("command error")

    for z in ll:
        print(z)

if __name__ == "__main__":
    main()